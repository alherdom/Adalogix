<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark">
      <img
        src="https://api.maptiler.com/resources/logo.svg"
        alt="MapTiler logo"
      />
    </a>
    <!--Here is where the map will be rendered-->
    <div class="map" ref="mapContainer">
      <div class="q-mini-drawer-hide absolute" style="top: 15px; right: 360px">
        <q-btn
          dense
          round
          unelevated
          color="primary"
          icon="chevron_right"
          @click="drawer = !drawer"
        ></q-btn>
      </div>
    </div>
    <q-list
      bordered
      separator
      v-if="dropoffPointsTable.length && userIsCourier"
      class="courier-route-list"
    >
      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-icon name="fmd_good"></q-icon>
        </q-item-section>
        <q-item-section style="margin-right: -400px">1</q-item-section>
        <q-item-section style="text-align: start">{{
          startPointTable
        }}</q-item-section>
      </q-item>
      <div v-for="(point, index) in dropoffPointsTable" :key="index">
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="fmd_good"></q-icon>
          </q-item-section>
          <q-item-section style="margin-right: -400px">{{
            index + 2
          }}</q-item-section>
          <q-item-section style="text-align: start">{{ point }}</q-item-section>
        </q-item>
      </div>
    </q-list>
    <q-btn
      v-if="dropoffPointsTable.length && userIsCourier"
      @click="finishCourierRoute"
      push
      color="primary"
      class="finish-button"
      >Finish</q-btn
    >
  </div>
  <!--Beginning of the drawer-->

  <div
    v-if="!drawer && userIsAdmin"
    style="position: absolute; top: 65px; right: 10px; z-index: 2000"
  >
    <q-btn round push color="primary" @click="drawer = !drawer">
      <q-icon :name="drawer ? 'chevron_right' : 'chevron_left'" />
    </q-btn>
  </div>

  <q-drawer
    elevated
    side="right"
    v-model="drawer"
    overlay
    bordered
    :mini="miniState"
    :width="350"
    :breakpoint="500"
    v-if="userIsAdmin"
    class="router-drawer"
  >
    <div
      v-if="drawer"
      style="position: absolute; top: 15px; right: 330px; z-index: 2000"
    >
      <q-btn
        round
        push
        color="primary"
        :icon="drawer ? 'chevron_right' : 'chevron_left'"
        @click="drawer = !drawer"
      />
    </div>

    <div class="select-inputs">
      <q-select
        filled
        label="Courier"
        :options="employeesListOptions"
        v-model="employeeSelected"
        @update:model-value="setCourierRoute"
        ><q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Select a courier
        </q-tooltip>
        <template v-slot:append> <q-icon name="person" /> </template>
      </q-select>
      <q-select
        filled
        label="Order"
        :options="storesListOptions"
        v-model="storeSelected"
        @update:model-value="setStartPoint"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Select an order
        </q-tooltip>

        <template v-slot:append> <q-icon name="place" /> </template>
      </q-select>
      <q-separator />

      <div class="search-place-inputs">
        <q-input
          bottom-slots
          placeholder="Search a place..."
          filled
          v-model="searchAddress"
          debounce="300"
          style="font-size: 16px"
          @update:model-value="setAddressOptions"
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            Search for an address
          </q-tooltip>
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-select
          filled
          v-model="addressSelected"
          :options="addressesListOptions"
          label="Suggested addresses"
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            Select an suggested address
          </q-tooltip>
          <template v-slot:after
            ><q-btn
              round
              color="primary"
              icon="add"
              size="sm"
              push
              @click="setDropoffPoint"
            >
              <q-tooltip
                anchor="bottom middle"
                transition-show="scale"
                transition-hide="scale"
              >
                Add dropoff
              </q-tooltip>
            </q-btn>
          </template>
        </q-select>
      </div>
    </div>
    <div class="drawer-buttons">
      <q-btn
        color="primary"
        push
        @click="drawLayers"
        label="Calculate"
        :disable="
          layers.length != 0 ||
          startPoint == null ||
          dropoffPoints.length == 0 ||
          startPointTable == null
        "
        style="height: 45px"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Calculate route from set points
        </q-tooltip>
      </q-btn>
      <div class="ds-buttons">
        <q-btn
          color="primary"
          push
          @click="deleteRoute"
          label="Delete"
          style="width: 100%; height: 45px"
          :disable="
            layers.length == 0 &&
            startPointTable == null &&
            dropoffPointsTable.length == 0
          "
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            Delete the route
          </q-tooltip>
        </q-btn>
        <q-btn
          color="primary"
          push
          @click="saveCourierRoute"
          label="Save"
          style="width: 100%"
          :disable="layers.length == 0"
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            Save the route for the courier
          </q-tooltip>
        </q-btn>
      </div>
    </div>
    <q-separator />
    <q-scroll-area style="height: 65%; max-width: 98%; margin-top: -20px">
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
          <q-btn
            icon="close"
            round
            size="sm"
            flat
            @click="deleteStartPoint()"
          ></q-btn>
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
            <q-btn
              icon="close"
              round
              size="sm"
              flat
              @click="deleteDropoffPoint(index)"
            ></q-btn>
          </q-item-section>
        </q-item>
      </div>
    </q-scroll-area>
  </q-drawer>

  <!--End of the drawer-->
