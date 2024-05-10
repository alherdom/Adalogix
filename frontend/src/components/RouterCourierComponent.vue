<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"
      ><img
        src="https://api.maptiler.com/resources/logo.svg"
        alt="MapTiler logo"
    /></a>
    <div class="map" ref="mapContainer"></div>
    <q-btn
      class="completed-button"
      color="primary"
      push
      @click="completedRoute()"
      v-if="waypointTable.length"
      >Finish</q-btn
    >
    <q-list bordered separator class="route-table" v-if="waypointTable.length">
    <template v-for="waypoint, index in waypointTable" :key="index" >
    <q-item clickable v-ripple>
      <q-item-section avatar>
        <q-icon name="fmd_good"></q-icon>
      </q-item-section>
      <q-item-section>{{ index + 1}}</q-item-section>
      <q-item-section side>{{ waypoint }}</q-item-section>
    </q-item>
    </template>
    </q-list>
  </div>
</template>

<script setup>
import { Map } from "maplibre-gl";
import { shallowRef, onMounted, onUnmounted, markRaw, ref, toRaw } from "vue";
import { getRequest, patchRequest } from "src/utils/common";
import Swal from "sweetalert2";


const mapContainer = shallowRef(null);
const map = shallowRef(null);
const travelMode = "drive";
const apiKey = "96100818ef1a4f1a8a50d609496386fa";
const loading = ref(false);
const agentPlan = ref({});
const waypointTable = ref([]);
let mapLayers = []

const completedRoute = async () => {
  try {
    loading.value = true;
    const requestData = {
      route: null,
      available: true,
    };
    const url = `http://localhost:8000/user/update/${localStorage.userId}/`;
    const response = await patchRequest(requestData, url);
    if (response.status === 200) {
      Swal.fire({
        title: "Success",
        text: "Route finished successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
      waypointTable.value = []
      agentPlan.value = {}
      removeMapLayers()
    } else {
      alert("Error");
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
    }
};

const getAgentRoute = async () => {
  try {
    loading.value = true;
    const url = `http://localhost:8000/user/detail/${localStorage.userId}/`;
    const response = await getRequest(url);
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

  map.value.addLayer(routeLayer)

  mapLayers.push(routeLayer)
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

  map.value.addLayer(waypointLayer)
  mapLayers.push(waypointLayer)


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

  map.value.addLayer(waypointTextLayer)
  mapLayers.push(waypointTextLayer)
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

  getAgentRoute();
});

onUnmounted(() => {
  map.value?.remove();
});

// create points source + layer

async function generateRoute(points, mode) {
  const waypoints = points
    .map((position) => position[1] + "," + position[0])
    .join("|");
  let url = `https://api.geoapify.com/v1/routing?waypoints=${waypoints}&mode=${mode}&apiKey=${apiKey}`;

  const resp = await fetch(url);
  return await resp.json();
}

const removeMapLayers = () => {
  console.log(mapLayers.length)
  if (map.value && mapLayers.length > 0) {
    mapLayers.forEach((layer) => {
      map.value.removeLayer(layer.id);
      map.value.removeSource(layer.source);
    });
    mapLayers = []
  }
};

</script>

<style scoped>
@import "/node_modules/maplibre-gl/dist/maplibre-gl.css";

.map-wrap {
  position: relative;
  width: 100%;
  height: 95vh;
}

.completed-button {
  position: absolute;
  left: 50vw;
  bottom: 5%;
  z-index: 999;
}

.route-table {
  position: absolute;
  width: 550px;
  z-index: 999;
  top: 2%;
  left: 67vw;
  background-color: rgba(255, 255, 255, 0.89);
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
</style>
