import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    userData: {},
    editFormOpen: false,
  }),

  getters: {
    isAdmin(state) {
      return state.userData.group === "admin";
    },
    isCourier(state) {
      return state.userData.group === "courier";
    },
  },

  actions: {
    setUser(response) {
      this.userData = response;
    },
    clearData() {
      this.userData = {};
    },
    handleEditFormDialog() {
      this.editFormOpen = !this.editFormOpen;
    },
  },
});
