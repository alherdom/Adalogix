export const links = [
  {
    path: "/orders",
    label: "Orders",
    icon: "dashboard_customize",
    roles: ["admin"],
  },
  {
    path: "/inventories",
    label: "Inventories",
    icon: "inventory",
    roles: ["admin"],
  },
  {
    path: "/employees",
    label: "Employees",
    icon: "people_alt",
    roles: ["admin"],
  },
  {
    path: "/router",
    label: "Router",
    icon: "fmd_good",
    roles: ["admin", "courier"],
  },
  {
    path: "/chat",
    label: "Chat",
    icon: "comment",
    roles: ["admin", "courier"],
  },
  {
    path: "/settings",
    label: "Settings",
    icon: "settings",
    roles: ["admin", "courier"],
  },
];

export const inventoryColumns = [
  {
    name: "id",
    required: true,
    label: "Product Code",
    align: "left",
    field: "id",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "Product Name",
    align: "left",
    field: "name",
    sortable: true,
  },
  {
    name: "description",
    required: true,
    label: "Description",
    align: "left",
    field: "description",
    sortable: true,
  },
  {
    name: "quantity",
    required: true,
    label: "Total Stock",
    align: "left",
    field: "quantity",
    sortable: true,
  },
  {
    name: "category",
    required: true,
    label: "Category",
    align: "left",
    field: "category",
    sortable: true,
  },
  {
    name: "price",
    required: true,
    label: "Price €",
    align: "left",
    field: "price",
    sortable: true,
  },
  {
    name: "weight",
    required: true,
    label: "Weight Kg",
    align: "left",
    field: "weight",
    sortable: true,
  },
  {
    name: "volume",
    required: true,
    label: "Volume m3",
    align: "left",
    field: "volume",
    sortable: true,
  },
  { name: "actions", label: "Actions", align: "left", field: "actions" },
];

export const userColumns = [
  {
    name: "id",
    required: true,
    label: "Employee Code",
    align: "left",
    field: "id",
    sortable: true,
  },
  {
    name: "userName",
    required: true,
    label: "Username",
    align: "left",
    field: "username",
    sortable: true,
  },
  {
    name: "firstName",
    required: true,
    label: "First Name",
    align: "left",
    field: "first_name",
    sortable: true,
  },
  {
    name: "lastName",
    required: true,
    label: "Last Name",
    align: "left",
    field: "last_name",
    sortable: true,
  },
  {
    name: "role",
    required: true,
    label: "Role",
    align: "left",
    field: "role",
    sortable: true,
  },
  {
    name: "email",
    required: true,
    label: "Email",
    align: "left",
    field: "email",
    sortable: true,
  },
  { name: "actions", label: "Actions", align: "left", field: "actions" },
];

export const storeColumns = [
  {
    name: "id",
    required: true,
    label: "Store Code",
    align: "left",
    field: "id",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "Store Name",
    align: "left",
    field: "name",
    sortable: true,
  },
  {
    name: "address",
    required: true,
    label: "Address",
    align: "left",
    field: "address",
    sortable: true,
  },
  {
    name: "productId",
    required: true,
    label: "Code",
    align: "left",
    field: "productId",
    sortable: true,
  },
  {
    name: "stock",
    required: true,
    label: "Stock",
    align: "left",
    field: "stock",
    sortable: true,
  },
  { name: "actions", label: "Update", align: "left", field: "actions" },
];
