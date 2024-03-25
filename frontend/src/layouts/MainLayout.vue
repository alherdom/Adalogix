<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <a href="">Adalogix</a>
        </q-toolbar-title>

        <div>v0.0.1</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>
        </q-item-label>

        <EssentialLink v-for="link in linksList" :key="link.title" v-bind="link" target="" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

defineOptions({
  name: 'MainLayout'
})

const linksList = [
  {
    title: 'HOME',
    icon: 'home',
    link: '#/main'
    // caption: '',
  },
  {
    title: 'INVENTORY',
    icon: 'category',
    link: '#/main/inventory' // Agrega la URL correspondiente
  },
  {
    title: 'ROUTE',
    icon: 'location_on',
    link: '#/main/route' // Agrega la URL correspondiente
  },
  {
    title: 'CHAT',
    icon: 'chat',
    link: '#/main/chat' // Agrega la URL correspondiente
  },
  {
    title: 'REGISTER',
    icon: 'people_alt',
    link: '#/main/register' // Corregida la URL para ir a la página de registro
  },
  {
    title: 'LOGOUT',
    icon: 'exit_to_app',
    link: '#/main/logout'
  },
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

a:hover {
  color: #000000;
}
</style>