</template>

<script setup>
import { Map, Marker, Popup } from "maplibre-gl";
import { getRequest, patchRequest } from "src/utils/common";
import config from "src/utils/keys";
import Swal from "sweetalert2";
import { markRaw, onMounted, ref, shallowRef, toRaw } from "vue";

// Global constants

const drawer = ref(false);
const miniState = ref(false);
const userIsAdmin = localStorage.userGroup == "admin";
const userIsCourier = localStorage.userGroup == "courier";
const maptilerApiKey = config.maptilerApiKey;
const geoapifyApiKey = config.geoapifyApiKey;
const map = shallowRef(null);
const mapContainer = shallowRef(null);
const dropoffPointsTable = ref([]);
const startPointTable = ref(null);
const calculated = ref(false);
const layers = ref([]);
const routeSource = ref(null);
const waypointsSource = ref(null);
const orderId = ref(null);

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
    lng: -16.278529776841715,
    lat: 28.46727453908661,
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
  // let employeesListUrl = "http://localhost:8000/user/list/";
  let employeesListUrl = "https://backend.adalogix.es/user/list/";
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

const getOrders = async () => {
  // let ordersListUrl = "http://localhost:8000/order/list/";
  let ordersListUrl = "https://backend.adalogix.es/order/list/";
  let orders = await getRequest(ordersListUrl);
  return orders;
};

const setOrders = async () => {
  let orders = await getOrders();
  orders.forEach((order) => {
    if (order.status == false && order.courier == null) {
      storesListOptions.value.push({
        label: `Order ${order.id} (${order.store.name})`,
        value: order.id,
        lng: order.store.longitude,
        lat: order.store.latitude,
      });
    }
  });
};

const saveDropoffPointInfo = (lng, lat, address) => {
  let dropoffId = dropoffPoints.value.length;
  dropoffPointsInfo.value[`order_${dropoffId}`] = [lng, lat];
  dropoffPointsTable.value.push(address);
};

const drawMark = (lng, lat, color, address) => {
  if (!calculated.value) {
    const popup = new Popup({ offset: 25 }).setText(address);
    const mark = new Marker({ draggable: false, color: color })
      .setLngLat([lng, lat])
      .setPopup(popup)
      .addTo(map.value);
    mark.getElement().addEventListener("mouseenter", () => mark.togglePopup());
    mark.getElement().addEventListener("mouseleave", () => mark.togglePopup());
    return mark;
  }
};

