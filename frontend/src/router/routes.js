const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
  path: "/login",
  name: "login",
  component: () => import("pages/LoginPage.vue"),},
  {
    path: "/main",
    name: "main",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "home",
        component: () => import("pages/IndexPage.vue"),
      },
      {
        path: "inventory",
        name: "inventory",
        component: () => import("pages/InventoryPage.vue"),
      },
      {
        path: "register",
        name: "register",
        component: () => import("pages/RegisterPage.vue"),
      },
      { path: "route", component: () => import("pages/IndexPage.vue") },
      { path: "chat", component: () => import("pages/IndexPage.vue") },
      { path: "logout", component: () => import("pages/IndexPage.vue") },
    ],
  },
  // Ruta para manejar cualquier otra ruta no definida
  {
    path: "/:catchAll(.*)",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
