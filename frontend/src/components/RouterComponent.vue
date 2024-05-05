<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"><img
        src="https://api.maptiler.com/resources/logo.svg" alt="MapTiler logo"/></a>
    <div class="map" ref="mapContainer"></div>
  </div>
  <q-dialog v-model="markerDialog" >
    <MarkerForm :markerPoint="markerPoint" @draw="drawMark"/>
  </q-dialog>
  <button @click="sendRequest">Calculate</button>
  <q-drawer 
        side="right"
        v-model="drawerRight"
        show-if-above
        bordered
        :width="200"
        :breakpoint="500"
        :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
        style="z-index: 100;"
      >
        <q-scroll-area class="fit">
          <div class="q-pa-sm">
            <div v-for="n in 50" :key="n">Drawer {{ n }} / 50</div>
          </div>
        </q-scroll-area>
        <q-btn flat @click="drawerRight = !drawerRight" round dense icon="menu" />
      </q-drawer>
  
</template>

<script setup>
import { Map, Marker } from 'maplibre-gl';
import { shallowRef, onMounted, onUnmounted, markRaw, ref, toRaw } from 'vue';
import MarkerForm from './MarkerForm.vue'
import { featureCollection, point } from '@turf/turf';

const drawerRight = ref(true)
const mapContainer = shallowRef(null);
const map = shallowRef(null);
const markerDialog = ref(false)
const markerPoint = ref({})
const markerCoordinates = ref({})
const markers = ref([])

onMounted(() => {
    const apiKey = 'GMM53qEv5wFImFPJ6Rgl';

    // const getLocation =  () => {
    //       return new Promise((resolve, reject) => {
    //          navigator.geolocation.getCurrentPosition(resolve, reject);
    //       });
    //     };
    //     // Destructure latitude and longitude from geolocation
    //     const position = await getLocation();
    //     const { latitude, longitude } = position.coords;
    //     // Fetch weather data based on obtained geolocation

    const initialState = { lng: -16.549341485486707, lat: 28.4031139299302, zoom: 13 };

    map.value = markRaw(new Map({
    container: mapContainer.value,
    style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${apiKey}`,
    center: [initialState.lng, initialState.lat],
    zoom: initialState.zoom
    }));

    map.value.on('click', (e) => {
    markerPoint.value = e.point
    markerCoordinates.value = e.lngLat.wrap()
    markerDialog.value = true
    })
})

function drawMark(type) {
    let markType = type.value
    let color;
    if (markType == 'pickup') {
        color = '#FFFF00'
    } else if (markType == 'dropoff') {
        color = '#ADD8E6'
    } else if (markType== "start") {
        color = "#FF6C37"
    }
    if (markType) {
        let marker;
        if (markType == 'start' && agents.value[0]['start_location'].length == 0) {
            marker = new Marker({draggable: false, color: color})
                .setLngLat([markerCoordinates.value.lng, markerCoordinates.value.lat])
                .addTo(map.value);
            agents.value[0]['start_location'] = [markerCoordinates.value.lng, markerCoordinates.value.lat]
            markers.value.push(marker)
        }
        if (markType == 'pickup' && shipmentsPickup.value.length == 0) {
            marker = new Marker({draggable: false, color: color})
                .setLngLat([markerCoordinates.value.lng, markerCoordinates.value.lat])
                .addTo(map.value);
            shipmentsPickup.value = [markerCoordinates.value.lng, markerCoordinates.value.lat]
            markers.value.push(marker)
        }
        if (markType == 'dropoff' && shipmentsPickup.value.length != 0 && agents.value[0]['start_location'].length != 0) {
            marker = new Marker({draggable: false, color: color})
                .setLngLat([markerCoordinates.value.lng, markerCoordinates.value.lat])
                .addTo(map.value);
                shipmentsDropoff.value.push({
                    "id": `order_${shipmentsDropoff.value.length + 1}`,
                    "pickup": {
                        "location": [
                            shipmentsPickup.value[0], shipmentsPickup.value[1]
                        ]
                    },
                    "delivery": {
                        "location": [
                            markerCoordinates.value.lng, markerCoordinates.value.lat
                        ]
                    }
                })
            markers.value.push(marker)
        }
    }



    markerDialog.value = false

}

onUnmounted(() => {
    map.value?.remove();
})

// Create the request

const agents = ref([{"start_location": []}])
const shipmentsPickup = ref([])
const shipmentsDropoff = ref([])
const travelMode = "drive"
const apiKey = "96100818ef1a4f1a8a50d609496386fa"

function sendRequest() {
    let requestData = {
        "mode": "drive",
        "agents": toRaw(agents.value),
        "shipments": toRaw(shipmentsDropoff.value)
    }

const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify(requestData)
  
const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("https://api.geoapify.com/v1/routeplanner?apiKey=96100818ef1a4f1a8a50d609496386fa", requestOptions)
  .then((response) => response.json())
  .then((response) => {
    let plan = response
    let agentPlan = plan.features[0].properties
    const waypoints = agentPlan.waypoints.map(waypoint => waypoint.location);
    generateRoute(waypoints, travelMode /* 'drive', 'truck', ...*/).then((routeData) => {
    const layerId = `agent-route-${1}`;
    agentPlan.routeLayer = layerId;
    map.value.addSource(layerId, {
      type: 'geojson',
      data: routeData
    });
    map.value.addLayer({
      'id': layerId,
      'type': 'line',
      'source': layerId,
      'layout': {
        'line-cap': "round",
        'line-join': "round"
      },
      'paint': {
        'line-color': "#FF6C37",
        'line-width': 3
      }
    });

})


if (markers.value!==null) {
  for (var i = markers.value.length - 1; i >= 0; i--) {
    markers.value[i].remove();
  }
}

const items = agentPlan.waypoints.map((waypoint, index) =>
    turf.point(waypoint.location, { index: index + 1 }))

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
    }})

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


    } )
  .catch((error) => console.error(error));
}

function generateRoute(points, mode) {
  const waypoints = points.map(position => position[1] + ',' + position[0]).join('|');
  let url = `https://api.geoapify.com/v1/routing?waypoints=${waypoints}&mode=${mode}&apiKey=${apiKey}`;

  return fetch(url).then((resp) => resp.json());
}


</script>

<style scoped>
@import '/node_modules/maplibre-gl/dist/maplibre-gl.css';

.map-wrap {
  position: relative;
  width: 100%;
  height: calc(100vh - 77px); /* calculate height of the screen minus the heading */
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