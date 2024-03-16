<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="headline grey lighten-2">
            Register
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="register">
              <v-text-field
                v-model="username"
                label="Username"
                required
              ></v-text-field>
              <v-text-field
                v-model="fullName"
                label="Full Name"
                required
              ></v-text-field>
              <v-select
                v-model="role"
                :items="roles"
                label="Role"
                required
              ></v-select>
              <v-text-field
                v-model="email"
                label="Email"
                type="email"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                required
              ></v-text-field>
              <v-text-field
                v-model="retypePassword"
                label="Retype Password"
                type="password"
                required
              ></v-text-field>
              <v-btn
                color="primary"
                type="submit"
                class="mr-4"
                :loading="loading"
              >
                Register
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      fullName: '',
      role: '',
      email: '',
      password: '',
      retypePassword: '',
      loading: false,
      roles: ['Admin', 'User', 'Guest'] // Define your list of roles here
    };
  },
  methods: {
    register() {
      // Here you can handle registration logic, such as sending data to your backend
      // For simplicity, we're just logging the data to the console here
      console.log('Username:', this.username);
      console.log('Full Name:', this.fullName);
      console.log('Role:', this.role);
      console.log('Email:', this.email);
      console.log('Password:', this.password);
      console.log('Retype Password:', this.retypePassword);
    }
  }
};
</script>
<style scoped>
.v-container {
  margin-top: 100px;
}
</style>