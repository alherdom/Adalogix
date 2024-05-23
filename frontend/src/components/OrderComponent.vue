<template>
  <q-table
    flat
    :rows="displayedItems"
    :columns="columns"
    class="my-sticky-header-table"
    style="height: 93vh"
    :pagination="{ rowsPerPage: 20 }"
    row-key="id"
    v-model:selected="selectedRows"
    selection="multiple"
  >
    <template v-slot:top>
      <q-btn
        icon="add"
        color="white"
        text-color="black"
        push
        size="12px"
        class="q-ml-sm q-mt-lg action-btn"
        @click="openAddOrderForm"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Create order
        </q-tooltip>
      </q-btn>
      <q-btn
        push
        size="12px"
        class="q-ml-xs q-mt-lg action-btn"
        color="white"
        text-color="black"
        :disable="loading"
        icon="cancel"
        @click="deleteItems"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Cancel orders
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
        @click="getOrders"
      >
        <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Refresh orders
        </q-tooltip>
      </q-btn>
      <q-space />
      <q-input
        dense
        filled
        class="q-mt-sm q-pl-sm q-pt-sm action-btn"
        placeholder="Search Order..."
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
          By code, courier or status
        </q-tooltip>
      </q-input>
    </template>
    <template v-slot:body-cell-status="props">
      <q-td style="text-align: center">
        <q-badge outline :color="COLOR_STATUS[props.row.status]">{{
          props.row.status
        }}</q-badge>
      </q-td>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td style="text-align: center">
        <q-btn
          flat
          round
          size="sm"
          color="primary"
          icon="visibility"
          @click="orderDetail(props.row.id)"
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            View order detail
          </q-tooltip>
        </q-btn>
        <q-btn
          flat
          round
          size="sm"
          color="primary"
          icon="cancel"
          @click="deleteItem(props.row)"
        >
          <q-tooltip
            anchor="bottom middle"
            transition-show="scale"
            transition-hide="scale"
          >
            Cancel order
          </q-tooltip>
        </q-btn>
      </q-td>
    </template>
  </q-table>
  <q-dialog v-model="addOrderForm" maximized>
    <addOrderForm @closeOrderForm="closeOrderForm" />
  </q-dialog>
  <q-dialog v-model="showOrderDetail">
    <OrderDetail :orderProducts="orderData" :orderStore="orderStore" />
  </q-dialog>
</template>

<script setup>
import { deleteRequest, getRequest } from "src/utils/common";
import { computed, onMounted, ref } from "vue";
import AddOrderForm from "./AddOrderForm.vue";
import OrderDetail from "./OrderDetail.vue";
import { formatDate } from "src/utils/formatDate";
import Swal from "sweetalert2";

const loading = ref(false);
const selectedRows = ref([]);
const filter = ref("");

const COLOR_STATUS = {
  Completed: "secondary",
  "In progress": "primary",
};
const addOrderForm = ref(false);

const openAddOrderForm = () => {
  addOrderForm.value = true;
};

const columns = [
  {
    name: "order_id",
    required: true,
    label: "Order Code",
    align: "center",
    field: "id",
    sortable: true,
  },
  {
    name: "courier",
    required: false,
    label: "Courier Assigned",
    align: "center",
    field: "courier",
    sortabel: true,
  },
  {
    name: "date",
    required: true,
    label: "Creation Date",
    align: "center",
    field: "created_at",
    sortable: true,
  },
  {
    name: "completion_date",
    required: false,
    label: "Completion Date",
    align: "center",
    field: "completion_date",
    sortable: true,
  },
  {
    name: "status",
    required: true,
    label: "Status",
    align: "center",
    field: "status",
    sortable: true,
  },
  {
    name: "actions",
    required: true,
    label: "Actions",
    align: "center",
    field: "actions",
  },
];

const rows = ref([]);

const getOrders = async () => {
  try {
    loading.value = true;
    rows.value = [];
    // const url = "http://localhost:8000/order/list/";
    const url = "https://backend.adalogix.es/order/list/";
    const response = await getRequest(url);

    response.forEach((row) => {
      let completion_date;
      let courier;
      if (row.courier != null) {
        courier = `${row.courier.username} (${row.courier.first_name} ${row.courier.last_name})`;
      } else {
        courier = "➖";
      }

      if (row.completion_date != null) {
        completion_date = formatDate(row.completion_date);
      } else {
        completion_date = "➖";
      }
      const row_info = {
        id: row.id,
        courier: courier,
        created_at: formatDate(row.created_at),
        completion_date: completion_date,
        status: row.status == true ? "Completed" : "In progress",
      };
      rows.value.push(row_info);
    });
    // rows.value = response.map((row) => ({ ...row, courier: row.courier.username }));
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

const closeOrderForm = (value) => {
  addOrderForm.value = value;
  rows.value = [];
  getOrders();
};

const displayedItems = computed(() => {
  return rows.value.filter((row) => {
    if (!filter.value) return true;
    const search = filter.value.toLowerCase();
    return (
      row.id.toString().toLowerCase().includes(search) ||
      row.courier.toLowerCase().includes(search) ||
      row.status.toLowerCase().includes(search)
    );
  });
});

const deleteItems = async () => {
  if (selectedRows.value.length === 0) {
    Swal.fire({
      title: "No orders selected",
      text: "Please select orders to delete",
      icon: "error",
      showConfirmButton: false,
      timer: 1500,
    });
    return;
  }
  Swal.fire({
    title: "Cancel Orders",
    text: "Are you sure you want to cancel?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = {
        orders_ids: selectedRows.value.map((item) => item.id),
      };
      // const url = "http://localhost:8000/order/delete/multiple/";
      const url = "https://backend.adalogix.es/order/delete/multiple/";
      try {
        const response = await deleteRequest(requestData, url);
        if (response.status === 200) {
          selectedRows.value = [];
          rows.value = [];
          getOrders();
          Swal.fire({
            title: "Success",
            text: "Orders canceled successfully!",
            icon: "success",
            showConfirmButton: false,
            timer: 1500,
          });
        }
      } catch (error) {
        console.error("Error canceling orders:", error);
      }
    }
  });
};

const deleteItem = async (item) => {
  Swal.fire({
    title: "Cancel Order",
    text: `Are you sure you want to cancel the order ${item.id}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      // const url = `http://localhost:8000/order/delete/${item.id}/`;
      const url = `https://backend.adalogix.es/order/delete/${item.id}/`;
      const requestData = { order_id: item.id };
      try {
        const response = await deleteRequest(requestData, url);
        if (response.status === 200) {
          rows.value = [];
          getOrders();
          Swal.fire({
            title: "Success",
            text: "Order canceled successfully!",
            icon: "success",
            showConfirmButton: false,
            timer: 1500,
          });
        }
      } catch (error) {
        console.error("Error canceling order:", error);
      }
    }
  });
};

const orderStore = ref(null);
const orderData = ref([]);
const showOrderDetail = ref(false);

const orderDetail = async (orderId) => {
  // const url = `http://localhost:8000/order/detail/${orderId}/`
  const url = `https://backend.adalogix.es/order/detail/${orderId}/`;
  const response = await getRequest(url);
  orderStore.value = response.store.name;
  orderData.value = response.order_products;
  showOrderDetail.value = true;
};

onMounted(() => {
  getOrders();
});
</script>
