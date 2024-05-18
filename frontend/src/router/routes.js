// const routes = [
//   {
//     path: "/login",
//     name: "login",
//     component: () => import("pages/LoginPage.vue"),
//   },
//   {
//     path: "/",
//     name: "main",
//     component: () => import("layouts/MainLayout.vue"),
//     meta: { requiresAuth: true, roles: ["admin", "courier"] },
//     children: [
//       {
//         path: "",
//         name: "home",
//         component: () => import("pages/IndexPage.vue"),
//       },
//       {
//         path: "inventory",
//         name: "inventory",
//         component: () => import("pages/InventoryPage.vue"),
//         meta: { requiresAuth: true, roles: ["admin"] },
//         children: [],
//       },
//       {
//         path: "users",
//         name: "users",
//         component: () => import("pages/UsersPage.vue"),
//         meta: { requiresAuth: true, roles: ["admin"] },
//         children: [
//           {
//             path: "profile",
//             name: "profile",
//             component: () => import("pages/ProfilePage.vue"),
//             meta: { requiresAuth: true, roles: ["admin"] },
//           },
//         ],
//       },
//       {
//         path: "register",
//         name: "register",
//         component: () => import("pages/RegisterPage.vue"),
//         meta: { requiresAuth: true, roles: ["admin"] },
//       },
//       {
//         path: "router",
//         name: "router",
//         component: () => import("pages/RouterPage.vue"),
//         meta: { requiresAuth: true, roles: ["admin"] },
//       },
//       {
//         path: "courier-router",
//         name: "courier-router",
//         component: () => import("pages/RouterCourierPage.vue"),
//         meta: { requiresAuth: true, roles: ["courier"] },
//       },
//       {
//         path: "chat",
//         name: "chat",
//         component: () => import("pages/ChatPage.vue"),
//       },
//       {
//         path: "settings",
//         name: "settings",
//         component: () => import("pages/IndexPage.vue"),
//       },
//     ],
//   },
//   {
//     path: "/:catchAll(.*)",
//     component: () => import("pages/ErrorNotFound.vue"),
//   },
// ];

// export default routes;
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
        path: "",
        name: "home",
        component: () => import("pages/IndexPage.vue"),
      },
      {
        path: "inventory",
        name: "inventory",
        component: () => import("pages/InventoryPage.vue"),
        meta: { requiresAuth: true, roles: ["admin"] },
        children: [],
      },
      {
        path: "users",
        name: "users",
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
        component: () => import("pages/ChatPage.vue"),
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
