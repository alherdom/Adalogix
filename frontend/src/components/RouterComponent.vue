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
    <q-select
      filled
      v-model="selectedEmployee"
      :options="options"
      label="Employees"
    >
    </q-select>
    <q-select
      filled
      v-model="selectedStore"
      :options="storeOptions"
      label="Stores"
      @update:model-value="drawMark()"
    >
    </q-select>
    <div class="search-dropoff-container">
      <q-input
        bottom-slots
        label="Dropoff places"
        :dense="dense"
        v-model="inputAddress"
        debounce="300"
        @update:model-value="setAddressOptions"
        class="input-address"
      >
      </q-input>
      <q-select
        filled
        v-model="selectedAddress"
        :options="addressOptions"
        label="label"
        class="suggest-address"
      >
        <template v-slot:before> <q-icon name="place" /> </template>
        <template v-slot:after
          ><q-btn
            round
            color="primary"
            icon="add"
            size="sm"
            @click="drawByAddress"
        /></template>
      </q-select>
    </div>

    <q-btn
      :loading="loading[0]"
      color="primary"
      @click="saveEmployeeStatus()"
      label="Save"
      :disable="disable"
    />
    <q-btn
      :loading="loading[0]"
      color="primary"
      @click="sendRequest"
      label="Calculate"
    />
    <div id="autocomplete" class="autocomplete-container"></div>
  </q-drawer>
</template>

<script setup>
import { Map, Marker, Popup } from "maplibre-gl";
import { shallowRef, onMounted, onUnmounted, markRaw, ref, toRaw } from "vue";
import { getRequest, patchRequest } from "src/utils/common";

const drawerRight = ref(true);
const mapContainer = shallowRef(null);
const map = shallowRef(null);
const markers = ref([]);
const agents = ref([{ start_location: [] }]);
const shipmentsPickup = ref([]);
const shipmentsDropoff = ref([]);
const travelMode = "drive";
const apiKey = "96100818ef1a4f1a8a50d609496386fa";
const options = ref([]);
const storeOptions = ref([]);
const selectedEmployee = ref(null);
const selectedStore = ref(null);
const loading = ref(false);
const disable = ref(true);
const inputAddress = ref("");
const addressOptions = ref([]);
const selectedAddress = ref("Address Options");

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
  console.log(response);
  response.results.forEach((option) => {
    console.log(option.formatted);
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

const getAvaiableEmployees = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/user/list/available/";
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
  const apiKey = "GMM53qEv5wFImFPJ6Rgl";

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

  console.log(requestData);

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
    "https://api.geoapify.com/v1/routeplanner?apiKey=96100818ef1a4f1a8a50d609496386fa",
    requestOptions
  )
    .then((response) => response.json())
    .then((response) => {
      plan.value = response;
      let agentPlan = plan.value.features[0].properties;
      const waypoints = agentPlan.waypoints.map(
        (waypoint) => waypoint.location
      );
      generateRoute(waypoints, travelMode /* 'drive', 'truck', ...*/).then(
        (routeData) => {
          const layerId = `agent-route-${1}`;
          agentPlan.routeLayer = layerId;
          map.value.addSource(layerId, {
            type: "geojson",
            data: routeData,
          });
          map.value.addLayer({
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
          });
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

      map.value.addLayer({
        id: `waypoints-of-agent-${agentPlan.agentIndex}`,
        type: "circle",
        source: `waypoints-of-agent-${agentPlan.agentIndex}`,
        paint: {
          "circle-radius": 15,
          "circle-color": "#FF6C37", // set any color here
          "circle-stroke-width": 1,
          "circle-stroke-color": "#777777", // set a darker color here
        },
      });

      map.value.addLayer({
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
      });
      disable.value = false;
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