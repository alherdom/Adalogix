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
        @click="emit('closeProductDetail')"
        v-close-popup
      />
    </template>
  </q-table>
</template>

<script setup>
import Swal from "sweetalert2";
import { ref, onMounted, watch } from "vue";
import { getRequest } from "src/utils/common";
import { storeColumns } from "src/utils/const";

const props = defineProps({
  productId: String,
  item: Object,
});

const emit = defineEmits(["closeProductDetail"]);
const stores = ref([]);
const loading = ref(false);

const fetchData = async (id) => {
  try {
    loading.value = true;
    const url = `http://localhost:8000/store/product/?product_id=${id}`;
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

const loadProductData = () => {
  const id = props.item?.id || props.productId;
  if (id) {
    fetchData(id);
  }
};

onMounted(loadProductData);
watch(() => props.productId, loadProductData);
watch(() => props.item, loadProductData);
</script>
