<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"
      ><img
        src="https://api.maptiler.com/resources/logo.svg"
        alt="MapTiler logo"
    /></a>
    <div class="map" ref="mapContainer"></div>
  </div>
  <q-drawer
    side="right"
    v-model="drawerRight"
    show-if-above
    bordered
    :width="350"
    :breakpoint="500"
    :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
    style="z-index: 100"
    class="router-drawer"
  >
    <div class="q-pa-lg">
      <div class="q-my-xl flex-container">
        <q-select
          filled
          v-model="selectedEmployee"
          :options="options"
          label="Employees"
          @update:model-value="getAgentRoute(), mainMarkRemove()"
        >
        </q-select>
        <q-select
          filled
          v-model="selectedStore"
          :options="storeOptions"
          label="Stores"
          @update:model-value="drawMark(), removeMapLayers()"
        >
        </q-select>
      </div>

      <div class="search-dropoff-container q-pa-sm">
        <q-input
          bottom-slots
          label="Search a place"
          :dense="dense"
          v-model="inputAddress"
          debounce="300"
          @update:model-value="setAddressOptions"
          class="input-address"
        >
        </q-input>
        <q-select
          v-model="selectedAddress"
          :options="addressOptions"
          label="Suggested address"
          class="suggest-address"
        >
          <template v-slot:before> <q-icon name="place" /> </template>
          <template v-slot:after
            ><q-btn
              round
              color="primary"
              icon="add"
              size="sm"
              push
              @click="drawByAddress"
          /></template>
        </q-select>
      </div>
      <div class="q-pa-xl sidebar-router-buttons">
        <q-btn
          :loading="loading[0]"
          color="primary"
          push
          @click="sendRequest"
          label="Calculate"
        />
        <q-btn
          :loading="loading[0]"
          color="primary"
          @click="deleteRoute()"
          label="Delete"
          push
        />
        <q-btn
          :loading="loading[0]"
          color="primary"
          @click="saveEmployeeStatus()"
          label="Save"
          push
          :disable="disable"
        />
      </div>
    </div>
    <q-list bordered separator>
      <template v-for="(waypoint, index) in waypointTable" :key="index">
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="fmd_good"></q-icon>
          </q-item-section>
          <q-item-section>{{ index + 1 }}</q-item-section>
          <q-item-section side>{{ waypoint }}</q-item-section>
        </q-item>
      </template>
    </q-list>
  </q-drawer>
</template>

<script setup>
import { Map, Marker, Popup } from "maplibre-gl";
import { shallowRef, onMounted, onUnmounted, markRaw, ref, toRaw } from "vue";
import { getRequest, patchRequest } from "src/utils/common";
import Swal from "sweetalert2";
import config from "../utils/keys";

const drawerRight = ref(true);
const mapContainer = shallowRef(null);
const map = shallowRef(null);
const markers = ref([]);
const agents = ref([{ start_location: [] }]);
const shipmentsPickup = ref([]);
const shipmentsDropoff = ref([]);
const travelMode = "drive";
const apiKey = config.geoapifyApiKey;
const options = ref([]);
const storeOptions = ref([]);
const selectedEmployee = ref(null);
const selectedStore = ref(null);
const loading = ref(false);
const disable = ref(true);
const inputAddress = ref("");
const addressOptions = ref([]);
const selectedAddress = ref("");
let mapLayers = [];
const waypointTable = ref([]);

