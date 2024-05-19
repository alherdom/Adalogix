<template>
    <q-btn
        color="primary"
        icon="add"
        size="sm"
        push
        @click="openAddOrderForm"
    />
  <q-table
    flat
    :rows="rows"
    :columns="columns"
    class="q-ma-xl"
    />
    <q-dialog v-model="addOrderForm">
        <addOrderForm />
  </q-dialog>
</template>

<script setup>
import { getRequest } from 'src/utils/common';
import { onMounted, ref } from 'vue';
import AddOrderForm from './AddOrderForm.vue';

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
        field: "id"
    },
    {
        name: "courier",
        required: false,
        label: "Courier",
        align: "left",
        field: "courier"
    },
    {
        name: "date",
        required: true, 
        label: "Creation Date",
        align: "left",
        field: "created_at"
    },
    {
        name: "status",
        required: true,
        label: "Status",
        align: "left",
        field: "status"
    },
]

const rows = ref([])

const getOrders = async () => {
    try {
    // const url = "https://backend.adalogix.es/product/list/";
    const url = "http://localhost:8000/order/list/";
    const response = await getRequest(url);
    console.log(response)
    rows.value = response.map((row) => ({ ...row }));
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

onMounted(() => {
    getOrders()
})




</script>
