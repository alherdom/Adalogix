<template>
  <q-card class="login-card">
    <q-card-section>
      <q-form @submit="sendData" class="form">
        <q-input class="input-form" outlined v-model="username" label="Username" type="text" required />
        <q-input class="input-form" outlined v-model="firstname" label="Firstname" type="text" required />
        <q-input class="input-form" outlined v-model="lastname" label="Lastname" type="text" required />
        <q-select class="input-form" v-model="role" outlined label="Role" :options="roleOptions" required />
        <q-input class="input-form" outlined v-model="email" label="Email" type="text" required />
        <q-input class="input-form" outlined v-model="password" label="Password" type="password" required />
        <q-input class="input-form" outlined v-model="retypePassword" label="Retype password" type="password"
          required />
        <q-btn color="primary" label="Register" type="submit" class="login-btn" :loading="loading" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import { postRequest } from '../utils/common';
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
      retypePassword: '',
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
        await postRequest(data, url);
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
