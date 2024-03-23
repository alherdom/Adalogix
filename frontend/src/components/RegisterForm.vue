<template>
  <q-card class="login-card">
    <q-card-section>
      <q-form @submit="register" class="form">
        <q-input class="input-form" outlined v-model="username" label="Username" type="text" required />
        <q-input class="input-form" outlined v-model="firstname" label="Firstname" type="text" required />
        <q-input class="input-form" outlined v-model="lastname" label="Lastname" type="text" required />
        <q-select class="input-form" v-model="role" outlined label="Role" :options="roleOptions" required />
        <q-input class="input-form" outlined v-model="email" label="Email" type="text" required />
        <q-input class="input-form" outlined v-model="password" label="Password" type="password" required />
        <!-- <q-input class="input-form" outlined v-model="password2" label="Retype password" type="password"
          required /> -->
        <q-btn color="primary" label="Register" type="submit" class="login-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import { request } from '../utils/common';
export default {
  data() {
    return {
      username: '',
      firstname: '',
      lastname: '',
      role: '',
      roleOptions: [
        { label: 'Admin', value: 'admin' },
        { label: 'Courier', value: 'courier' },
        { label: 'Guest', value: 'guest' }
      ],
      email: '',
      password: '',
      loading: false,
    };
  },
  methods: {
    register() {
      request({
        username: this.username,
        firstname: this.firstname,
        lastname: this.lastname,
        role: this.role.value,
        email: this.email,
        password: this.password,
      }, 'http://127.0.0.1:8000/user/register/', 'POST');
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
