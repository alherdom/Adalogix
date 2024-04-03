<template>
  <q-table class="my-sticky-header-table" flat bordered title="Inventory Table" :rows="items" :columns="columns"
    :loading="loading" row-key="id" v-model:selected="selectedRows" selection="multiple"
    :pagination="{ rowsPerPage: 20 }">
    <template v-slot:top-right>
        <q-input class="searchInput" v-model="search" debounce="300" dense placeholder="Search item..." />
      <q-btn-group class="myBtns">
        <q-btn push dense no-caps label="Delete Items" icon="delete" @click="deleteItem" />
        <q-btn push dense no-caps label="Export CSV" icon="download" @click="exportTable" />
        <q-btn push dense no-caps label="Load Data" icon="upload" @click="exportTable" />
      </q-btn-group>
    </template>
  </q-table>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";

const columns = [
  {
    name: "id",
    required: true,
    label: "Id",
    align: "left",
    field: "id",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "Name",
    align: "left",
    field: "name",
    sortable: true,
  },
  {
    name: "description",
    required: true,
    label: "Description",
    align: "left",
    field: "description",
    sortable: true,
  },
  {
    name: "category",
    required: true,
    label: "Category",
    align: "left",
    field: "category",
    sortable: true,
  },
  {
    name: "quantity",
    required: true,
    label: "Quantity",
    align: "left",
    field: "quantity",
    sortable: true,
  },
  {
    name: "price",
    required: true,
    label: "Price",
    align: "left",
    field: "price",
    sortable: true,
  },
];

const loading = ref(false);
const selectedRows = ref([]);
const items = ref([]);

const fetchData = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/product/list/";
    const response = await getRequest(url);
    items.value = response;
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

onMounted(fetchData);

const deleteItem = async () => {
  if (selectedRows.value.length === 0) {
    Swal.fire({
      title: "No items selected",
      text: "Please select items to delete",
      icon: "error",
      showConfirmButton: false,
      timer: 1500,
    });
    return;
  }
  Swal.fire({
    title: "Delete items?",
    text: "Are you sure you want to delete the selected items?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = { product_ids: selectedRows.value.map((item) => item.id) };
      const url = "http://localhost:8000/product/delete/multiple/";
      try {
        const response = await deleteRequest(requestData, url);
        if (response.status === 200) {
          selectedRows.value = [];
          fetchData();
        }
      } catch (error) {
        console.error("Error deleting items:", error);
      }
    }
  });
};

const exportTable = () => {
  Swal.fire({
    title: "Exporting table...",
    text: "This feature is not implemented yet",
    icon: "info",
  });
};
</script>
