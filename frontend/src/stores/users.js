import { defineStore } from "pinia";

// export const useCounterStore = defineStore("counter", {
//   // state is the same as data in a component
//   state: () => ({
//     counter: 0,
//   }),

//   // getters are like computed properties but for stores
//   getters: {
//     doubleCount(state) {
//       return state.counter * 2;
//     },
//   },

//   // actions are the same as methods in a component
//   actions: {
//     increment() {
//       this.counter++;
//     },
//   },
// });

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
    }
  },
});
