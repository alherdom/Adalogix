// import { route } from "quasar/wrappers";
// import { useUserStore } from "../stores/users";
// import {
//   createRouter,
//   createMemoryHistory,
//   createWebHistory,
//   createWebHashHistory,
// } from "vue-router";
// import routes from "./routes";

// /*
//  * If not building with SSR mode, you can
//  * directly export the Router instantiation;
//  *
//  * The function below can be async too; either use
//  * async/await or return a Promise which resolves
//  * with the Router instance.
//  */

// export default route(function (/* { store, ssrContext } */) {
//   const createHistory = process.env.SERVER
//     ? createMemoryHistory
//     : process.env.VUE_ROUTER_MODE === "history"
//     ? createWebHistory
//     : createWebHashHistory;

//   const Router = createRouter({
//     scrollBehavior: () => ({ left: 0, top: 0 }),
//     routes,

//     // Leave this as is and make changes in quasar.conf.js instead!
//     // quasar.conf.js -> build -> vueRouterMode
//     // quasar.conf.js -> build -> publicPath
//     history: createHistory(process.env.VUE_ROUTER_BASE),
//   });

//   Router.beforeEach((to, from, next) => {
//     const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
//     const userRole = localStorage.getItem("userGroup");
//     // const userStore = useUserStore();
//     // const userRole = userStore.userData.group;
//     if (requiresAuth) {
//       if (!userRole) {
//         next({ path: "/login" });
//       } else {
//         const allowedRoles = to.meta.roles;
//         if (allowedRoles.includes(userRole.toLowerCase())) {
//           next();
//         } else {
//           next({ path: "/unauthorized" });
//         }
//       }
//     } else {
//       next();
//     }
//   });
//   return Router;
// });

import { route } from "quasar/wrappers";
import { createRouter, createMemoryHistory, createWebHistory } from "vue-router";
import routes from "./routes";

export default route(function () {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : createWebHistory;

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Configuración de history
    history: createHistory(process.env.VUE_ROUTER_BASE),
  });

  Router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
    const userRole = localStorage.getItem("userGroup");
    if (requiresAuth) {
      if (!userRole) {
        next({ path: "/login" });
      } else {
        const allowedRoles = to.meta.roles;
        if (allowedRoles.includes(userRole.toLowerCase())) {
          next();
        } else {
          next({ path: "/unauthorized" });
        }
      }
    } else {
      next();
    }
  });

  return Router;
});