const drawDropoffMark = (lng, lat, color, address) => {
  if (!calculated.value) {
    const popup = new Popup({ offset: 25 }).setText(address);
    const mark = new Marker({ draggable: false, color: color })
      .setLngLat([lng, lat])
      .setPopup(popup)
      .addTo(map.value);
    mark.getElement().addEventListener("mouseenter", () => mark.togglePopup());
    mark.getElement().addEventListener("mouseleave", () => mark.togglePopup());
    dropoffPoints.value.push(mark);
    saveDropoffPointInfo(lng, lat, address);
    return mark;
  }
};

const saveStartPointInfo = (lng, lat, address) => {
  startPointInfo.value = [parseFloat(lng), parseFloat(lat)];
  startPointTable.value = address;
};

const setStartPoint = async () => {
  if (startPoint.value) {
    startPoint.value.remove();
  }
  let lng = storeSelected.value.lng;
  let lat = storeSelected.value.lat;
  let color = "#FF6C37";
  let addres = await getAddressByCoords(lng, lat);

  startPoint.value = drawMark(lng, lat, color, addres);
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

const setDropoffPoint = () => {
  let lng = addressSelected.value.lng;
  let lat = addressSelected.value.lat;
  let color = "#85CBFA";
  let address = addressSelected.value.label;

  dropoffPoints.value.push(drawMark(lng, lat, color, address));
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
    let lng = waypoint.location[0];
    let lat = waypoint.location[1];
    let address = await getAddressByCoords(lng, lat);
    // The 0 is the startPoint and it's already in the startPointTable
    if (waypoints.indexOf(waypoint) !== 0) {
      dropoffPointsTable.value.push(address);
    }
  }
  return calculatedRouteData;
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

  if (routeSource.value) {
    routeSource.value = null;
  }

  if (waypointsSource.value) {
    waypointsSource.value = null;
  }

  calculatedRoute.routeLayer = layerId;

  routeSource.value = {
    type: "geojson",
    data: generatedRouteData,
  };

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

  waypointsSource.value = {
    type: "geojson",
    data: turf.featureCollection(waypoints),
  };

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

  dropoffPoints.value = [];

  layers.value.forEach((layer) => {
    map.value.removeLayer(layer.id);
    map.value.removeSource(layer.source);
  });

  const routeLayer = await generateRouteLayer();
  const pointsLayer = await generatePointsLayer();
  layers.value.push(routeLayer, pointsLayer[0], pointsLayer[1]);
  map.value.addLayer(routeLayer);
  map.value.addLayer(pointsLayer[0]);
  map.value.addLayer(pointsLayer[1]);
  orderId.value = storeSelected.value.value;
};

const getAddressByCoords = async (lng, lat) => {
  let reverseAddressUrl = ` https://api.geoapify.com/v1/geocode/reverse?lat=${lat}&lon=${lng}&format=json&apiKey=${geoapifyApiKey}`;
  let reverseAddressResponse = await fetch(reverseAddressUrl).then((response) =>
    response.json()
  );
  return reverseAddressResponse.results[0].formatted;
};

const deleteDropoffPoint = (index) => {
  dropoffPoints.value[index].remove();
  delete dropoffPointsInfo.value[`order_${index + 1}`];
  delete dropoffPointsTable.value.splice(index, 1);
  dropoffPoints.value.splice(index, 1);
};

const deleteStartPoint = () => {
  startPoint.value.remove();
  startPointInfo.value = null;
  startPointTable.value = null;
};

const unassignCourierOrder = async () => {
  // const url = `http://localhost:8000/order/update/${orderId.value}/`
  const url = `https://backend.adalogix.es/order/update/${orderId.value}/`;
  const requestData = {
    courier: null,
  };
  await patchRequest(requestData, url);
};

