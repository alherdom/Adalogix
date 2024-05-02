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
    <template v-slot:top>
      <q-toolbar-title>Inventory Table</q-toolbar-title>
      <q-btn
        class="q-ml-sm"
        color="primary"
        text-color="black"
        :disable="loading"
        no-caps
        dense
        flat
        label="Delete Items"
        icon="delete"
        @click="deleteItem"
      />
      <q-btn
        class="q-ml-sm"
        color="primary"
        text-color="black"
        :disable="loading"
        no-caps
        dense
        flat
        label="Load Data"
        icon="cloud_upload"
        @click="exportTable"
      />
      <q-btn
        class="q-ml-sm"
        color="primary"
        text-color="black"
        :disable="loading"
        no-caps
        dense
        flat
        label="Export CSV"
        icon="archive"
        @click="exportTable"
      />
      <q-space />
      <q-input
        borderless
        dense
        debounce="300"
        color="primary"
        v-model="filter"
        placeholder="Search Items..."
      >
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </template>
    <template v-slot:body="props"  >
        <q-tr :props="props" @click="props.expand = !props.expand"  >
          <q-td>
            <q-checkbox v-model="props.selected" color="grey-8"></q-checkbox>
          </q-td>
          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
            selected="single"
          >
            {{ col.value }}
          </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props" class="expandedRowTable">
          <q-td>
        <q-btn class="actions-btn" color="primary" flat icon="edit" @click="getData(props.row)" />
        <q-dialog v-model="editUserForm">
          <EditProductForm :data="rowData" @close="closeDialog"/>
        </q-dialog>
      </q-td>
          <q-td colspan="100%">
            <p>Description:</p>
            <p>{{ props.row.description }}</p>
          </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props" class="expandedRowTable">
          <q-td colspan="100%">
            <q-table flat square="" class="expandedRowTable" :rows="parseStore(props.row.stores)" :columns="extendedRowColumns" row-key="name" color="primary" hide-bottom hide-title/>
          </q-td>
        </q-tr>
      </template>    
  </q-table>
  <template>

  </template>
  
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { exportFile, useQuasar } from "quasar";
import { EdirProductForm } from "./EditProductForm.vue"
function wrapCsvValue(val, formatFn, row) {
  let formatted = formatFn !== void 0 ? formatFn(val, row) : val;
  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);
  formatted = formatted.split('"').join('""');
  return `"${formatted}"`;
}

function parseStore(store) {
  return JSON.parse(store)
}

const extendedRowColumns = [
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
  label: "Store",
  align: "left",
  field: "name",
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
  name: "address",
  required: true,
  label: "Address",
  align: "left",
  field: "address",
  sortable: true,
  },
]



const $q = useQuasar();

const exportTable = () => {
  const content = [columns.map((col) => wrapCsvValue(col.label))]
    .concat(
      items.value.map((row) =>
        columns
          .map((col) =>
            wrapCsvValue(
              typeof col.field === "function"
                ? col.field(row)
                : row[col.field === void 0 ? col.name : col.field],
              col.format,
              row
            )
          )
          .join(",")
      )
    )
    .join("\r\n");

  const status = exportFile("inventory-table.csv", content, "text/csv");

  if (status !== true) {
    $q.notify({
      message: "Browser denied file download...",
      color: "negative",
      icon: "warning",
    });
  }
};

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
  }
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
      const requestData = {
        product_ids: selectedRows.value.map((item) => item.id),
      };
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
</script>
