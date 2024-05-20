<template>
  <q-card class="item-card card-container">
    <q-card-section>
      <div class="text-h5 text-center item-form-title">
        <div class="text-right">
          <q-btn flat dense icon="close" v-close-popup />
        </div>
        Create Order
      </div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="item-form">
        <q-select :options="storeOptions" v-model="store" filled label="Stores" outlined  @update:model-value="getStoreProducts" style="width: 10%;"/>
        <div class="order-container"> 
          <div class="table-container">
            <q-table
              flat
              :rows="rows"
              :columns="columns"
              style="padding: 30px; height: 60vh;"
              :rows-per-page-options="[0]"
              class="my-sticky-header-table"
              hide-bottom
            >
            <template v-slot:body-cell-quantity="props">
            <q-td style="width: 150px;">
       
                  <q-input
                    type="number"
                    filled
                    v-model="props.row.quantity"
                    style="width: 150px;"
                    :min="0"
                    :max="props.row.stock"
                  />
            </q-td>
        </template>
        <template v-slot:body-cell-action="props">
          <q-td style="width: 150px;">
            <q-btn
                    label="Add"
                    size="sm"
                    color="primary"
                    icon="add"
                    :disabled="props.row.quantity > props.row.stock || props.row.quantity === 0 || props.row.quantity === '0'"
                    @click="addProduct(props.row)"/>
                    
          </q-td>
        </template>
          </q-table>
          </div>
        <div class="orders-container">
          <q-scroll-area style="height: 100%; max-width: 98%; margin-top: 0px">
          <div v-for="(product, index) in products" :key="index">
            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="category"></q-icon>
              </q-item-section>
              <q-item-section style="text-align: start">{{ product.name }}</q-item-section>
              <q-item-section style="text-align: start">{{ product.quantity }}</q-item-section>
            </q-item>
          </div>
        </q-scroll-area>
        </div>
      </div>
        <q-btn push color="primary" label="Save" type="button" class="item-btn" style="width: 100px;" @click="saveOrder"/>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { getRequest, postRequest } from 'src/utils/common';
import Swal from 'sweetalert2';
import { onMounted, ref } from 'vue';

const products = ref([])
const storeOptions = ref([])
const store = ref(null)
const rows = ref([])
const emit = defineEmits(["closeOrderForm"]);
const columns = [
  {
    name: "id",
    required: true, 
    label: "Id",
    align: "left",
    field: "product"
  },
  {
    name: "name",
    required: true,
    label: "Name",
    align: "left",   
    field: "product_name"
  },
  {
    name: "stock",
    required: true,
    label: "Stock",
    align: "left",
    field: "stock"
  },
  {
    name: "quantity",
    required: false, 
    label: "Quantity",
    align: "left", 
    field: "quantity"
  },
  {
    name: "action",
    required: false, 
    label: "Action",
    align: "left", 
    field: "action"
  }
]

  const addProduct = (props) => {
    const product_info = {
      name: props.product_name,
      quantity: props.quantity,
      id: props.product
    }
    products.value.push(product_info)
  }

const getStores = async () => {
  const url = "http://localhost:8000/store/list/"
  const stores = await getRequest(url)
  stores.forEach((store) => {
    storeOptions.value.push({label: store['name'], value: store['id']})
  })
}

const getStoreProducts = async () => {
    try {
    // const url = "https://backend.adalogix.es/product/list/";
    const url = `http://localhost:8000/store/detail/${store.value.value}/`;
    const response = await getRequest(url);
    rows.value = response.map((row) => ({ ...row, quantity: 0}));
  } catch (error) {
    console.error("Error fetching data:", error);
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Something went wrong while fetching data!",
    });
  } 
};

const saveOrder = async () => {

  try {
    const products_data = []
    products.value.forEach((product) => {
    const product_info = {
      product: product.id,
      quantity: product.quantity
    }
    products_data.push(product_info)
    })

    const requestData = {
      store: store.value.value,
      products: products_data
    }

    // const url = `https:/backend.adalogix.es/user/reset_password/`;
    const url = "http://localhost:8000/order/create/"
    const response = await postRequest(requestData, url);
    console.log(response)
    if (response.status === 200) {
      emit("closeOrderForm", false)
      Swal.fire({
        title: "Success",
        text: "Password reset successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,

      });
    } else {
      console.log(response.status);
      alert("Error");
    }
  } catch (error) {
    console.error(error);
  }
};


onMounted(() => {
  getStores()
})
</script>

<style>

.order-container {
  border-top: 2px solid #eee;
  border-bottom: 2px solid #eee;
  display: flex;
  margin: 30px 0px;
}

.table-container {
  width: 70%;
  height: 20%;
}

.orders-container {
  width: 30%;
  display: flex;
  flex-direction: column;
  border-left: 2px solid #eee;
  padding: 30px;
}

.card-container {
  display: flex;
  flex-direction: column;
}
</style>