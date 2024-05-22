<template>
  <q-layout view="hHh Lpr lff" container style="height: 100vh" class="shadow-2">
    <q-header elevated class="myHeader">
      <q-toolbar>
        <q-btn flat @click="drawer = !drawer" dense icon="menu" />
        <q-toolbar-title class="title">{{ capitalizePath }}</q-toolbar-title>
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
      elevated
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
            class="link"
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
            <q-item-section class="link"> Logout </q-item-section>
          </q-item>
          <q-separator />
          <!-- i18n -->
          <!-- <q-item class="absolute-bottom" clickable @click="changeLanguage" v-ripple>
            <q-item-section avatar>
              <q-icon name="language" />
            </q-item-section>
            <q-item-section class="link">Language</q-item-section>
          </q-item> -->
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
import { links } from "../utils/const";
import { useUserStore } from "../stores/users";
import { useRouter } from "vue-router";

const drawer = ref(true);
const miniState = ref(true);
const userStore = useUserStore();
const router = useRouter();
const userName = localStorage.getItem("userName");
const path = computed(() => {
  return router.currentRoute.value.path.slice(1);
});
const capitalizePath = computed(() => {
  return path.value.charAt(0).toUpperCase() + path.value.slice(1);
});

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
    title: "Logout",
    text: "Are you sure you want to leave?",
    icon: "question",
    showCancelButton: true,
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
