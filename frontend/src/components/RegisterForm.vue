<template>
  <q-card class="login-card">
    <q-card-section>
      <q-form @submit="sendData" class="form">
        <q-input class="input-form" outlined v-model="username" label="Username" type="text" required />
        <q-input class="input-form" outlined v-model="firstname" label="First Name" type="text" required />
        <q-input class="input-form" outlined v-model="lastname" label="Last Name" type="text" required />
        <q-select class="input-form" v-model="role" outlined label="Role" :options="roleOptions" required />
        <q-input class="input-form" outlined v-model="email" label="Email" type="text" required />
        <q-input class="input-form" outlined v-model="password" label="Password" type="password" required />
        <q-input class="input-form" outlined v-model="confirmPassword" label="Confirm Password" type="password"
          required />
        <q-btn color="primary" label="Register" type="submit" class="login-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import Swal from 'sweetalert2';
import { Dialog } from 'quasar';
import { postRequest } from '../utils/common';

export default {
  data() {
    return {
      username: '',
      firstname: '',
      lastname: '',
      role: '',
      roleOptions: [
        { label: 'Admin', value: 'SA' },
        { label: 'Courier', value: 'CO' },
      ],
      email: '',
      password: '',
      confirmPassword: '',
      loading: false,
    };
  },
  methods: {
    async sendData() {
      try {
        const data = {
          username: this.username,
          firstname: this.firstname,
          lastname: this.lastname,
          role: this.role.value,
          email: this.email,
          password: this.password,
        };
        const url = 'http://localhost:8000/user/register/';
        const response = await postRequest(data, url);
        if (response.status === 200) {
          Swal.fire({
            title: 'Success',
            text: 'User registered successfully',
            icon: 'success',
            showConfirmButton: false,
            timer: 2000,
          });
          this.$router.push('/main');
        } else {
          console.error('Error sending data:', response.statusText);
        }
      } catch (error) {
        console.error('Error sending data:', error);
      }
    }
  }

}
</script>

<style scoped>
.login-card {
  width: 500px;
  margin: 0 auto;
  margin-top: 50px;
}

.form {
  display: flex;
  flex-direction: column;
}

.input-form:first-child {
  margin-top: 20px;
}

.input-form {
  padding: 0px 20px 20px 20px;
}

.login-btn {
  height: 50px;
  width: 91%;
  padding: 0px 20px 0px 20px;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
