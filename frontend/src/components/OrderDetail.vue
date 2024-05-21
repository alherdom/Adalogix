<template>
  <q-table
    flat
    :rows="products"
    :columns="columns"
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
        @click="emit('closeOrderDetail')"
        v-close-popup
      />
    </template>
  </q-table>
</template>


<script setup>
import { onMounted, ref, toRaw } from 'vue';


const props = defineProps({
  orderProducts: Array,
  orderStore: String,
});



const emit = defineEmits(["closeOrderDetail"]);
const products = ref([]);
const loading = ref(false);

const columns = [
{
    name: "id",
    required: true,
    label: "Id",
    align: "center",
    field: "id",
    sortable: true,
    },
    {
    name: "name",
    required: true,
    label: "Product Name",
    align: "center",
    field: "name",
    sortable: true,
    },
    {
    name: "quantity",
    required: true,
    label: "Quantity",
    align: "center",
    field: "quantity",
    sortable: true,
  },
  {
    name: "store",
    require: true,
    label: "Store",
    align: "center",
    field: "store",
    sortable: true,
  }
]

onMounted(() => {
    let productInfo;
    props.orderProducts.forEach((product) => {
        productInfo = {
            id: product.product.id,
            name: product.product.name,
            quantity: product.quantity,
            store: props.orderStore
        }
        products.value.push(productInfo)
    })
})


</script>

<style lang="scss" scoped>

</style>