const deleteRoute = async () => {
  Swal.fire({
    title: "Delete route",
    text: "Are you sure you want to delete?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      if (startPoint.value != null) {
        startPoint.value.remove();
      }
      if (dropoffPoints.value.length > 0) {
        dropoffPoints.value.forEach((dropoffPoint) => {
          dropoffPoint.remove();
        });
      }

      dropoffPoints.value = [];

      const sourceToRemove = new Set();

      layers.value.forEach((layer) => {
        map.value.removeLayer(layer.id);
        sourceToRemove.add(layer.source);
      });

      sourceToRemove.forEach((source) => map.value.removeSource(source));

      if (employeeSelected.value) {
        const employeeId = employeeSelected.value.value;
        try {
          // const url = `http://localhost:8000/user/update/${employeeId}/`;
          const updateUrl = `https://backend.adalogix.es/user/update/${employeeId}/`;
          const updateRequestData = {
            available: true,
            route: null,
          };

          const deleteUrl = `https://backend.adalogix.es/order/courier/delete/${employeeId}/`;
          const [updateResponse, deleteResponse] = await Promise.all([
            patchRequest(updateRequestData, updateUrl),
            patchRequest(updateRequestData, deleteUrl),
          ]);

          if (updateResponse.status === 200 && deleteResponse.status === 200) {
            Swal.fire({
              icon: "success",
              title: "Route Deleted",
              text: "The route was successfully deleted!",
              timer: 1500,
            });
          } else {
            console.log("error");
          }
        } catch (error) {
          console.error("Error fetching data:", error);
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong while fetching data!",
          });
        }
      }
      layers.value = [];
      startPointInfo.value = null;
      startPointTable.value = null;
      dropoffPointsInfo.value = [];
      dropoffPointsTable.value = [];
      calculated.value = false;
    }
  });

  await unassignCourierOrder();
};

const saveOrderAssignment = async () => {
  const orderId = storeSelected.value.value;
  // const url = `http://localhost:8000/order/update/${orderId}/`
  const url = `https://backend.adalogix.es/order/update/${orderId}/`;
  const requestData = {
    courier: employeeSelected.value.value,
  };
  await patchRequest(requestData, url);
};

const saveCourierRoute = async () => {
  const dataForCourier = JSON.stringify({
    order: storeSelected.value.value,
    layers: toRaw(layers.value),
    startPoint: toRaw(startPointTable.value),
    dropoffPoints: toRaw(dropoffPointsTable.value),
    sourceRouteData: toRaw(routeSource.value),
    sourceWaypontsData: toRaw(waypointsSource.value),
  });

  const employeeId = employeeSelected.value.value;

  try {
    // const url = `http://localhost:8000/user/update/${employeeId}/`;
    const url = `https://backend.adalogix.es/user/update/${employeeId}/`;
    const requestData = {
      available: false,
      route: dataForCourier,
    };

    const response = await patchRequest(requestData, url);

    if (response.status === 200) {
      Swal.fire({
        icon: "success",
        title: "Status save",
        text: "Status save successfully!",
        timer: 1500,
      });
    } else {
      console.log("error");
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Something went wrong while fetching data!",
    });
  }

  await saveOrderAssignment();

  dropoffPoints.value = [];
};

// Finish Admin functions

// Courier functions

// TODO: Refactor this function

