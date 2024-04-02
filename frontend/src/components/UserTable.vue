<template>
  <q-table
    class="my-sticky-header-table"
    flat
    bordered
    title="Users Table"
    :rows="items"
    :columns="columns"
    :loading="loading"
    row-key="id"
    v-model:selected="selectedRows"
    selection="multiple"
    :pagination="{ rowsPerPage: 20 }"
  >
    <template v-slot:top-right>
      <q-btn
        class="registerUser"
        color="primary"
        no-caps
        dense
        flat
        text-color="black"
        icon-right="add"
        label="Register new user"
        @click="registerUser"
      />
    </template>
  </q-table>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "src/utils/common";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
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
        name: "first_name",
        required: true,
        label: "Name",
        align: "left",
        field: "first_name",
        sortable: true,
      },
      {
        name: "last_name",
        required: true,
        label: "Name",
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
      {
        name: "role",
        required: true,
        label: "Role",
        align: "left",
        field: "role",
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

    const registerUser = () => {
     router.push("/register");
    };

    return {
      columns,
      items,
      loading,
      selectedRows,
      registerUser,
    };
  },
};
</script>
