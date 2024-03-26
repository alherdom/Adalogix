<template>
  <q-table :rows="users" :columns="columns" row-key="id" :pagination="{ rowsPerPage: 10 }">
  </q-table>
</template>

<script>
import { getRequest } from 'src/utils/common';

export default {
  data() {
    return {
      users: [],
      columns: [
        {
          name: 'id',
          required: true,
          label: 'ID',
          align: 'left',
          field: 'id',
          sortable: true
        },
        {
          name: 'username',
          required: true,
          label: 'Username',
          align: 'left',
          field: 'username',
          sortable: true
        },
        {
          name: 'first_name',
          required: true,
          label: 'Name',
          align: 'left',
          field: 'first_name',
          sortable: true
        },
        {
          name: 'last_name',
          required: true,
          label: 'Last Name',
          align: 'left',
          field: 'last_name',
          sortable: true
        },
        {
          name: 'email',
          required: true,
          label: 'Email',
          align: 'left',
          field: 'email',
          sortable: true
        },
        {
          name: 'role',
          required: true,
          label: 'Role',
          align: 'left',
          field: 'groups__name',
          sortable: true
        }
      ]
    }
  },
  created() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const url = 'http://localhost:8000/user/list';
        const responseData = await getRequest(url); // Assuming API endpoint is '/api/users'
        this.users = responseData;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    }
  }
}
</script>

<style scoped>
/* Estilos específicos para la tabla si es necesario */
</style>
