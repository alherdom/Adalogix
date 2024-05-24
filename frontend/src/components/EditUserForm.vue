<template>
  <q-card class="edit-card">
    <q-card-section>
      <div class="text-h5 text-center edit-form-title">
        <div class="text-right">
          <q-btn flat dense icon="close" v-close-popup />
        </div>
        Edit Employee
      </div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="sendData" class="edit-form">
        <q-input
          outlined
          v-model="userName"
          label="Username"
          type="text"
          required
        />
        <q-input
          outlined
          v-model="firstName"
          label="First Name"
          type="text"
          required
        />
        <q-input
          outlined
          v-model="lastName"
          label="Last Name"
          type="text"
          required
        />
        <q-select
          class="input-form"
          outlined
          v-model="role"
          label="Role"
          :options="roleOptions"
          required
        />
        <q-input outlined v-model="email" label="Email" type="text" required />
        <q-btn
          push
          color="primary"
          label="RESET PASSWORD"
          class="edit-btn reset-password-btn"
          :loading="loading"
          @click="resetPassword"
        />
        <q-btn
          push
          color="primary"
          label="SAVE"
          type="submit"
          class="edit-btn"
          :loading="loading"
        />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { patchRequest, postRequest } from "../utils/common";
import { ref } from "vue";

const props = defineProps({
  user: Object,
});
const userData = { ...props.user };
const id = ref(userData.id);
const userName = ref(userData.username);
const firstName = ref(userData.first_name);
const lastName = ref(userData.last_name);
const roleOptions = ref([
  { label: "Admin", value: "SA" },
  { label: "Courier", value: "CO" },
]);
const role = ref(userData.role);
const email = ref(userData.email);
const loading = ref(false);
const emit = defineEmits(["closeEditForm"]);

const sendData = async () => {
  try {
    loading.value = true;
    const requestData = {
      id: id.value,
      username: userName.value,
      first_name: firstName.value,
      last_name: lastName.value,
      role: role.value.value,
      email: email.value,
    };
    // const url = `http://localhost:8000/user/update/${id.value}/`;
    const url = `https://backend.adalogix.es/user/update/${id.value}/`;
    const response = await patchRequest(requestData, url);
    if (response.status === 200) {
      emit("closeEditForm", false);
      Swal.fire({
        title: "Success",
        text: "Employee edited successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
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

const resetPassword = async () => {
  try {
    loading.value = true;
    const requestData = {
      employeeId: id.value,
    };
    // const url = `http://localhost:8000/user/reset/password/`;
    const url = `https://backend.adalogix.es/user/reset/password/`;
    const response = await postRequest(requestData, url);
    if (response.status === 200) {
      emit("closeEditForm", false);
      Swal.fire({
        title: "Success",
        text: "Password reset successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,

      });
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
