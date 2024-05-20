<template>
  <q-table
  flat
  :rows="displayedItems"
  :columns="columns"
  class="my-sticky-header-table"
  style="height: 93vh;"
  :pagination="{ rowsPerPage: 20 }"
  row-key="id"
  v-model:selected="selectedRows"
  selection="multiple"
  >
  <template v-slot:top>
    <q-btn
        icon="add"
        size="12px"
        color="white"
        text-color="black"
        push
        class="q-ml-sm q-mt-lg action-btn"
        @click="openAddOrderForm"
    >
    <q-tooltip
          anchor="bottom middle"
          transition-show="scale"
          transition-hide="scale"
        >
          Create Order
        </q-tooltip>
    </q-btn>
    <q-btn
        push
        size="12px"
        class="q-ml-sm q-mt-lg action-btn"
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
          Cancel Orders
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
          By courier, creation date, completion date or status
        </q-tooltip>
      </q-input>
    </template>
    <template v-slot:body-cell-status="props">
    <q-td style="text-align: center;">
      <q-badge outline :color="COLOR_STATUS[props.row.status]">{{ props.row.status }}</q-badge>
    </q-td>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td style="text-align: center;">
        <q-btn
            flat
            round
            size="sm"
            color="primary"
            icon="cancel"
            @click="deleteItem(props.row)"
          />
      </q-td>
    </template>
  </q-table>
    <q-dialog v-model="addOrderForm" maximized>
        <addOrderForm @closeOrderForm="closeOrderForm"/>
  </q-dialog>
</template>

<script setup>
import { deleteRequest, getRequest } from 'src/utils/common';
import { computed, onMounted, ref } from 'vue';
import AddOrderForm from './AddOrderForm.vue';
import { formatDate } from 'src/utils/formatDate';
import Swal from 'sweetalert2';

const loading = ref(false);
const selectedRows = ref([])
const filter = ref("");

const COLOR_STATUS = {
  'Completed': "secondary",
  'In progress': "primary"
}
const addOrderForm = ref(false);


const openAddOrderForm = () =>  {
    addOrderForm.value = true
}


const columns = [
  {
    name: "order_id",
    required: true,
    label: "Order id",
    align: "center",
    field: "id",
    sortable: true,
  },
  {
    name: "courier",
    required: false,
    label: "Courier",
    align: "center",
    field: "courier",
    sortabel: true
  },
  {
    name: "date",
    required: true,
    label: "Creation Date",
    align: "center",
    field: "created_at",
    sortable: true
  },
  {
    name: "completion_date",
    required: false,
    label: "Completion Date",
    align: "center",
    field: "completion_date",
    sortable: true
  },
  {
    name: "status",
    required: true,
    label: "Status",
    align: "center",
    field: "status",
    sortable: true
  },
  {
    name: "actions",
    required: true,
    label: "Actions",
    align: "center",
    field: "actions",
  },
]

const rows = ref([])


const getOrders = async () => {
  try {
    // const url = "https://backend.adalogix.es/product/list/";
    const url = "http://localhost:8000/order/list/";
    const response = await getRequest(url);

    console.log(response)
    response.forEach((row) => {
      let completion_date;
      let courier;
      if (row.courier != null) {
        courier = `${row.courier.username} (${row.courier.first_name} ${row.courier.last_name})`
      } else {
        courier = '➖'
      }

      console.log(row)

      if (row.completion_date != null)  {
        completion_date = formatDate(row.completion_date)
      } else {
        completion_date = '➖'
      }
      const row_info = {
        id: row.id,
        courier: courier,
        created_at: formatDate(row.created_at),
        completion_date: completion_date,
        status: row.status == true ? 'Completed' : 'In progress'
      }
      rows.value.push(row_info)
    })
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
  addOrderForm.value = value
  rows.value = []
  getOrders()
}

const displayedItems = computed(() => {
  return rows.value.filter((row) => {
    console.log(row)
    if (!filter.value) return true;
    const search = filter.value.toLowerCase();
    return (
      row.created_at.toLowerCase().includes(search) ||
      row.completion_date.toLowerCase().includes(search) ||
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
    text: "Cancel Orders",
    title: "Are you sure you want to cancel?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = {
        orders_ids: selectedRows.value.map((item) => item.id),
      };
      // const url = "https://backend.adalogix.es/product/delete/multiple/";
      const url = "http://localhost:8000/order/delete/multiple/";
      try {
        const response = await deleteRequest(requestData, url);
        console.log(response);
        if (response.status === 200) {
          selectedRows.value = [];
          rows.value = []
          getOrders()
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
    text: `Are you sure you want to cancel the Order Nº${item.id}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      // const url = `https://backend.adalogix.es/product/delete/${item.id}/`;
      const requestData = { order_id: item.id };
      const url = `http://localhost:8000/order/delete/${item.id}/`;
      try {
        const response = await deleteRequest(requestData, url);
        console.log(response);
        if (response.status === 200) {
          rows.value = []
          getOrders()
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


onMounted(() => {
  getOrders()
})




</script>