const setCourierRoute = async () => {
  let courierId;
  if (userIsAdmin) {
    courierId = employeeSelected.value.value;
  } else if (userIsCourier) {
    courierId = localStorage.userId;
  }
  // const getCourierRouterInfoUrl = `http://localhost:8000/user/detail/${courierId}/`;
  const getCourierRouterInfoUrl = `https://backend.adalogix.es/user/detail/${courierId}/`;
  const courierRouteInfo = await getRequest(getCourierRouterInfoUrl);
  const sourceToRemove = new Set();

  if (layers.value.length != 0) {
    layers.value.forEach((layer) => {
      map.value.removeLayer(layer.id);
      sourceToRemove.add(layer.source);
    });
    sourceToRemove.forEach((source) => map.value.removeSource(source));
    layers.value = [];
    startPointTable.value = null;
    dropoffPointsTable.value = [];
    startPointInfo.value = null;
    dropoffPointsInfo.value = [];
  }

  if (courierRouteInfo.route) {
    if (startPoint.value != null) {
      startPoint.value.remove();
    }
    if (dropoffPoints.value.length > 0) {
      dropoffPoints.value.forEach((dropoffPoint) => {
        dropoffPoint.remove();
      });
    }
    const courierRoute = JSON.parse(courierRouteInfo.route);
    if (courierRoute) {
      orderId.value = courierRoute.order;
      calculated.value = true;
      layers.value = courierRoute.layers;
      dropoffPointsTable.value = courierRoute.dropoffPoints;
      startPointTable.value = courierRoute.startPoint;
      routeSource.value = courierRoute.sourceRouteData;
      waypointsSource.value = courierRoute.sourceWaypontsData;
      map.value.addSource("agent-route-1", toRaw(routeSource.value));
      map.value.addSource("waypoints-of-agent-1", toRaw(waypointsSource.value));
      layers.value.forEach((layer) => map.value.addLayer(layer));
    }
  } else {
    calculated.value = false;
  }
};

const finishOrder = async () => {
  // const url = `http://localhost:8000/order/update/${orderId.value}/`
  const url = `https://backend.adalogix.es/order/update/${orderId.value}/`;
  const completion_date = new Date().toISOString();
  const requestData = {
    status: true,
    completion_date: completion_date,
  };
  await patchRequest(requestData, url);
};

const finishCourierRoute = async () => {
  Swal.fire({
    title: "Are you sure you want to finish this route?",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      try {
        const requestData = {
          route: null,
          available: true,
        };
        // const url = `http://localhost:8000/user/update/${localStorage.userId}/`;
        const url = `https://backend.adalogix.es/user/update/${localStorage.userId}/`;
        const response = await patchRequest(requestData, url);
        if (response.status === 200) {
          Swal.fire({
            title: "Success",
            text: "Route finished successfully",
            icon: "success",
            showConfirmButton: false,
            timer: 1500,
          });
          dropoffPointsTable.value = [];
          startPointTable.value = null;
          const sourceToRemove = new Set();

          layers.value.forEach((layer) => {
            map.value.removeLayer(layer.id);
            sourceToRemove.add(layer.source);
          });

          sourceToRemove.forEach((source) => map.value.removeSource(source));
        } else {
          alert("Error");
        }
      } catch (error) {
        console.error(error);
      }
    }
  });

  await finishOrder();
};

// Finish courier functions

onMounted(() => {
  mountMap();

  if (userIsAdmin) {
    map.value.on("click", async (event) => {
      let lng = event.lngLat.lng;
      let lat = event.lngLat.lat;
      let address = await getAddressByCoords(lng, lat);
      let color = "#85CBFA";
      drawDropoffMark(lng, lat, color, address);
    });
    setEmployees();
    setOrders();
  }

  if (userIsCourier) {
    map.value.on("style.load", () => {
      setCourierRoute();
    });
  }
});
</script>

<style>
/* Style necessary to render the map properly */

.finish-button {
  position: absolute;
  left: 50%;
  top: 90%;
  width: 100px;
  height: 40px;
}

.courier-route-list {
  position: absolute;
  left: 70%;
  top: 1%;
  background-color: white;
  border-radius: 10px;
  width: 550px;
}

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

.router-drawer {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 50px;
  background-color: #eeeeee;
}

.drawer-buttons {
  display: flex;
  flex-direction: column;
  padding: 0px 30px;
  justify-content: space-around;
  gap: 15px;
  margin-bottom: -20px;
  margin-top: -20px;
}

.ds-buttons {
  display: flex;
  justify-content: space-around;
  gap: 15px;
}

.select-inputs {
  padding: 0px 30px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  justify-items: center;
}

.search-place-inputs {
  display: flex;
  margin-top: 5px;
  flex-direction: column;
}
/* --------------------------------------------- */
</style>
