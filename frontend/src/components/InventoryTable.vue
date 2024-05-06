<template>
  <q-table
    class="my-sticky-header-table"
    flat
    bordered
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
      <q-toolbar-title> Inventory Table </q-toolbar-title>
      <q-space />
      <div class="row">
        <div class="col-12 q-mt-md q-ml-xl q-mr-xl">
          <q-input
            outlined
            rounded
            dense
            debounce="300"
            color="primary"
            v-model="filter"
            placeholder="Search Item..."
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </div>
      </div>
      <q-space />
      <div class="row">
        <div class="col-12 q-mt-md q-mr-xl">
          <q-btn
            class="q-ml-xl"
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
            :disable="loading"
            no-caps
            dense
            flat
            label="Load Items"
            icon="cloud_upload"
            @click="openUploaderDialog"
          />
          <q-dialog v-model="uploaderDialog">
            <q-uploader
              text-color="black"
              ref="uploader"
              url="http://localhost:8000/product/upload/"
              label="Select a CSV file to upload"
              single-file
              accept=".csv"
              @uploaded="handleUpload"
            >
            </q-uploader>
          </q-dialog>
          <q-btn
            class="q-ml-sm"
            :disable="loading"
            no-caps
            dense
            flat
            label="Export CSV"
            icon="archive"
            @click="exportTable"
          />
        </div>
      </div>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td>
        <q-btn
          flat
          size="sm"
          color="primary"
          icon="edit"
          @click="editItem(props.row)"
        />
        <q-btn
          flat
          size="sm"
          color="primary"
          icon="visibility"
          @click="productDetail = true"
        />
      </q-td>
    </template>
  </q-table>
  <q-dialog v-model="editItemForm">
    <EditItemForm :item="itemData" @closeEditForm="closeEditItemForm" />
  </q-dialog>
  <q-dialog v-model="productDetail">
    <q-card style="width: 100%; max-width: 80vw">
      <q-card-section>
        <div class="text-h6">Full Width</div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        Click/Tap on the backdrop.
      </q-card-section>
      <q-card-actions align="right" class="bg-white text-teal">
        <q-btn flat label="OK" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, onMounted, computed } from "vue";
import { exportFile, useQuasar } from "quasar";
import EditItemForm from "./EditItemForm.vue";

const uploaderDialog = ref(false);
const openUploaderDialog = () => {
  uploaderDialog.value = true;
};

const handleUpload = () => {
  uploaderDialog.value = false;
  Swal.fire({
    icon: "success",
    title: "Items loaded successfully!",
  });
  fetchData();
};

function wrapCsvValue(val, formatFn, row) {
  let formatted = formatFn !== void 0 ? formatFn(val, row) : val;
  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);
  formatted = formatted.split('"').join('""');
  return `"${formatted}"`;
}

const $q = useQuasar();
const exportTable = () => {
  let rowsToExport =
    selectedRows.value.length > 0 ? selectedRows.value : items.value;
  const columnsToExport = columns.slice(0, -1);
  const content = [columnsToExport.map((col) => wrapCsvValue(col.label))]
    .concat(
      rowsToExport.map((row) =>
        columnsToExport
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
  },
  { name: "actions", label: "Actions", align: "left", field: "actions" },
];

const itemData = ref({});
const loading = ref(false);
const selectedRows = ref([]);
const items = ref([]);
const filter = ref("");
const editItemForm = ref(false);
const productDetail = ref(false);

const fetchData = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/product/list/";
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

const editItem = (itemProps) => {
  itemData.value = itemProps;
  editItemForm.value = true;
};

const closeEditItemForm = (value) => {
  editItemForm.value = value;
  fetchData();
};

const toggleExpand = (row) => {
  row.expanded = !row.expanded;
};

const isExpanded = (row) => {
  return row.expanded;
};

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
