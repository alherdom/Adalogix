<template>
  <q-card class="register-card">
  <q-card-section class="register-card">
    <div class="text-h5 text-center">Edit</div>
  </q-card-section>
  <q-card-section>
    <q-form @submit="sendData" class="register-form">
      <q-input
        name="name"
        autocomplete="name"
        v-model="name"
        color="primary"
        label="Name"
        filled
        clearable
      />
      <q-input
        name="description"
        autocomplete="description"
        v-model="description"
        color="primary"
        label="Description"
        filled
        clearable
      />
      <q-input
        name="category"
        autocomplete="category"
        v-model="category"
        color="primary"
        label="Category"
        filled
        clearable
      />
      <q-input
        name="price"
        autocomplete="price"
        v-model="price"
        color="primary"
        label="Category"
        filled
        clearable
      />
      <q-input
        name="weight"
        autocomplete="weight"
        v-model="weight"
        color="primary"
        label="Weight"
        filled
        clearable
      />
      <q-input
        name="volume"
        autocomplete="volume"
        v-model="volume"
        color="primary"
        label="Volume"
        filled
        clearable
      />
      <q-btn
          color="primary"
          label="Edit"
          type="submit"
          class="register-btn"
          :loading="loading"
        />
    </q-form>
  </q-card-section>
</q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { patchRequest } from "../utils/common";
import { ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps({
  product: Object,
});



const emit = defineEmits(['close'])

function closeDialog() {
  emit('close', false)
}

const productData = {...props.product}
const router = useRouter();
const id = productData.id;
const name = ref(productData.name);
const description = ref(productData.description);
const category = ref(productData.category);
const price = ref(productData.price);
const weight = ref(productData.weight)
const volume = ref(productData.volume)
const loading = ref(false);

const sendData = async () => {
    try {
        loading.value = true;
        const requestData =  {
            id: id,
            name: name.value,
            description: description.value,
            category: category.value,
            price: price.value,
            weight: weight.value,
            volume: volume.value,
        }
        console.log(requestData)
        const url = `http://localhost:8000/product/update/${id}/`;
        const response = await patchRequest(requestData, url);
        console.log(response)
        if (response.status === 200) {
          closeDialog()
          Swal.fire({
            title: "Success",
            text: "Product edited successfully",
            icon: "success",
            showConfirmButton: false,
            timer: 1500
          })
          router.push("/users")
        } else {
          alert("Error")
        }
        } catch (error) {
          console.error(error);
        } finally {
          loading.value = false;
          router.push('/inventory')
        }

    }
</script>
