<template>
  <q-card class="login-card">
    <q-card-section class="q-pt-none">
      <div class="text-h6 text-center title-form">
        <img class="logo" src="../assets/box3d-three-points.svg" alt="" />
      </div>
      <div class="text-h6 text-center">Adalogix</div>
    </q-card-section>

    <q-card-section>
      <q-form @submit="login" class="form">
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
          type="password"
          required
        />

        <q-btn
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

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      loading: false,
    };
  },
  methods: {
    async login() {
      try {
        this.loading = true; // Activar la animación de carga

        // Enviar datos de inicio de sesión al backend
        const response = await login({
          username: this.username,
          password: this.password,
        });

        // Manejar la respuesta del backend
        if (response.status === 200) {
          // Login exitoso, redirigir al dashboard por ejemplo
          this.$router.push("/dashboard");
        } else {
          // Mostrar mensaje de error al usuario
          this.errorMessage =
            response.message || "An error occurred during login.";
        }
      } catch (error) {
        console.error("Error during login:", error);
        // Manejar el error de la solicitud (por ejemplo, problemas de red)
        this.errorMessage = "An error occurred during login.";
      } finally {
        this.loading = false; // Desactivar la animación de carga, independientemente del resultado
      }
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
  width: 100px;
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
