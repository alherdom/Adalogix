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

