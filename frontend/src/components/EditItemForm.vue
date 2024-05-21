<template>
  <q-card class="item-card">
    <q-card-section>
      <div class="text-h5 text-center item-form-title">
        <div class="text-right">
          <q-btn flat dense icon="close" v-close-popup />
        </div>
        Edit Product
      </div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="item-form">
        <q-input outlined v-model="name" label="Name" type="text" />
        <q-input outlined v-model="description" label="Description" type="text" />
        <q-input outlined v-model="category" label="Category" type="text" />
        <q-input outlined v-model="price" label="Price" type="text" />
        <q-input outlined v-model="weight" label="Weight" type="text" />
        <q-input outlined v-model="volume" label="Volume" type="text" />
        <q-btn push color="primary" label="SAVE" type="submit" class="item-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { patchRequest } from "../utils/common";
import { ref } from "vue";

const props = defineProps({
  item: Object,
});
const itemData = { ...props.item };
const id = ref(itemData.id);
const name = ref(itemData.name);
const description = ref(itemData.description);
const category = ref(itemData.category);
const price = ref(itemData.price);
const weight = ref(itemData.weight);
const volume = ref(itemData.volume);
const loading = ref(false);
const emit = defineEmits(['closeEditForm'])

const sendData = async () => {
  try {
    loading.value = true;
    const requestData = {
      id: id.value,
      name: name.value,
      description: description.value,
      category: category.value,
      price: price.value,
      weight: weight.value,
      volume: volume.value,
    };
    // const url = `http://localhost:8000/product/update/${id.value}/`;
    const url = `https://backend.adalogix.es/product/update/${id.value}/`;
    const response = await patchRequest(requestData, url);
    if (response.status === 200) {
      Swal.fire({
        title: "Success",
        text: "Product edited successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
      emit("closeEditForm", false);
    } else {
      console.log(response.status);
      alert("Error");
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

</script>
