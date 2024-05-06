<template>
  <q-layout view="hHh Lpr lff" container style="height: 100vh" class="shadow-2">
    <q-header class="myHeader">
      <q-toolbar>
        <q-btn flat @click="drawer = !drawer" dense icon="menu" />
        <q-toolbar-title class="title"
          ><a href="/">Adalogix</a></q-toolbar-title
        >
        <q-space />
        <q-btn-dropdown
          class="userName"
          flat
          dense
          :label="userName"
          icon="person"
          no-caps
        >
          <div class="row no-wrap q-pa-md">
            <div class="myDropdown">
              <q-btn
                class="btn-profile"
                color="primary"
                text-color="black"
                label="Profile"
                push
                size="sm"
                @click="showProfile"
              />
              <q-btn
                class="btn-logout"
                color="primary"
                text-color="black"
                label="Logout"
                push
                size="sm"
                @click="logout"
              />
            </div>
          </div>
        </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawer"
      show-if-above
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      mini-to-overlay
      :width="200"
      :breakpoint="500"
      bordered
      :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
    >
      <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: 0 }">
        <q-list padding>
          <router-link
            v-for="(link, index) in filteredLinks"
            :key="link.path"
            :to="link.path"
          >
            <q-item :active="isActive(link.path)" clickable v-ripple>
              <q-item-section avatar>
                <q-icon :name="link.icon" />
              </q-item-section>
              <q-item-section>
                {{ link.label }}
              </q-item-section>
            </q-item>
            <q-separator
              v-if="(index + 1) % 5 === 0 && index !== filteredLinks.length - 1"
            />
          </router-link>
          <q-item clickable @click="logout" v-ripple>
            <q-item-section avatar>
              <q-icon name="exit_to_app" />
            </q-item-section>
            <q-item-section> LOGOUT </q-item-section>
          </q-item>
          <q-separator />
        </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, computed } from "vue";
import Swal from "sweetalert2";
import { useUserStore } from "../stores/users";
import { useRouter } from "vue-router";

const drawer = ref(false);
const miniState = ref(true);
const userStore = useUserStore();
const router = useRouter();
const userName = localStorage.getItem("userName");

const links = [
  {
    path: "/",
    label: "HOME",
    icon: "cottage",
    roles: ["admin", "courier"],
  },
  {
    path: "/inventory",
    label: "INVENTORY",
    icon: "inventory",
    roles: ["admin"],
  },
  { path: "/router", label: "ROUTER", icon: "fmd_good", roles: ["admin"] },
  {
    path: "/chat",
    label: "CHAT",
    icon: "comment",
    roles: ["admin", "courier"],
  },
  { path: "/users", label: "USERS", icon: "people_alt", roles: ["admin"] },
  {
    path: "/settings",
    label: "SETTINGS",
    icon: "settings",
    roles: ["admin", "courier"],
  },
];

const filteredLinks = computed(() => {
  const userRole = localStorage.getItem("userGroup");
  if (!userRole) return [];
  return links.filter(
    (link) => Array.isArray(link.roles) && link.roles.includes(userRole)
  );
});

const isActive = (route) => {
  return router.currentRoute.value.path === route;
};

const logout = () => {
  Swal.fire({
    title: "Are you sure you want to leave?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: `Bye ${userName}! 👋🏻`,
        text: "You have been logged out successfully",
        icon: "success",
      });
      router.push("/login");
      userStore.clearData();
      localStorage.clear();
    }
  });
};

const showProfile = () => {
  Swal.fire({
    title: "Showing profile...",
    text: "This feature is not implemented yet",
    icon: "info",
  });
};
</script>
