<template>
  <div class="q-pa-md">
    <q-card v-for="employee in employees" :key="employee.id" class="my-card">
      <q-card-section>
        <div class="text-h6">{{ employee.name }}</div>
        <div class="text-subtitle2">{{ employee.position }}</div>
      </q-card-section>

      <q-card-section>
        <div class="text-caption">{{ employee.description }}</div>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="More Info" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getRequest } from "../utils/common";

const employees = ref([]);
const loading = ref(false);

const getAvailableEmployees = async () => {
  try {
    loading.value = true;
    const url = "https://backend.adalogix.es/user/list/available/";
    const response = await getRequest(url);
    response.forEach((employee) => {
      employees.value.push({
        id: employee.id,
        name: employee.role,
        position: employee.position,
        description: employee.description,
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

onMounted(getAvailableEmployees);
</script>

<style scoped>
.my-card {
  width: 300px;
  margin: 10px;
}
</style>
