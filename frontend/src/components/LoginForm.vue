<template>
  <q-card class="login-card">
    <q-card-section class="q-pt-none">
      <div class="text-h6 text-center title-form">
        <img class="login-logo" src="../assets/box3d-three-points.svg" alt="" />
      </div>
      <div class="text-h6 text-center">Adalogix</div>
    </q-card-section>

    <q-card-section>
      <q-form @submit="sendData" class="login-form">
        <q-input
          class="input-form"
          outlined
          v-model="username"
          label="Username"
          type="text"
          required
        />
        <q-input
          class="input-form"
          outlined
          v-model="password"
          label="Password"
          :type="isPwd ? 'password' : 'text'"
          required
        >
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>

        <q-btn
          push
          color="primary"
          label="Log in"
          type="submit"
          class="login-btn"
          :loading="loading"
        />

        <div class="text-center subtitle-form">
          <q-btn flat label="Forgot your password?" @click="forgotPassword" />
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { ref } from "vue";
import Swal from "sweetalert2";
import { postLoginRequest } from "../utils/common";
import { useUserStore } from "../stores/users";
import { useRouter } from "vue-router";

// Configuration of the component properties
// The setup function is a new way to define the component properties
// It is a composition API that allows you to define the component properties in a more organized way
const isPwd = ref(true);
const router = useRouter();
const userStore = useUserStore();
const username = ref("");
const password = ref("");
const loading = ref(false);

// Function to handle the success login, show message and redirect
// Also sets the user data in the user store
// The user store is a global store that can be accessed from any component
const handleSuccessLogin = (response) => {
  Swal.fire({
    title: `Welcome ${response.name}! 👋🏻`,
    text: "You are successfully logged in",
    icon: "success",
    showConfirmButton: false,
    timer: 2000,
  });

  localStorage.setItem("userId", response.id);
  localStorage.setItem("userName", response.name);
  localStorage.setItem("userGroup", response.group);
  localStorage.setItem("userToken", response.token);
  userStore.setUser(response);
  router.push(response.group === "admin" ? "/orders" : "/router");
};

// Function to handle the failed login
// It shows an error message if the login fails
const handleFailedLogin = () => {
  Swal.fire({
    title: "Error",
    text: "Invalid username or password",
    icon: "error",
    showConfirmButton: false,
    timer: 2000,
  });
};

// Function to send the login data to the server
// It sends a POST request to the server with the username and password
// If the login is successful, it calls the handleSuccessLogin function
// If the login fails, it calls the handleFailedLogin function
const sendData = async () => {
  try {
    loading.value = true;
    const requestData = {
      username: username.value,
      password: password.value,
    };
    // const url = "http://localhost:8000/user/login/";
    const url = "https://backend.adalogix.es/user/login/";
    const response = await postLoginRequest(requestData, url);
    if (response.status === 200) {
      handleSuccessLogin(response);
    } else {
      handleFailedLogin();
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

// Function to handle the forgot password action
// It shows an info message to contact the administrator
const forgotPassword = () => {
  Swal.fire({
    title: "Forgot Password",
    text: "Please contact your administrator",
    icon: "info",
    showConfirmButton: false,
    timer: 2000,
  });
};
</script>
