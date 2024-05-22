const routes = [
  {
    path: "/login",
    name: "login",
    component: () => import("pages/LoginPage.vue"),
  },
  {
    path: "/",
    name: "main",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true, roles: ["admin", "courier"] },
    children: [
      {
        path: "orders",
        name: "orders",
        component: () => import("pages/OrderPage.vue"),
        meta: { requiresAuth: true, roles: ["admin"]}
      },
      {
        path: "inventories",
        name: "inventories",
        component: () => import("pages/InventoryPage.vue"),
        meta: { requiresAuth: true, roles: ["admin"] },
        children: [],
      },
      {
        path: "employees",
        name: "employees",
        component: () => import("pages/UsersPage.vue"),
        meta: { requiresAuth: true, roles: ["admin"] },
      },
      {
        path: "register",
        name: "register",
        component: () => import("pages/RegisterPage.vue"),
        meta: { requiresAuth: true, roles: ["admin"] },
      },
      {
        path: "router",
        name: "router",
        component: () => import("pages/RouterPage.vue"),
        meta: { requiresAuth: true, roles: ["admin", "courier"] },
      },
      {
        path: "chat",
        name: "chat",
        component: () => import("pages/IndexPage.vue"),
      },
      {
        path: "settings",
        name: "settings",
        component: () => import("pages/IndexPage.vue"),
      },
    ],
  },
  {
    path: "/:catchAll(.*)",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
