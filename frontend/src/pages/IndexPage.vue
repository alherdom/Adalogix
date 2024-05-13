<template>
  <div class="logo">
    <h2>Low Stock Products!</h2>
    <LowStock />
  </div>
  <div class="cards">
    <AvailableEmployees />
  </div>
</template>

<script setup>
import LowStock from "../components/LowStockProducts.vue";
import AvailableEmployees from "../components/AvailableEmployees.vue";
</script>

<style scoped>
.logo {
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 80vh;
}
.cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

img {
  width: 250px;
}

.title {
  font-weight: 400;
}
</style>
