<template>
  <v-app>
    <v-app-bar app class="header">
      <v-toolbar-title>My App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn text to="/login">Sign In</v-btn>
      <v-btn text to="/register">Register</v-btn>
    </v-app-bar>
    <router-view/>
  </v-app>
</template>

<script setup>
import { RouterView } from 'vue-router';
</script>
<style scoped>
</style>
