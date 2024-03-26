<template>
  <q-card class="login-card">
    <q-card-section class="q-pt-none">
      <div class="text-h6 text-center title-form">
        <img class="logo" src="../assets/box3d-three-points.svg" alt="" />
      </div>
      <div class="text-h6 text-center">Adalogix</div>
    </q-card-section>

    <q-card-section>
      <q-form @submit="sendData" class="form">
        <q-input class="input-form" outlined v-model="username" label="Username" type="text" required />
        <q-input class="input-form" outlined v-model="password" label="Password" type="password" required />

        <q-btn color="primary" label="Log in" type="submit" class="login-btn" :loading="loading" />

        <div class="text-center subtitle-form">
          <q-btn flat label="Forgot your password?" @click="forgotPassword" />
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import Swal from 'sweetalert2';
import { postRequest } from '../utils/common';
export default {
  data() {
    return {
      username: "",
      password: "",
      loading: false,
    };
  },
  methods: {
    async sendData() {
      try {
        const data = {
          username: this.username,
          password: this.password,
        };
        const url = 'http://localhost:8000/user/login/';
        const response = await postRequest(data, url);
        if (response.status === 200) {
          Swal.fire({
            title: 'Success',
            text: 'You are successfully logged in',
            icon: 'success',
            showConfirmButton: false,
            timer: 2000,
          });
          sessionStorage.setItem('name', response.name);
          sessionStorage.setItem('role', response.group);
          this.$router.push('/main');
        }
      } catch (error) {
        Swal.fire({
          title: 'Error',
          text: 'Invalid username or password',
          icon: 'error',
          showConfirmButton: false,
          timer: 2000,
        });
        console.error('Error sending data:', error);
      }
    },
    forgotPassword() {
      Swal.fire({
        title: 'Forgot Password',
        text: 'Please contact your administrator',
        icon: 'info',
        showConfirmButton: false,
        timer: 2000,
      });
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

.logo {
  width: 120px;
}

.login-card {
  width: 500px;
  margin: 0 auto;
  margin-top: 50px;
}

.title-form {
  padding-top: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

.subtitle-form {
  margin-top: 20px;
  margin-bottom: 20px;
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
}
</style>
