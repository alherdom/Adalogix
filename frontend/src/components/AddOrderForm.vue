<template>
  <q-card class="item-card">
    <q-card-section>
      <div class="text-h5 text-center item-form-title">
        <div class="text-right">
          <q-btn flat dense icon="close" v-close-popup />
        </div>
        Add Order
      </div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="item-form">
        <q-select :options="storeOptions" v-model="store" filled label="Stores" outlined  @update:model-value="getStoreProducts"/>
        <q-table
          flat
          :rows="rows"
          :columns="columns"
          hide-bottom
        >
          
        </q-table>
        <q-btn push color="primary" label="SEND" type="submit" class="item-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { getRequest } from 'src/utils/common';
import { onMounted, ref } from 'vue';

  const storeOptions = ref([])
  const store = ref(null)
  const rows = ref([])
  const columns = [
    {
        name: "name",
        required: true,
        label: "Name",
        align: "left",   
        field: "name"
    },
    {
        name: "quantity",
        required: true,
        label: "Quantity",
        align: "left",
        field: "quantity"
    }
]

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
  getStores()
})

</script>
