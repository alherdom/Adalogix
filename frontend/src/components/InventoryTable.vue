<template>
  <q-table
    flat
    class="my-sticky-header-table"
    :rows="displayedItems"
    :columns="inventoryColumns"
    :loading="loading"
    row-key="id"
    v-model:selected="selectedRows"
    selection="multiple"
    :pagination="{ rowsPerPage: 20 }"
  >
    <template v-slot:top>
      <q-btn
        push
        size="12px"
        class="q-ml-sm q-mt-lg action-btn"
        color="white"
        text-color="black"
        :disable="loading"
        icon="delete"
        @click="deleteItems"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Delete Products
        </q-tooltip>
      </q-btn>
      <q-btn
        push
        size="12px"
        class="q-ml-xs q-mt-lg action-btn"
        color="white"
        text-color="black"
        :disable="loading"
        icon="upload"
        @click="openUploaderDialog"
        ><q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Upload Products
        </q-tooltip>
      </q-btn>
      <q-btn
        push
        size="12px"
        class="q-ml-xs q-mt-lg action-btn"
        color="white"
        text-color="black"
        :disable="loading"
        icon="download"
        @click="exportTable"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Export Table
        </q-tooltip>
      </q-btn>
      <q-btn
        push
        size="12px"
        class="q-ml-xs q-mt-lg action-btn"
        color="white"
        text-color="black"
        :disable="loading"
        icon="refresh"
        @click="fetchData"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Refresh Table
        </q-tooltip>
      </q-btn>
      <CodeScanner @decodedValues="handleDecodedValues" />
      <q-space />
      <q-input
        dense
        filled
        class="q-mt-sm q-pl-sm q-pt-sm action-btn"
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
    <!-- Row actions -->
    <template v-slot:body-cell-actions="props">
      <q-td>
        <q-btn
          flat
          size="sm"
          color="primary"
          icon="visibility"
          @click="productDetail(props.row)"
        />
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
          icon="delete"
          @click="deleteItem(props.row)"
        />
      </q-td>
    </template>
  </q-table>

  <!-- Dialogs-->
  <!-- url="http://localhost:8000/product/upload/" -->
  <q-dialog v-model="uploaderDialog">
    <q-uploader
      text-color="black"
      ref="uploader"
      url="https://backend.adalogix.es/product/upload/"
      label="Select a CSV file to upload"
      single-file
      accept=".csv"
      @uploaded="handleUpload"
    >
    </q-uploader>
  </q-dialog>
  <q-dialog v-model="editItemForm">
    <EditItemForm :item="itemData" @closeEditForm="closeEditItemForm" />
  </q-dialog>
  <q-dialog v-model="showProductDetail" >
    <ProductDetail class="product-detail-table"
      :productId="itemData.id.toString()"
      @closeProductDetail="closeProductDetailTable"
    />
  </q-dialog>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, onMounted, computed } from "vue";
import { exportFile, useQuasar } from "quasar";
import { inventoryColumns } from "src/utils/const";
import EditItemForm from "./EditItemForm.vue";
import ProductDetail from "./ProductDetail.vue";
import CodeScanner from "./CodeScanner.vue";

const handleDecodedValues = (value) => {
  console.log("Decoded value:", value);
};

const uploaderDialog = ref(false);
const openUploaderDialog = () => {
  uploaderDialog.value = true;
};

const handleUpload = () => {
  uploaderDialog.value = false;
  Swal.fire({
    icon: "success",
    title: "Success",
    text: "Products loaded successfully!",
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
  const columnsToExport = inventoryColumns.slice(0, -1);
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

const itemData = ref({});
const loading = ref(false);
const selectedRows = ref([]);
const items = ref([]);
const filter = ref("");
const editItemForm = ref(false);
const showProductDetail = ref(false);

const fetchData = async () => {
  try {
    loading.value = true;
    // const url = "http://localhost:8000/product/list/";
    const url = "https://backend.adalogix.es/product/list/";
    const response = await getRequest(url);
    items.value = response.map((item) => ({ ...item }));
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

const deleteItem = async (item) => {
  Swal.fire({
    title: "Delete Product",
    text: `Are you sure you want to delete ${item.name}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      // const url = `http://localhost:8000/product/delete/${item.id}/`;
      const url = `https://backend.adalogix.es/product/delete/${item.id}/`;
      const requestData = { product_id: item.id };
      try {
        const response = await deleteRequest(requestData, url);
        if (response.status === 200) {
          fetchData();
          Swal.fire({
            title: "Success",
            text: "Product deleted successfully!",
            icon: "success",
            showConfirmButton: false,
            timer: 1500,
          });
        }
      } catch (error) {
        console.error("Error deleting item:", error);
      }
    }
  });
};

const deleteItems = async () => {
  if (selectedRows.value.length === 0) {
    Swal.fire({
      title: "No products selected",
      text: "Please select products to delete",
      icon: "error",
      showConfirmButton: false,
      timer: 1500,
    });
    return;
  }
  Swal.fire({
    title: "Delete Products",
    text: "Are you sure you want to delete?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = {
        product_ids: selectedRows.value.map((item) => item.id),
      };
      // const url = "http://localhost:8000/product/delete/multiple/";
      const url = "https://backend.adalogix.es/product/delete/multiple/";
      try {
        const response = await deleteRequest(requestData, url);
        console.log(response);
        if (response.status === 200) {
          selectedRows.value = [];
          fetchData();
          Swal.fire({
            title: "Success",
            text: "Products deleted successfully!",
            icon: "success",
            showConfirmButton: false,
            timer: 1500,
          });
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

const productDetail = (itemProps) => {
  itemData.value = itemProps;
  showProductDetail.value = true;
};

const closeProductDetailTable = (value) => {
  showProductDetail.value = value;
  fetchData();
};

const displayedItems = computed(() => {
  return items.value.filter((item) => {
    if (!filter.value) return true;
    const search = filter.value.toLowerCase();
    return (
      item.id.toString().includes(search) ||
      item.name.toLowerCase().includes(search) ||
      item.description.toLowerCase().includes(search) ||
      item.category.toLowerCase().includes(search)
    );
  });
});
</script>
