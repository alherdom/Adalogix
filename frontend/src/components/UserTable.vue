<template>
  <q-table class="my-sticky-header-table" flat bordered title="Users Table" :rows="items" :columns="columns"
  :loading="loading" row-key="user" v-model:selected="selectedRows" selection="multiple"
    :pagination="{ rowsPerPage: 20 }">
    <template v-slot:top-right>
      <q-input class="searchInput" v-model="search" debounce="300" dense placeholder="Search user..." />
      <q-btn-group class="myBtns">
        <q-btn push dense no-caps label="Delete Users" icon="delete" @click="deleteUser" />
        <q-btn push dense no-caps label="Export CSV" icon="download" @click="exportTable" />
        <q-btn push dense no-caps label="Register User" icon="person_add" @click="registerUser" />
      </q-btn-group>
    </template>
  </q-table>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const columns = [
  {
    name: "id",
    required: true,
    label: "Id",
    align: "left",
    field: "user",
    sortable: true,
  },
  {
    name: "userName",
    required: true,
    label: "Username",
    align: "left",
    field: "username",
    sortable: true,
  },
  {
    name: "role",
    required: true,
    label: "Role",
    align: "left",
    field: "role",
    sortable: true,
  },
  {
    name: "firstName",
    required: true,
    label: "First Name",
    align: "left",
    field: "first_name",
    sortable: true,
  },
  {
    name: "lastName",
    required: true,
    label: "Last Name",
    align: "left",
    field: "last_name",
    sortable: true,
  },
  {
    name: "email",
    required: true,
    label: "Email",
    align: "left",
    field: "email",
    sortable: true,
  },
];

const loading = ref(false);
const selectedRows = ref([]);
const items = ref([]);
const router = useRouter();

const fetchData = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/user/list";
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

const deleteUser = async () => {
  if (selectedRows.value.length === 0) {
    Swal.fire({
      title: "No users selected",
      text: "Please select users to delete",
      icon: "error",
      showConfirmButton: false,
      timer: 1500,
    });
    return;
  }
  Swal.fire({
    title: "Delete users?",
    text: "Are you sure you want to delete the selected users?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = { employee_ids: selectedRows.value.map((item) => item.user) };
      const url = "http://localhost:8000/user/delete/multiple/";
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

const registerUser = () => {
  router.push("/register");
};
</script>
