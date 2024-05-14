<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark">
      <img
        src="https://api.maptiler.com/resources/logo.svg"
        alt="MapTiler logo"
      />
    </a>
    <!--Here is where the map will be rendered-->
    <div class="map" ref="mapContainer"></div>
  </div>
  <!--Beginning of the drawer-->
  <q-drawer
    side="right"
    v-model="drawerRight"
    show-if-above
    bordered
    :width="350"
    style="z-index: 100"
    v-if="userIsAdmin"
  >
    <q-select
      filled
      label="Employees"
      :options="employeesListOptions"
      v-model="employeeSelected"
    >
      <template v-slot:before> <q-icon name="person" /> </template>
    </q-select>
    <q-select
      filled
      label="Stores"
      :options="storesListOptions"
      v-model="storeSelected"
      @update:model-value="setStartPoint"
    >
      <template v-slot:before> <q-icon name="place" /> </template>
    </q-select>
    <q-input
      bottom-slots
      label="Search a place"
      :dense="dense"
      v-model="searchAddress"
      debounce="300"
      @update:model-value="setAddressOptions"
    >
    </q-input>
    <q-select
      v-model="addressSelected"
      :options="addressesListOptions"
      label="Suggested address"
    >
      <template v-slot:before> <q-icon name="place" /> </template>
      <template v-slot:after
        ><q-btn
          round
          color="primary"
          icon="add"
          size="sm"
          push
          @click="setDropoffPoint"
      /></template>
    </q-select>
    <q-btn color="primary" push @click="drawLayers" label="Calculate"/>
    <q-btn color="primary" push @click="deleteRoute" label="Delete"/>
    <q-scroll-area style="height: 65%; max-width: 98%">
      <q-item v-if="startPointTable">
        <q-item-section avatar v-if="!calculated">
            <q-icon name="fmd_good" color="primary"></q-icon>
          </q-item-section>
          <q-item-section
            v-if="calculated"
            style="margin-right: -200px; font-weight: bold"
            >1</q-item-section
          >
          <q-item-section style="margin-left: -20px">{{
            startPointTable
          }}</q-item-section>
          <q-item-section avatar v-if="!calculated" class="delete-dropoff-btn">
            <q-btn icon="close" round size="sm" flat @click="deleteStartPoint()"></q-btn>
          </q-item-section>
      </q-item>
      <div v-for="(point, index) in dropoffPointsTable" :key="index">
        <q-item v-if="point">
          <q-item-section avatar v-if="!calculated">
            <q-icon name="fmd_good" color="info"></q-icon>
          </q-item-section>
          <q-item-section
            v-if="calculated"
            style="margin-right: -200px; font-weight: bold"
            >{{ index + 2 }}</q-item-section
          >
          <q-item-section style="margin-left: -20px">{{
            point
          }}</q-item-section>
          <q-item-section avatar v-if="!calculated" class="delete-dropoff-btn">
            <q-btn icon="close" round size="sm" flat @click="deleteDropoffPoint(index)"></q-btn>
          </q-item-section>
        </q-item>
      </div>
    </q-scroll-area>
  </q-drawer>
  <!--End of the drawer-->
</template>

<script setup>
import { Map, Marker, Popup } from "maplibre-gl";
import { event } from "quasar";
import { getRequest } from "src/utils/common";
import config from "src/utils/keys";
import { markRaw, onMounted, ref, shallowRef, toRaw } from "vue";

// Global constants

const userIsAdmin = localStorage.userGroup == "admin";
const userIsCourier = localStorage.userGroup == "courier";
const maptilerApiKey = config.maptilerApiKey;
const geoapifyApiKey = config.geoapifyApiKey;
const map = shallowRef(null);
const mapContainer = shallowRef(null);
const dropoffPointsTable = ref([]);
const startPointTable = ref(null)
const calculated = ref(false);
const layers = ref([])

// Finish Global constants

// Admin site constants

const employeesListOptions = ref([]);
const employeesDict = ref({});
const employeeSelected = ref(null);

const storesListOptions = ref([]);
const storeSelected = ref(null);
const startPoint = ref(null);
const startPointInfo = ref(null);

const searchAddress = ref("");
const addressesListOptions = ref([]);
const addressSelected = ref(null);
const dropoffPoints = ref([]);
const dropoffPointsInfo = ref({});

const routeWaypoints = ref([]);

// Finish Admin site constants

// Global functions

