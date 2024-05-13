<template>
  <div>
    <q-table
      :rows="stores"
      :columns="columns"
      row-key="id"
      :pagination="true"
      :rows-per-page-options="[5, 10, 15]"
    >
      <template v-slot:body-cell-quantity="props">
        <q-td :props="props">
          {{ props.row.quantity }}
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

const productId = props.productId;
const stores = ref([]);
const columns = [
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
  { name: 'quantity', label: 'Quantity', align: 'left', field: 'quantity' },
  { name: 'address', label: 'Address', align: 'left', field: 'address' }
];

// http://localhost:8000/products/1/stores/
const fetchStores = async () => {
  try {
    const response = await fetch(`/api/products/${productId}/stores/`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    stores.value = data;
  } catch (error) {
    console.error('Error fetching stores:', error);
  }
};

onMounted(fetchStores);
watch(() => props.productId, fetchStores);
</script>
