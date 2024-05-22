<template>
  <q-table
    flat
    :rows="stores"
    :columns="storeColumns"
    :loading="loading"
    row-key="id"
    hide-bottom
  >
    <template v-slot:bottom-row>
      <q-btn
        class="close-product-detail-btn"
        flat
        dense
        size="sm"
        icon="close"
        @click="emit('closeProductDetail')"
        v-close-popup
      />
    </template>
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="id" :props="props">
          {{ props.row.id }}
        </q-td>
        <q-td key="name" :props="props">
          {{ props.row.name }}
        </q-td>
        <q-td key="address" :props="props">
          {{ props.row.address }}
        </q-td>
        <q-td key="productId">
            {{ productId.valueOf() }}
        </q-td>
        <q-td key="stock" :props="props">
          <q-input
            v-model="props.row.stock"
            outlined
            dense
            autofocus
            type="number"
            style="width: 80px !important"
          />
        </q-td>
        <q-td key="actions" :props="props">
          <q-btn
            push
            label="save"
            size="sm"
            color="primary"
            @click="updateStore(props.row.id, productId.valueOf(), props.row.stock)"
          />
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script setup>
import Swal from "sweetalert2";
import { ref, onMounted, watch } from "vue";
import { getRequest, patchRequest } from "src/utils/common";
import { storeColumns } from "src/utils/const";


const props = defineProps({
  productId: String,
});

const productId = ref(props.productId);

const emit = defineEmits(["closeProductDetail"]);
const stores = ref([]);
const loading = ref(false);

const fetchData = async () => {
  try {
    loading.value = true;
    // const url = `http://localhost:8000/store/product/?product_id=${id}`;
    const url = `https://backend.adalogix.es/store/product/?product_id=${productId.value}`;
    const response = await getRequest(url);
    stores.value = response.map((store) => ({ ...store }));
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


const updateStore = async (store, productId, stock) => {
  try {
    const requestData = {
      product_id: productId,
      store_id: store,
      new_stock: stock,
    };
    // const url = "http://localhost:8000/product/update/stock/";
    const url = "https://backend.adalogix.es/product/update/stock/";
    const response = await patchRequest(requestData, url);
    if (response.status === 200) {
      emit("closeProductDetail");
      fetchData(productId);
      Swal.fire({
        title: "Success",
        text: "Stock updated successfully",
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
</script>
