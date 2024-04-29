<template>
  <q-card class="register-card">
    <q-card-section>
      <div class="text-h5 text-center register-form-title">Edit user</div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="register-form">
        <q-input outlined v-model="userName" label="Username" type="text" required />
        <q-input outlined v-model="firstName" label="First Name" type="text" required />
        <q-input outlined v-model="lastName" label="Last Name" type="text" required />
        <q-select class="input-form" outlined v-model="role" label="Role" :options="roleOptions" required />
        <q-input outlined v-model="email" label="Email" type="text" required />
        <q-input outlined v-model="password" label="New Password" :type="isPwd ? 'password' : 'text'">
          <template v-slot:append>
            <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
          </template>
        </q-input>
        <q-input outlined v-model="confirmPassword" label="Confirm Password" :type="isPwd ? 'password' : 'text'">
          <template v-slot:append>
            <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
          </template>
        </q-input>
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

const isPwd = ref(false);
const props = defineProps({
  user: Object,
});

const router = useRouter();
const userName = ref(props.user.username);
const firstName = ref(props.user.first_name);
const lastName = ref(props.user.last_name);
const role = ref({ label: props.user.role, value: props.user.role });
const roleOptions = ref([
  { label: "Admin", value: "SA" },
  { label: "Courier", value: "CO" },
]);
const email = ref(props.user.email);
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
