<template>
  <q-table
    class="product-detail-table"
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
        v-close-popup
      />
    </template>
  </q-table>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getRequest } from "src/utils/common";
import { storeColumns } from "src/utils/const";

const props = defineProps({
  item: Object,
});

const itemData = { ...props.item };
const productId = ref(itemData.id);
const stores = ref([]);
const loading = ref(false);
const emit = defineEmits(["closeProductDetail"]);

const fetchData = async () => {
  try {
    loading.value = true;
    // const url = `https://backend.adalogix.es/store/product/?product_id=${productId.value}`;
    const url = `http://localhost:8000/store/product/?product_id=${productId.value}`;
    const response = await getRequest(url);
    stores.value = response.map((store) => ({ ...store }));
    console.log(stores.value);
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
</script>
