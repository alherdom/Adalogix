<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark">
      <img src="https://api.maptiler.com/resources/logo.svg" alt="MapTiler logo"/>
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
    :options="employeesList"
  >
  <template v-slot:before> <q-icon name="person" /> </template>
  </q-select>

  </q-drawer>
  <!--End of the drawer-->

  
</template>

<script setup>
import { Map } from 'maplibre-gl';
import { getRequest } from 'src/utils/common';
import config from 'src/utils/keys';
import { markRaw, onMounted, ref, shallowRef } from 'vue';

// Global constants

const userIsAdmin = localStorage.userGroup == "admin"
const userIsCourier = localStorage.userGroup == "courier"
const maptilerApiKey = config.maptilerApiKey
const map = shallowRef(null)
const mapContainer = shallowRef(null)

// Finish Global constants

// Admin site constants

const employeesList = ref([])

// Finish Admin site constants

// Global functions

function mountMap() {
  // Function to mount the map, we use the coordinates of Puerto de La Cruz like initial point
  const initialState = {
    lng: -16.549341485486707,
    lat: 28.4031139299302,
    zoom: 13,
  }

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
  let employeesListUrl = "http://localhost:8000/user/list/"
  let employees = await getRequest(employeesListUrl)
  return employees
}

const setEmployees = async () => {
  let employees = await getEmployees()
  employees.forEach((employee) => {
    let employeeInfo = {
      label: `${employee.frist_name} ${employee.last_name} (${employee.username})`,
      value: employee.id
    }
    employeesList.value.push = employeeInfo
  })
}

// Finish Admin functions

onMounted(() =>  {
  mountMap()

  if (userIsAdmin) {
    setEmployees()
  }
  }
)

</script>

<style>
/* Style necessary to render the map properly */
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
/* --------------------------------------------- */
</style>