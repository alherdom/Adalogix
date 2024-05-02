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
        <q-btn color="primary" label="SEND" type="submit" class="register-btn" :loading="loading"/>
        <div class="text-center subtitle-register-form">
          <q-btn flat label="Back to user list" v-close-popup/>
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script setup>
import Swal from "sweetalert2";
import { patchRequest } from "../utils/common";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "src/stores/users";

const emit = defineEmits(['close'])

function closeDialog() {
  emit('close', false)
}
const userStore = useUserStore();
const isPwd = ref(false);
const props = defineProps({
  user: Object,
});
const userData = { ...props.user };
console.log(userData);
const router = useRouter();
const id = ref(userData.id);
const userName = ref(userData.username);
const firstName = ref(userData.first_name);
const lastName = ref(userData.last_name);
const role = ref({ label: userData.role, value: userData.role });
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
      id: id.value,
      username: userName.value,
      first_name: firstName.value,
      last_name: lastName.value,
      role: "SA",
      email: email.value,
    };
    console.log(requestData);
    const url = `http://localhost:8000/user/update/${id.value}/`;
    const response = await patchRequest(requestData, url);
    console.log(response);
    if (response.status === 200) {
      closeDialog()
      userStore.handleEditFormDialog();
      Swal.fire({
        title: "Success",
        text: "User edited successfully",
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
      });
      // emitir evento para cerrar dialog en el padre
      router.push("/users");
      
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
