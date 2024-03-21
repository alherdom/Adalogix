<template>
  <v-container>
    <v-row justify="center" >
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="headline grey lighten-2">
            Sign In
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="login">
              <v-text-field
                v-model="username"
                label="Username"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                required
              ></v-text-field>
              <v-btn
                color="primary"
                type="submit"
                class="mr-4"
                :loading="loading"
              >
                Sign In
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
      password: '',
      loading: false
    };
  },
  methods: {
    login() {
      // Here you can handle login logic, such as sending data to your backend
      // For simplicity, we're just logging the data to the console here
      console.log('Username:', this.username);
      console.log('Password:', this.password);
    }
  }
};
</script>
<style scoped>
.v-container {
  margin-top: 100px;
}
</style>