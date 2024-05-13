<template>
  <q-table
    flat
    class="my-sticky-header-table"
    title="Inventory Table"
    :rows="displayedItems"
    :columns="columns"
    :loading="loading"
    row-key="id"
    v-model:selected="selectedRows"
    selection="multiple"
    :pagination="{ rowsPerPage: 20 }"
  >
    <template v-slot:top>
      <q-input
        dense
        filled
        class="q-mr-sm q-mt-sm"
        placeholder="Search Product..."
        debounce="300"
        color="primary"
        v-model="filter"
      >
        <template v-slot:append>
          <q-icon name="search" />
        </template>
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          By name, description or category
        </q-tooltip>
      </q-input>
    </template>
  </q-table>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest } from "../utils/common";
import { ref, onMounted, computed } from "vue";

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
    name: "quantity",
    required: true,
    label: "Quantity",
    align: "left",
    field: "quantity",
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
    name: "price",
    required: true,
    label: "Price",
    align: "left",
    field: "price",
    sortable: true,
  },
  {
    name: "weight",
    required: true,
    label: "Weight",
    align: "left",
    field: "weight",
    sortable: true,
  },
  {
    name: "volume",
    required: true,
    label: "Volume",
    align: "left",
    field: "volume",
    sortable: true,
  },
];

const loading = ref(false);
const selectedRows = ref([]);
const items = ref([]);
const filter = ref("");

const fetchData = async () => {
  try {
    loading.value = true;
    const url = "https://backend.adalogix.es/product/list/lowstock/";
    const response = await getRequest(url);
    items.value = response.map((item) => ({ ...item, expanded: false }));
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

const displayedItems = computed(() => {
  return items.value.filter((item) => {
    if (!filter.value) return true;
    const search = filter.value.toLowerCase();
    return (
      item.name.toLowerCase().includes(search) ||
      item.description.toLowerCase().includes(search) ||
      item.category.toLowerCase().includes(search)
    );
  });
});
</script>

<style scoped>
.my-sticky-header-table {
  height: 50%;
}
</style>
