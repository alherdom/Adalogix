<template>
  <q-card class="register-card">
    <q-card-section>
      <div class="text-h5 text-center register-form-title">
        <div class="text-right">
          <q-btn flat dense icon="close" v-close-popup />
        </div>
        Register Employee
      </div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="register-form" ref="form">
        <q-input outlined v-model="firstName" label="First Name" type="text" required />
        <q-input outlined v-model="lastName" label="Last Name" type="text" required />
        <q-select class="input-form" outlined v-model="role" label="Role" :options="roleOptions" required
          :rules="[val => !!val || 'Please, user role is required']" lazy-rules />
        <q-input outlined v-model="email" label="Email" type="email" required />
        <q-btn push color="primary" label="SEND" type="submit" class="register-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { postRequest } from "../utils/common";
import { ref } from "vue";

// Variables
const userName = ref("");
const firstName = ref("");
const lastName = ref("");
const roleOptions = ref([{ label: "Admin", value: "SA" }, { label: "Courier", value: "CO" },]);
const role = ref("");
const email = ref("");
const loading = ref(false);
const emit = defineEmits(["closeEditForm"]);

// Functions
const generateUsername = () => {
  const randomDigits = Math.floor(Math.random() * 900) + 100;
  userName.value = `${firstName.value.substring(0, 3)}${lastName.value.substring(0, 3)}${randomDigits}`.toLowerCase();
  return userName.value;
};

const sendData = async () => {
  try {

    generateUsername();
    loading.value = true;
    const requestData = {
      username: userName.value,
      firstName: firstName.value,
      lastName: lastName.value,
      role: role.value.value,
      email: email.value,
    };
    // const url = "http://localhost:8000/user/register/";
    const url = "https://backend.adalogix.es/user/register/";
    const response = await postRequest(requestData, url);
    if (response.status === 200) {
      Swal.fire({
        title: "Success",
        text: "Employee registered successfully",
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
