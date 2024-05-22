<template>
  <q-card>
    <q-card-section>
        <div class="order-container">
          <div class="table-container">
            <q-table
              flat
              bordered
              :rows="rows"
              :columns="columns"
              style="height: 95vh"
              :rows-per-page-options="[0]"
              class="my-sticky-header-table"
              hide-bottom
            >
              <template v-slot:top>
                <div>
                  <q-select
                    :options="storeOptions"
                    v-model="store"
                    filled
                    label="Stores"
                    outlined
                    @update:model-value="getStoreProducts"
                    style="width: 250px"
                  />
                </div>
                <q-space />
                <div>
                  <q-btn
                    push
                    color="primary"
                    label="Create Order"
                    type="button"
                    class="item-btn"
                    style="width: 200px"
                    @click="saveOrder"
                  />
                </div>
              </template>
              <template v-slot:body-cell-quantity="props">
                <q-td
                  style="
                    display: flex;
                    height: auto;
                    align-items: center;
                    justify-content: center;
                    padding: 10px;
                  "
                >
                  <q-input
                    type="number"
                    filled
                    v-model="props.row.quantity"
                    style="width: 150px; padding: 0px"
                    :min="0"
                    :max="props.row.stock"
                  />
                </q-td>
              </template>
              <template v-slot:body-cell-action="props">
                <q-td style="width: 150px">
                  <q-btn
                    label="Add"
                    size="md"
                    color="primary"
                    icon="add"
                    :disabled="
                      props.row.quantity > props.row.stock ||
                      props.row.quantity === 0 ||
                      props.row.quantity === '0'
                    "
                    @click="addProduct(props.row)"
                  />
                </q-td>
              </template>
            </q-table>
          </div>
          <div class="orders-container">
            <div class="text-right" style="background-color: #eeeeee">
              <q-btn flat dense icon="close" v-close-popup />
            </div>
            <div>
              <q-toolbar-title
                class="text-center"
                style="
                  background-color: #eeeeee;
                  height: 96px;
                  border-bottom: 1px solid #e0e0e0;
                "
                >Products Order List</q-toolbar-title
              >
            </div>
            <q-scroll-area
              style="height: 100%; max-width: 98%; margin-top: 0px"
            >
              <div v-for="(product, index) in products" :key="index">
                <q-item>
                  <q-item-section avatar>
                    <q-icon name="label"></q-icon>
                  </q-item-section>
                  <q-item-section style="text-align: start">{{
                    product.name
                  }}</q-item-section>
                  <q-item-section style="text-align: center; border-left: 1px solid #E0E0E0;border-right: 1px solid #E0E0E0;">{{
                    product.quantity
                  }} uds</q-item-section>
                  <q-item-section
                    style="
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    "
                  >
                    <q-btn
                      flat
                      round
                      color="primary"
                      icon="delete"
                      dense
                      style="width: 20%"
                      @click="deleteProduct(index)"
                    />
                  </q-item-section>
                </q-item>
              </div>
            </q-scroll-area>
          </div>
        </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { getRequest, postRequest } from "src/utils/common";
import Swal from "sweetalert2";
import { onMounted, ref } from "vue";

const products = ref({});
const storeOptions = ref([]);
const store = ref(null);
const rows = ref([]);
const emit = defineEmits(["closeOrderForm"]);
const columns = [
  {
    name: "id",
    required: true,
    label: "Product Code",
    align: "center",
    field: "product",
  },
  {
    name: "name",
    required: true,
    label: "Name",
    align: "center",
    field: "product_name",
  },
  {
    name: "stock",
    required: true,
    label: "Stock",
    align: "center",
    field: "stock",
  },
  {
    name: "quantity",
    required: false,
    label: "Quantity",
    align: "center",
    field: "quantity",
  },
  {
    name: "action",
    required: false,
    label: "Action",
    align: "center",
    field: "action",
  },
];

const addProduct = (props) => {
  products.value[props.product] = {
    name: props.product_name,
    quantity: props.quantity,
  };
};

const getStores = async () => {
  // const url = "http://localhost:8000/store/list/";
  const url = "https://backend.adalogix.es/store/list/";
  const stores = await getRequest(url);
  stores.forEach((store) => {
    storeOptions.value.push({ label: store["name"], value: store["id"] });
  });
  if (storeOptions.value.length > 0) {
    store.value = storeOptions.value[0];
    getStoreProducts();
  }
};

const getStoreProducts = async () => {
  try {
    // const url = `http://localhost:8000/store/detail/${store.value.value}/`;
    const url = `https://backend.adalogix.es/store/detail/${store.value.value}/`;
    const response = await getRequest(url);
    rows.value = response.map((row) => ({ ...row, quantity: 0 }));
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
    const products_data = [];
    Object.keys(products.value).forEach((product_id) => {
      const product_info = {
        product: product_id,
        quantity: products.value[product_id].quantity,
      };
      products_data.push(product_info);
    });

    const requestData = {
      store: store.value.value,
      products: products_data,
    };


    // const url = "http://localhost:8000/order/create/";
    const url = "https://backend.adalogix.es/order/create/";
    const response = await postRequest(requestData, url);
    if (response.status === 200) {
      emit("closeOrderForm", false);
      Swal.fire({
        title: "Success",
        text: "Order created successfully",
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

const deleteProduct = (id) => {
  delete products.value[id];
};

onMounted(() => {
  getStores();
});
</script>

<style>
.order-container {
  display: flex;
}

.table-container {
  width: 70%;
  height: 100%;
}

.orders-container {
  border: 1px solid #e0e0e0;
  width: 30%;
  display: flex;
  flex-direction: column;
  height: 95vh;
  border-radius: 4px;
}

.card-container {
  display: flex;
  flex-direction: column;
}
</style>
