<template>
  <q-table
    class="my-sticky-dynamic"
    dense
    bordered
    title="Inventory Table"
    :rows="rows"
    :columns="columns"
    :loading="loading"
    row-key="id"
    virtual-scroll
    :virtual-scroll-item-size="48"
    :virtual-scroll-sticky-size-start="48"
    :pagination="pagination"
    :rows-per-page-options="[0]"
    @virtual-scroll="onScroll"
    v-model:selected="selectedRows"
    selection="multiple"
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
    <template v-slot:bottom-row>
      <q-tr>
        <q-td colspan="100%"> Button row </q-td>
      </q-tr>
    </template>

    <template v-slot:bottom> Button </template>
  </q-table>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "src/utils/common";
import { ref, computed, nextTick, onMounted } from "vue";

export default {
  setup() {
    // Define the reactive variables
    const nextPage = ref(2);
    const loading = ref(false);
    const lastPage = ref(0);
    const allRows = ref([]);
    const selectedRows = ref([]);

    // Function to fetch data from the server
    const fetchData = async () => {
      try {
        loading.value = true;
        const response = await getRequest("http://localhost:8000/product/list");
        allRows.value = response.results;
        lastPage.value = Math.ceil(response.count / response.results.length);
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

    // Life cycle hook
    onMounted(fetchData);

    // Export table function
    const exportTable = () => {
      Swal.fire({
        title: "Exporting table...",
        text: "This feature is not implemented yet",
        icon: "info",
      });
    };

    // Scroll infintie function
    const onScroll = ({ index, ref }) => {
      const lastIndex = allRows.value.length - 1;
      if (
        !loading.value &&
        nextPage.value <= lastPage.value &&
        index === lastIndex
      ) {
        loading.value = true;
        setTimeout(() => {
          nextPage.value++;
          nextTick(() => {
            ref.refresh();
            loading.value = false;
          });
        }, 500);
      }
    };

    // Define the columns of the table
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
        label: "Product Name",
        align: "left",
        field: "name",
        format: (val) => val,
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
        name: "price",
        required: true,
        label: "Price",
        align: "left",
        field: "price",
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
        name: "actions",
        label: "Actions",
        align: "left",
        field: "actions",
      },
    ];

    // Data and functions returned to be used in the template
    return {
      selectedRows,
      columns,
      rows: computed(() => allRows.value.slice(0, allRows.value.length - 1)),
      nextPage,
      loading,
      pagination: { rowsPerPage: 0 },
      onScroll,
      exportTable,
    };
  },
};
</script>
