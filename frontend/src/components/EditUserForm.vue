<template>
  <q-card class="register-card">
    <q-card-section>
      <div class="text-h5 text-center register-form-title">Edit user</div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="register-form">
        <q-input outlined v-model="user.userName" label="Username" type="text" required />
        <q-input outlined v-model="user.firstName" label="First Name" type="text" required />
        <q-input outlined v-model="user.lastName" label="Last Name" type="text" required />
        <q-select class="input-form" outlined v-model="user.role" label="Role" :options="roleOptions" required />
        <q-input outlined v-model="user.email" label="Email" type="text" required />
        <q-input outlined v-model="password" label="Password" type="password" required />
        <q-input outlined v-model="confirmPassword" label="Confirm Password" type="password" required />
        <q-btn color="primary" label="SEND" type="submit" class="register-btn" :loading="loading" />
        <div class="text-center subtitle-register-form">
          <q-btn flat label="Back to user list" v-close-popup />
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { postRequest } from "../utils/common";
import { ref } from "vue";
import { useRouter } from "vue-router";

const { user } = props;
console.log(props.user.value);
const router = useRouter();
const userName = ref("");
const firstName = ref("");
const lastName = ref("");
const role = ref("");
const roleOptions = ref([
  { label: "Admin", value: "SA" },
  { label: "Courier", value: "CO" },
]);
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const loading = ref(false);

const sendData = async () => {
  try {
    loading.value = true;
    const requestData = {
      username: userName.value,
      firstName: firstName.value,
      lastName: lastName.value,
      role: role.value.value,
      email: email.value,
      password: password.value,
    };
    console.log(requestData);
    const url = "http://localhost:8000/user/register/";
    const response = await postRequest(requestData, url);
    if (response.status === 200) {
      Swal.fire({
        title: "Success",
        text: "User registered successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
      router.push("/users");
    } else {
      alert("Error");
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

</script>
