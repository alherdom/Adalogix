<template>
  <q-table
    class="my-sticky-header-table"
    flat
    bordered
    title="Users Table"
    :rows="displayedUsers"
    :columns="columns"
    :loading="loading"
    row-key="user"
    v-model:selected="selectedRows"
    selection="multiple"
    :pagination="{ rowsPerPage: 20 }"
  >
    <template v-slot:top>
      <q-toolbar-title> Users Table </q-toolbar-title>
      <q-space />
      <div class="row">
        <div class="col-12 q-mt-md q-ml-xl q-mr-xl">
          <q-input
            outlined
            rounded
            dense
            style="width: 450px"
            debounce="300"
            color="primary"
            v-model="filter"
            placeholder="Search User..."
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </div>
      </div>
      <q-space />
      <div class="row">
        <div class="col-12 q-mt-md q-mr-xl">
          <q-btn
            class="q-ml-xl"
            color="primary"
            text-color="black"
            :disable="loading"
            no-caps
            dense
            flat
            label="Delete Users"
            icon="delete"
            @click="deleteUser"
          />
          <q-btn
            class="q-ml-sm"
            color="primary"
            text-color="black"
            :disable="loading"
            no-caps
            dense
            flat
            label="Register User"
            icon="cloud_upload"
            @click="registerForm = true"
          />
          <q-btn
            class="q-ml-sm"
            color="primary"
            text-color="black"
            :disable="loading"
            no-caps
            dense
            flat
            label="Export CSV"
            icon="archive"
            @click="exportTable"
          />
        </div>
      </div>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td>
        <q-btn
          class="actions-btn"
          color="primary"
          flat
          icon="edit"
          @click="editUser(props.row)"
        />
      </q-td>
    </template>
  </q-table>
  <q-dialog v-model="registerForm">
    <RegisterForm @closeEditForm="closeEditUserForm" />
  </q-dialog>
  <q-dialog v-model="editUserForm">
    <EditUserForm :user="userData" @closeEditForm="closeEditUserForm" />
  </q-dialog>
</template>

<script setup>
import Swal from "sweetalert2";
import { getRequest, deleteRequest } from "../utils/common";
import { ref, onMounted, computed } from "vue";
import { exportFile, useQuasar } from "quasar";
import RegisterForm from "./RegisterForm.vue";
import EditUserForm from "./EditUserForm.vue";

function wrapCsvValue(val, formatFn, row) {
  let formatted = formatFn !== void 0 ? formatFn(val, row) : val;
  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);
  formatted = formatted.split('"').join('""');
  return `"${formatted}"`;
}

const $q = useQuasar();
const exportTable = () => {
  const content = [columns.map((col) => wrapCsvValue(col.label))]
    .concat(
      items.value.map((row) =>
        columns
          .map((col) =>
            wrapCsvValue(
              typeof col.field === "function"
                ? col.field(row)
                : row[col.field === void 0 ? col.name : col.field],
              col.format,
              row
            )
          )
          .join(",")
      )
    )
    .join("\r\n");

  const status = exportFile("users-table.csv", content, "text/csv");

  if (status !== true) {
    $q.notify({
      message: "Browser denied file download...",
      color: "negative",
      icon: "warning",
    });
  }
};

const columns = [
  {
    name: "id",
    required: true,
    label: "Id",
    align: "left",
    field: "user",
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
    name: "role",
    required: true,
    label: "Role",
    align: "left",
    field: "role",
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
    name: "email",
    required: true,
    label: "Email",
    align: "left",
    field: "email",
    sortable: true,
  },
  { name: "actions", label: "Edit User", align: "left", field: "actions" },
];

const userData = ref({});
const loading = ref(false);
const selectedRows = ref([]);
const users = ref([]);
const filter = ref("");
const registerForm = ref(false);
const editUserForm = ref(false);

const fetchData = async () => {
  try {
    loading.value = true;
    const url = "http://localhost:8000/user/list";
    const response = await getRequest(url);
    users.value = response.map((user) => ({ ...user }));
  } catch (error) {
    console.error("Error fetching data:", error);
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Something went wrong while fetching data!",
    });
  } finally {
    loading.value = false;
  }
};

onMounted(fetchData);

const deleteUser = async () => {
  if (selectedRows.value.length === 0) {
    Swal.fire({
      title: "No users selected",
      text: "Please select users to delete",
      icon: "error",
      showConfirmButton: false,
      timer: 1500,
    });
    return;
  }
  Swal.fire({
    title: "Delete users?",
    text: "Are you sure you want to delete the selected users?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes",
    cancelButtonText: "No",
  }).then(async (result) => {
    if (result.isConfirmed) {
      const requestData = {
        employee_ids: selectedRows.value.map((item) => item.user),
      };
      const url = "http://localhost:8000/user/delete/multiple/";
      try {
        const response = await deleteRequest(requestData, url);
        if (response.status === 200) {
          selectedRows.value = [];
          fetchData();
        }
      } catch (error) {
        console.error("Error deleting users:", error);
      }
    }
  });
};

const editUser = (userProps) => {
  userData.value = userProps;
  editUserForm.value = true;
};

const closeEditUserForm = (value) => {
  editUserForm.value = value;
  registerForm.value = value;
  fetchData();
};

const displayedUsers = computed(() => {
  return users.value.filter((user) => {
    if (!filter.value) return true;
    const search = filter.value.toLowerCase();
    return (
      user.username.toLowerCase().includes(search) ||
      user.first_name.toLowerCase().includes(search) ||
      user.last_name.toLowerCase().includes(search) ||
      user.email.toLowerCase().includes(search) ||
      user.role.toLowerCase().includes(search)
    );
  });
});
</script>
