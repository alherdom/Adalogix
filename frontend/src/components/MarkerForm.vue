<template>
    <q-card class="register-card">
    <q-card-section class="register-card">
      <div class="text-h5 text-center">Create a point</div>
    </q-card-section>
    <q-card-section>
      <q-form class="register-form">
        <q-select
        filled
        v-model="selectedType"
        label="Simple select"
        :options="markerTypes"
        behavior="menu"
         />
        <br>
        <q-btn
            color="primary"
            label="Put"
            type="button"
            class="register-btn"
            :loading="loading"
            @click="drawMark()"
          />
      </q-form>
    </q-card-section>
  </q-card>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const emit = defineEmits(['draw'])

    function drawMark() {
    emit('draw', selectedType)
    }
  
    const selectedType = ref(null)
    const markerTypes = ref(['start', 'pickup', 'dropoff'])


  </script>
  