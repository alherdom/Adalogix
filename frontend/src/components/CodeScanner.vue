<template>
  <div>
    <qrcode-stream @decode="onDecode" @init="onInit"></qrcode-stream>
    <table v-if="productData">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Stock</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ productData.name }}</td>
          <td>{{ productData.description }}</td>
          <td>{{ productData.price }}</td>
          <td>{{ productData.stock }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
import { QrcodeStream } from 'vue-qrcode-reader';

const emits = defineEmits(['decoded']);
const productData = ref(null);

const onDecode = async (content) => {
  emits('decoded', content);
  await fetchProductData(content);
};

const fetchProductData = async (qrCodeContent) => {
  try {
    const response = await fetch(`/api/products/${qrCodeContent}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    productData.value = data;
  } catch (error) {
    console.error('Error fetching product data:', error);
  }
};

const onInit = (promise) => {
  promise.catch(error => {
    console.error(error);
    // Manejo de errores de inicialización
  });
};
</script>