const deleteRoute = async () => {
  try {
    loading.value = true;
    const requestData = {
      route: null,
      available: true,
    };
    const url = `http://localhost:8000/user/update/${selectedEmployee.value.value}/`;
    const response = await patchRequest(requestData, url);
    if (response.status === 200) {
      Swal.fire({
        title: "Success",
        text: "Route delete successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
      waypointTable.value = [];
      agentPlan.value = {};
      plan.value = {};
      removeMapLayers();
      disable.value = true;
    } else {
      alert("Error");
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};
const drawByAddress = async () => {
  let lng = selectedAddress.value.lng;
  let lat = selectedAddress.value.lat;
  if (mainMark.value) {
    let popupText = `${selectedAddress.value.label}`;
    let markerPopup = new Popup({
      anchor: "bottom",
      offset: [0, -64],
    }).setText(popupText);
    let marker = new Marker({ draggable: false, color: "#26A69A" })
      .setLngLat([lng, lat])
      .addTo(map.value)
      .setPopup(markerPopup);
    shipmentsDropoff.value.push({
      id: `order_${shipmentsDropoff.value.length + 1}`,
      pickup: {
        location: [shipmentsPickup.value[0], shipmentsPickup.value[1]],
      },
      delivery: {
        location: [lng, lat],
      },
    });
    markers.value.push(marker);
  }
};

function getAddressOptions() {
  let url = `https://api.geoapify.com/v1/geocode/autocomplete?text=${encodeURIComponent(
    inputAddress.value
  )}&format=json&apiKey=${apiKey}`;
  return fetch(url).then((response) => response.json());
}

const setAddressOptions = async () => {
  addressOptions.value = [];
  let response = await getAddressOptions();
  response.results.forEach((option) => {
    addressOptions.value.push({
      label: option.formatted,
      lng: option.lon,
      lat: option.lat,
    });
  });
  selectedAddress.value = addressOptions.value[0];
};

const saveEmployeeStatus = async () => {
  try {
    loading.value = true;
    const url = `http://localhost:8000/user/update/${selectedEmployee.value.value}/`;
    let requestData = {
      available: false,
      route: JSON.stringify(toRaw(plan.value)),
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
  } finally {
    loading.value = false;
  }
};

const agentPlan = ref({});

// -----------------------------

const getAgentRoute = async () => {
  try {
    loading.value = true;
    removeMapLayers();
    const url = `http://localhost:8000/user/detail/${selectedEmployee.value.value}/`;
    const response = await getRequest(url);
    if (response.available == false) {
      agentPlan.value = JSON.parse(response.route).features[0].properties;

      const rawAgentPlan = toRaw(agentPlan.value);
      const waypoints = rawAgentPlan.waypoints.map(
        (waypoint) => waypoint.location
      );

      await generateRoute(waypoints, travelMode).then((routeData) => {
        addRouteLayer(routeData);
      });

      await generateRouteTable(waypoints);

      addWaypointsLayer(rawAgentPlan);
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    loading.value = false;
  }
};

const generateRouteTable = async (waypoints) => {
  let url;
  for (let i = 0; i < waypoints.length; i++) {
    let waypoint = waypoints[i];
    url = `https://api.geoapify.com/v1/geocode/reverse?lat=${waypoint[1]}&lon=${waypoint[0]}&apiKey=${apiKey}`;
    let waypointsAddress = await fetch(url).then((response) => response.json());
    waypointTable.value.push(waypointsAddress.features[0].properties.formatted);
  }
};

const addWaypointsLayer = (agentPlan) => {
  const items = agentPlan.waypoints.map((waypoint, index) =>
    turf.point(waypoint.location, { index: index + 1 })
  );

  map.value.addSource(`waypoints-of-agent-${agentPlan.agentIndex}`, {
    type: "geojson",
    data: turf.featureCollection(items),
  });

  let waypointLayer = {
    id: `waypoints-of-agent-${agentPlan.agentIndex}`,
    type: "circle",
    source: `waypoints-of-agent-${agentPlan.agentIndex}`,
    paint: {
      "circle-radius": 15,
      "circle-color": "#FF6C37",
      "circle-stroke-width": 1,
      "circle-stroke-color": "#777777",
    },
  };

  map.value.addLayer(waypointLayer);
  mapLayers.push(waypointLayer);

  let waypointTextLayer = {
    id: `waypoints-text-of-agent-${agentPlan.agentIndex}`,
    type: "symbol",
    source: `waypoints-of-agent-${agentPlan.agentIndex}`,
    layout: {
      "text-field": "{index}",
      "text-allow-overlap": false,
      "text-font": ["Roboto", "Helvetica Neue", "sans-serif"],
      "text-size": 15,
    },
    paint: {
      "text-color": "#333333",
    },
  };

  map.value.addLayer(waypointTextLayer);
  mapLayers.push(waypointTextLayer);
};

const removeMapLayers = () => {
  if (map.value && mapLayers.length > 0) {
    mapLayers.forEach((layer) => {
      map.value.removeLayer(layer.id);
      map.value.removeSource(layer.source);
    });
    mapLayers = [];
  }
};

const getAvaiableEmployees = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/user/list/";
    const response = await getRequest(url);
    response.forEach((element) => {
      options.value.push({ label: element.username, value: element.id });
    });
  } catch (error) {
    console.error("Error fetching data:", error);
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Something went wrong while fetching data!",
    });
  } finally {
    loading.value = false;
  }
};

const addRouteLayer = (routeData) => {
  const layerId = `agent-route-${1}`;
  agentPlan.value.routeLayer = layerId;
  map.value.addSource(layerId, {
    type: "geojson",
    data: routeData,
  });
  let routeLayer = {
    id: layerId,
    type: "line",
    source: layerId,
    layout: {
      "line-cap": "round",
      "line-join": "round",
    },
    paint: {
      "line-color": "#FF6C37",
      "line-width": 3,
    },
  };

  map.value.addLayer(routeLayer);

  mapLayers.push(routeLayer);
};

const mainMarkRemove = () => {
  waypointTable.value = [];
  if (mainMark.value) {
    mainMark.value.remove();
  }
};

// -----------------------------

const getStores = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/store/list/";
    const response = await getRequest(url);
    response.forEach((element) => {
      storeOptions.value.push({
        label: element.name,
        value: element.id,
        longitude: element.longitude,
        latitude: element.latitude,
      });
    });
  } catch (error) {
    console.error("Error fetching data:", error);
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Something went wrong while fetching data!",
    });
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  const apiKey = config.maptilerApiKey;

  const initialState = {
    lng: -16.549341485486707,
    lat: 28.4031139299302,
    zoom: 13,
  };

  map.value = markRaw(
    new Map({
      container: mapContainer.value,
      style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${apiKey}`,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom,
    })
  );

  getAvaiableEmployees();

  getStores();
});

const mainMark = ref(null);

function drawMark() {
  shipmentsDropoff.value = [];
  if (mainMark.value) {
    mainMark.value.remove();
  }
  mainMark.value = new Marker({ draggable: false, color: "#FF6C37" })
    .setLngLat([selectedStore.value.longitude, selectedStore.value.latitude])
    .addTo(map.value);
  agents.value[0]["start_location"] = [
    selectedStore.value.longitude,
    selectedStore.value.latitude,
  ];
  shipmentsPickup.value = [
    selectedStore.value.longitude,
    selectedStore.value.latitude,
  ];
}

onUnmounted(() => {
  map.value?.remove();
});

let plan = ref({});
// Create the request

function sendRequest() {
  let requestData = {
    mode: "drive",
    agents: toRaw(agents.value),
    shipments: toRaw(shipmentsDropoff.value),
  };
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify(requestData);

  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  fetch(
    `https://api.geoapify.com/v1/routeplanner?apiKey=${config.geoapifyApiKey}`,
    requestOptions
  )
    .then((response) => response.json())
    .then((response) => {
      plan.value = response;
      let agentPlan = plan.value.features[0].properties;
      const waypoints = agentPlan.waypoints.map((waypoint) =>
        toRaw(waypoint.location)
      );
      console.log(waypoints);

      const waypointPromises = waypoints.map((waypoint) => {
        let url = `https://api.geoapify.com/v1/geocode/reverse?lat=${waypoint[1]}&lon=${waypoint[0]}&apiKey=${apiKey}`;
        return fetch(url).then((response) => response.json());
      });

      Promise.all(waypointPromises).then((waypointsAddress) => {
        waypointTable.value = waypointsAddress.map(
          (waypointAddress) => waypointAddress.features[0].properties.formatted
        );

        generateRoute(waypoints, travelMode /* 'drive', 'truck', ...*/).then(
          (routeData) => {
            const layerId = `agent-route-${1}`;
            agentPlan.routeLayer = layerId;
            map.value.addSource(layerId, {
              type: "geojson",
              data: routeData,
            });
            let routeLayer = {
              id: layerId,
              type: "line",
              source: layerId,
              layout: {
                "line-cap": "round",
                "line-join": "round",
              },
              paint: {
                "line-color": "#FF6C37",
                "line-width": 3,
              },
            };
            map.value.addLayer(routeLayer);
            mapLayers.push(routeLayer);
          }
        );

        if (markers.value !== null) {
          for (var i = markers.value.length - 1; i >= 0; i--) {
            markers.value[i].remove();
            mainMark.value.remove();
          }
        }

        const items = agentPlan.waypoints.map((waypoint, index) =>
          turf.point(waypoint.location, { index: index + 1 })
        );

        // create points source + layer

        map.value.addSource(`waypoints-of-agent-${agentPlan.agentIndex}`, {
          type: "geojson",
          data: turf.featureCollection(items),
        });

        let waypointLayer = {
          id: `waypoints-of-agent-${agentPlan.agentIndex}`,
          type: "circle",
          source: `waypoints-of-agent-${agentPlan.agentIndex}`,
          paint: {
            "circle-radius": 15,
            "circle-color": "#FF6C37", // set any color here
            "circle-stroke-width": 1,
            "circle-stroke-color": "#777777", // set a darker color here
          },
        };

        let waypointTextLayer = {
          id: `waypoints-text-of-agent-${agentPlan.agentIndex}`,
          type: "symbol",
          source: `waypoints-of-agent-${agentPlan.agentIndex}`,
          layout: {
            "text-field": "{index}",
            "text-allow-overlap": false,
            "text-font": ["Roboto", "Helvetica Neue", "sans-serif"],
            "text-size": 15,
          },
          paint: {
            "text-color": "#333333", // set contrast to the color textColor
          },
        };

        map.value.addLayer(waypointLayer);
        map.value.addLayer(waypointTextLayer);
        mapLayers.push(waypointLayer);
        mapLayers.push(waypointTextLayer);

        disable.value = false;
      });
    })
    .catch((error) => console.error(error));
}

function generateRoute(points, mode) {
  const waypoints = points
    .map((position) => position[1] + "," + position[0])
    .join("|");
  let url = `https://api.geoapify.com/v1/routing?waypoints=${waypoints}&mode=${mode}&apiKey=${apiKey}`;

  return fetch(url).then((resp) => resp.json());
}
</script>

<style scoped>
@import "/node_modules/maplibre-gl/dist/maplibre-gl.css";
@import "/node_modules/@geoapify/geocoder-autocomplete/styles/minimal.css";

.map-wrap {
  position: relative;
  width: 100%;
  height: 95vh;
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

.autocomplete-panel {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 400px;
  z-index: 1000;
}

.autocomplete-container {
  position: relative;
}

.suggest-address {
  width: 100%;
}

.input-address {
  width: 100%;
}

.search-dropoff-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
