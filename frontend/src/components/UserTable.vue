<template>
  <q-table
    class="my-sticky-dynamic"
    dense
    bordered
    title="Users Table"
    :rows="users"
    :columns="columns"
    :loading="loading"
    row-key="id"
    virtual-scroll
    :virtual-scroll-item-size="48"
    :virtual-scroll-sticky-size-start="48"
    :pagination="pagination"
    :rows-per-page-options="[0]"
    @virtual-scroll="onScroll"
    v-model:selected="selectedRows"
    selection="multiple"
  >
    <template v-slot:top-right>
      <q-btn
        class="registerUser"
        color="primary"
        no-caps
        dense
        flat
        text-color="black"
        icon-right="add"
        label="Register new user"
        @click="registerUser"
      />
    </template>
    <template v-slot:bottom-row>
      <q-tr>
        <q-td colspan="100%"> Button row </q-td>
      </q-tr>
    </template>
    <template v-slot:bottom> Button </template>

  </q-table>
</template>

<!-- <script>
import Swal from "sweetalert2";
import { useRouter } from "vue-router";
import { getRequest } from "src/utils/common";
import { ref, computed, nextTick, onMounted } from "vue";

export default {
  data() {
    return {
      users: [],
      columns: [
        {
          name: "id",
          required: true,
          label: "ID",
          align: "left",
          field: "id",
          sortable: true,
        },
        {
          name: "username",
          required: true,
          label: "Username",
          align: "left",
          field: "username",
          sortable: true,
        },
        {
          name: "first_name",
          required: true,
          label: "Name",
          align: "left",
          field: "first_name",
          sortable: true,
        },
        {
          name: "last_name",
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
        {
          name: "role",
          required: true,
          label: "Role",
          align: "left",
          field: "groups__name",
          sortable: true,
        },
      ],
    };
  },
  created() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const url = "http://localhost:8000/user/list";
        const responseData = await getRequest(url); // Assuming API endpoint is '/api/users'
        this.users = responseData;
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    },
    registerUser() {
      this.route.push("#/main/register");
    },
  },
};
</script> -->

<script>
import Swal from "sweetalert2";
import { useRouter } from "vue-router";
import { getRequest } from "src/utils/common";
import { ref, computed, nextTick, onMounted } from "vue";

export default {
  setup() {
    const users = ref([]);
    const router = useRouter();
    const selectedRows = ref([]);

    // Function to fetch users from the server
    const fetchUsers = async () => {
      try {
        const url = "http://localhost:8000/user/list";
        const responseData = await getRequest(url);
        users.value = responseData;
      } catch (error) {
        console.error("Error fetching users:", error);
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Failed to fetch users",
        });
      }
    };

    // Redirect to register user page
    const registerUser = () => {
      router.push("/register");
    };

    // Life cycle hook
    onMounted(fetchUsers);

    // Define the columns for the table
    const columns = [
      {
        name: "id",
        required: true,
        label: "ID",
        align: "left",
        field: "id",
        sortable: true,
      },
      {
        name: "username",
        required: true,
        label: "Username",
        align: "left",
        field: "username",
        sortable: true,
      },
      {
        name: "first_name",
        required: true,
        label: "Name",
        align: "left",
        field: "first_name",
        sortable: true,
      },
      {
        name: "last_name",
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
      {
        name: "role",
        required: true,
        label: "Role",
        align: "left",
        field: "groups__name",
        sortable: true,
      },
    ];

    // Retorno de datos y funciones del setup
    return {
      selectedRows,
      users,
      columns,
      registerUser,
    };
  },
};
</script>
