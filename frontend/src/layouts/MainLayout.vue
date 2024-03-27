<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>
          <a href="" class="title">Adalogix</a>
        </q-toolbar-title>
        <q-chip>
          <q-avatar>
            <img src="../assets/default-avatar.svg">
          </q-avatar>
          {{ userName }}
        </q-chip>
        <!-- <div class="q-pa-md">
          <q-btn-dropdown class="showUser" size="md" color="white" :label="userName">
            <div class="row no-wrap q-pa-md user-row">
              <div class="column">
                <q-avatar size="100px">
                  <img src="../assets/default-avatar.svg">
                </q-avatar>
                <div class="text-subtitle1 q-mt-md q-mb-xs">{{ userName }}</div>
                <q-btn color="primary" label="Logout" push size="md" v-close-popup />
              </div>
            </div>
          </q-btn-dropdown>
        </div> -->
      </q-toolbar>
    </q-header>
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <EssentialLink v-for="link in filteredLinks" :key="link.title" v-bind="link" @click="hadleClick(link)" />
      </q-list>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, computed } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import Swal from 'sweetalert2';

defineOptions({
  name: 'MainLayout'
})
const userName = sessionStorage.getItem('name')

const linksList = [
  {
    title: 'HOME',
    icon: 'home',
    link: '#/main',
    roles: ['admin', 'courier']
  },
  {
    title: 'INVENTORY',
    icon: 'inventory',
    link: '#/main/inventory',
    roles: ['admin']
  },
  {
    title: 'ROUTE',
    icon: 'location_on',
    link: '#/main/route',
    roles: ['admin']
  },
  {
    title: 'CHAT',
    icon: 'chat',
    link: '#/main/chat',
    roles: ['admin', 'courier']
  },
  {
    title: 'USERS',
    icon: 'people_alt',
    link: '#/main/users',
    roles: ['admin']
  },
  {
    title: 'REGISTER',
    icon: 'app_registration',
    link: '#/main/register',
    roles: ['admin']
  },
  {
    title: 'LOGOUT',
    icon: 'exit_to_app',
    roles: ['admin', 'courier']
  }
]

const leftDrawerOpen = ref(false)
const userRole = sessionStorage.getItem('role')

const filteredLinks = computed(() => {
  return linksList.filter(link => link.roles.includes(userRole));
})

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

function hadleClick(link) {
  if (link.title === 'LOGOUT') {
    sessionStorage.removeItem('role')
    Swal.fire({
      title: 'See you soon 👋🏻',
      text: 'You have been logged out',
      icon: 'success',
      showConfirmButton: false,
      timer: 2000,
    });
  }
}

</script>
<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

a::after {
  background-color: red;
}

.title {
  font-size: 1.5rem;
  font-weight: 400;
}

.q-chip {
  background-color: white;
  font-weight: 400;
}

.q-list {
  padding: 50px 0px 0px 0px;
  font-weight: 400;
}

.q-list a:first-child {
  border-top: 1px solid #f0f0f0;
}

.q-list a {
  border-bottom: 1px solid #f0f0f0;
  padding-top: 12px;
}

.showUser {
  color: black !important;
  border-radius: 8px;
  border-bottom: 3px solid rgb(255, 255, 255, 0.5);
  text-transform: capitalize;
  height: 10px !important;
}

.user-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
