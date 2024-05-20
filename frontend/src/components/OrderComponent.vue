<template>
    <q-btn
        round
        color="primary"
        icon="add"
        size="m"
        push
        @click="openAddOrderForm"
        style="position: absolute; top: 9vh; left: 96vw; z-index: 999;"
    />
  <q-table
    flat
    :rows="rows"
    :columns="columns"
    class="q-ma-xl my-sticky-header-table"
    style="height: 80vh; border: 2px solid #FF6C37;; border-radius: 10px;"
    :rows-per-page-options="[0]"
    hide-bottom
    >
    <template v-slot:body-cell-status="props">
    <q-td>
      <q-badge outline :color="COLOR_STATUS[props.row.status]">{{ props.row.status }}</q-badge>
    </q-td>
    </template>
  </q-table>
    <q-dialog v-model="addOrderForm" maximized>
        <addOrderForm @closeOrderForm="closeOrderForm"/>
  </q-dialog>
</template>

<script setup>
import { getRequest } from 'src/utils/common';
import { onMounted, ref } from 'vue';
import AddOrderForm from './AddOrderForm.vue';
import { formatDate } from 'src/utils/formatDate';

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
    align: "left",   
    field: "id",
    sortable: true,
  },
  {
    name: "courier",
    required: false,
    label: "Courier",
    align: "left",
    field: "courier",
    sortabel: true
  },
  {
    name: "date",
    required: true, 
    label: "Creation Date",
    align: "left",
    field: "created_at",
    sortable: true
  },
  {
    name: "completion_date",
    required: false,
    label: "Completion Date",
    align: "left",
    field: "completion_date",
    sortable: true
  },
  {
    name: "status",
    required: true,
    label: "Status",
    align: "left",
    field: "status",
    sortable: true
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
        courier = '----------------'
      }
      
      console.log(row)
      
      if (row.completion_date != null)  {
        completion_date = formatDate(row.completion_date)
      } else {
        completion_date = '----------------'
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
  getOrders()
}

onMounted(() => {
  getOrders()
})




</script>