function mountMap() {
  // Function to mount the map, we use the coordinates of Puerto de La Cruz like initial point
  const initialState = {
    lng: -16.549341485486707,
    lat: 28.4031139299302,
    zoom: 13,
  };

  map.value = markRaw(
    new Map({
      container: mapContainer.value,
      style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${maptilerApiKey}`,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom,
    })
  );
}

// Finish Global functions

// Admin site functions

const getEmployees = async () => {
  let employeesListUrl = "http://localhost:8000/user/list/";
  let employees = await getRequest(employeesListUrl);
  return employees;
};

const setEmployees = async () => {
  let employees = await getEmployees();
  let employeesInfoList = [];
  // Employee information is stored in a dictionary for later use,
  // thus saving the fetch to the detail endpoint.
  let employeesInfoDict = {};
  employees.forEach((employee) => {
    if (employee.role == "Courier") {
      employeesInfoDict[employee.id] = employee;
      let employeeInfo = {
        label: `${employee.username}  (${employee.first_name} ${employee.last_name})`,
        value: employee.id,
      };
      employeesInfoList.push(employeeInfo);
    }
  });
  employeesDict.value = employeesInfoDict;
  employeesListOptions.value = employeesInfoList;
};

const getStores = async () => {
  let storesListUrl = "http://localhost:8000/store/list/";
  let stores = await getRequest(storesListUrl);
  return stores;
};

const setStores = async () => {
  let stores = await getStores();
  stores.forEach((store) => {
    storesListOptions.value.push({
      label: store.name,
      value: store.id,
      lng: store.longitude,
      lat: store.latitude,
    });
  });
};

const drawMark = (lng, lat, color) => {
  if (!calculated.value) {
    const mark = new Marker({ draggable: false, color: color })
      .setLngLat([lng, lat])
      .addTo(map.value);
    return mark;
  }
};

const saveStartPointInfo = (lng, lat, address) => {
  startPointInfo.value = [parseFloat(lng), parseFloat(lat)];
  startPointTable.value = address
};

const setStartPoint = async () => {
  if (startPoint.value) {
    startPoint.value.remove();
  }
  let lng = storeSelected.value.lng;
  let lat = storeSelected.value.lat;
  let color = "#FF6C37";
  let addres = await getAddressByCoords(lng, lat);

  let info = new Popup({
    anchor: "bottom",
    offset: [0, -64],
  }).setText(addres);

  startPoint.value = drawMark(lng, lat, color).setPopup(info);
  saveStartPointInfo(lng, lat, addres);
};

const getAddressOptions = async () => {
  let autocompleteAddressUrl = `https://api.geoapify.com/v1/geocode/autocomplete?text=${encodeURIComponent(
    searchAddress.value
  )}&format=json&apiKey=${geoapifyApiKey}`;
  let addresses = await fetch(autocompleteAddressUrl).then((response) =>
    response.json()
  );
  return addresses;
};

const setAddressOptions = async () => {
  addressesListOptions.value = [];
  let addresses = await getAddressOptions();
  addresses.results.forEach((address) => {
    let addressInfo = {
      label: address.formatted,
      lng: address.lon,
      lat: address.lat,
    };
    addressesListOptions.value.push(addressInfo);
  });
  addressSelected.value = addressesListOptions.value[0];
};

const saveDropoffPointInfo = (lng, lat, address) => {
  let dropoffId = dropoffPoints.value.length;
  dropoffPointsInfo.value[`order_${dropoffId}`] = [lng, lat];
  dropoffPointsTable.value.push(address);
};

const setDropoffPoint = () => {
  let lng = addressSelected.value.lng;
  let lat = addressSelected.value.lat;
  let color = "#85CBFA";
  let info = new Popup({
    anchor: "bottom",
    offset: [0, -64],
  }).setText(`${addressSelected.value.label}`);
  dropoffPoints.value.push(drawMark(lng, lat, color).setPopup(info));
  saveDropoffPointInfo(lng, lat, `${addressSelected.value.label}`);
};

const getCalculatedRoute = async () => {
  calculated.value = true;
  dropoffPointsTable.value = [];

  let agentData = [
    {
      start_location: toRaw(startPointInfo.value),
    },
  ];
  let shipmentsData = [];

  Object.keys(dropoffPointsInfo.value).forEach((orderId) => {
    let dropoffData = {
      id: orderId,
      pickup: {
        location: toRaw(startPointInfo.value),
      },
      delivery: {
        location: toRaw(dropoffPointsInfo.value[orderId]),
      },
    };
    shipmentsData.push(dropoffData);
  });

  let requestData = JSON.stringify({
    mode: "drive",
    agents: agentData,
    shipments: shipmentsData,
  });

  let headersData = new Headers();
  headersData.append("Content-Type", "application/json");

  let requestOptions = {
    method: "POST",
    headers: headersData,
    body: requestData,
    redirect: "follow",
  };

  let calculateRouteUrl = `https://api.geoapify.com/v1/routeplanner?apiKey=${geoapifyApiKey}`;

  let calculatedRouteData = await fetch(calculateRouteUrl, requestOptions).then(
    (response) => response.json()
  );

  let waypoints = calculatedRouteData.features[0].properties.waypoints;
  for (const waypoint of waypoints) {
    let lng = waypoint.location[0]
    let lat = waypoint.location[1]
    let address = await getAddressByCoords(lng, lat)
    // The 0 is the startPoint and it's already in the startPointTable
    if (waypoints.indexOf(waypoint) !== 0) {
      dropoffPointsTable.value.push(address)
    }
  }
  return calculatedRouteData
};

const setRouteWaypoints = async () => {
  if (routeWaypoints.value.length > 0) {
    routeWaypoints.value = [];
  }
  let calculatedRoute = await getCalculatedRoute();
  calculatedRoute.features[0].properties.waypoints.forEach((waypoint) => {
    waypoint.location;
    routeWaypoints.value.push(waypoint.location);
  });
  return calculatedRoute.features[0].properties;
};

const generateRoute = async (waypoints) => {
  let waypointsInfo = waypoints
    .map((waypoint) => waypoint[1] + "," + waypoint[0])
    .join("|");
  let generateRouteUrl = `https://api.geoapify.com/v1/routing?waypoints=${waypointsInfo}&mode=drive&apiKey=${geoapifyApiKey}`;
  let generatedRoute = await fetch(generateRouteUrl).then((response) =>
    response.json()
  );
  return generatedRoute;
};

const generateRouteLayer = async () => {
  const calculatedRoute = await setRouteWaypoints();
  const generatedRouteData = await generateRoute(routeWaypoints.value);
  const layerId = `agent-route-1`;

  calculatedRoute.routeLayer = layerId;

  map.value.addSource(layerId, {
    type: "geojson",
    data: generatedRouteData,
  });

  const routeLayer = {
    id: layerId,
    type: "line",
    source: layerId,
    layout: {
      "line-cap": "round",
      "line-join": "round",
    },
    paint: {
      "line-color": "#0F53FF",
      "line-width": 2,
    },
  };

  return routeLayer;
};

const generatePointsLayer = async () => {
  let waypoints = toRaw(routeWaypoints.value).map((waypoint, index) => {
    return turf.point(waypoint, { index: index + 1 });
  });

  map.value.addSource(`waypoints-of-agent-1`, {
    type: "geojson",
    data: turf.featureCollection(waypoints),
  });

  let pointLayer = {
    id: `waypoints-of-agent-1`,
    type: "circle",
    source: `waypoints-of-agent-1`,
    paint: {
      "circle-radius": 15,
      "circle-color": "#FFFFFF", // set any color here
      "circle-stroke-width": 2,
      "circle-stroke-color": "#000000", // set a darker color here
    },
  };

  let pointTextLayer = {
    id: `waypoints-text-of-agent-1`,
    type: "symbol",
    source: `waypoints-of-agent-1`,
    layout: {
      "text-field": "{index}",
      "text-allow-overlap": false,
      "text-font": ["Roboto", "Helvetica Neue", "sans-serif"],
      "text-size": 18,
    },
    paint: {
      "text-color": "#000000", // set contrast to the color textColor
    },
  };
  return [pointLayer, pointTextLayer];
};

const drawLayers = async () => {
  startPoint.value.remove();
  dropoffPoints.value.forEach((dropoffPoint) => {
    dropoffPoint.remove();
  });
  const routeLayer = await generateRouteLayer();
  const pointsLayer = await generatePointsLayer();
  layers.value.push(routeLayer, pointsLayer[0], pointsLayer[1])
  map.value.addLayer(routeLayer);
  map.value.addLayer(pointsLayer[0]);
  map.value.addLayer(pointsLayer[1]);
};

const getAddressByCoords = async (lng, lat) => {
  let reverseAddressUrl = ` https://api.geoapify.com/v1/geocode/reverse?lat=${lat}&lon=${lng}&format=json&apiKey=${geoapifyApiKey}`;
  let reverseAddressResponse = await fetch(reverseAddressUrl).then((response) =>
    response.json()
  );
  return reverseAddressResponse.results[0].formatted;
};

const deleteDropoffPoint = (index) => {
    dropoffPoints.value[index].remove()
    delete dropoffPointsInfo.value[`order_${index + 1}`]
    dropoffPointsTable.value[index] = null
}

const deleteStartPoint = () => {
  startPoint.value.remove()
  startPointInfo.value = null
  startPointTable.value = null
}

const deleteRoute = () => {
  layers.value.forEach((layer) => {
    map.value.removeLayer(layer.id); 
    map.value.removeSource(layer.source)
  });
  layers.value = []; 
  startPointInfo.value = null
  startPointTable.value = null
  dropoffPointsInfo.value = []
  dropoffPointsTable.value = []
  calculated.value = false
};

// Finish Admin functions

onMounted(() => {
  mountMap();

  if (userIsAdmin) {
    map.value.on("dblclick", async (event) => {
      let lng = event.lngLat.lng;
      let lat = event.lngLat.lat;
      let address = await getAddressByCoords(lng, lat);

      let color = "#85CBFA";
      let info = new Popup({
        anchor: "bottom",
        offset: [0, -64],
      }).setText(address);
      dropoffPoints.value.push(drawMark(lng, lat, color).setPopup(info));
      saveDropoffPointInfo(lng, lat, address);
    });
    setEmployees();
    setStores();
  }
});
</script>

<style>
/* Style necessary to render the map properly */
.map-wrap {
  position: relative;
  width: 100%;
  height: 94.5vh;
}

.map {
  position: absolute;
  width: 100%;
  height: 100%;
}

.watermark {
  position: absolute;
  left: 10px;
  bottom: 10px;
  z-index: 999;
}

.delete-dropoff-btn {
  margin: 0px 0px 40px;
}
/* --------------------------------------------- */
</style>
