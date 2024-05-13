<template>
  <div class="logo">
    <h2>Low Stock Products!</h2>
    <LowStock class="prueba" />
  </div>
</template>

<script setup>
import LowStock from "../components/LowStockProducts.vue";
</script>

<style scoped>
.logo {
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 80vh;
}

img {
  width: 250px;
}

.title {
  font-weight: 400;
}
</style>
