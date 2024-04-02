<template>
  <q-table
    class="my-sticky-header-table"
    flat
    bordered
    title="Inventory Table"
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
        class="exportTable"
        color="primary"
        no-caps
        flat
        dense
        text-color="black"
        icon-right="archive"
        label="Export to csv"
        @click="exportTable"
      />
    </template>
  </q-table>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "../utils/common";
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
        const url = "http://localhost:8000/product/list";
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

    const exportTable = () => {
      Swal.fire({
        title: "Exporting table...",
        text: "This feature is not implemented yet",
        icon: "info",
      });
    };

    return {
      columns,
      items,
      loading,
      selectedRows,
      exportTable,
    };
  },
};
</script>
