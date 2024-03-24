<template>
      <q-toolbar>
          <!-- Input de búsqueda -->
          <q-input v-model="filter" debounce="300" placeholder="Search" />
          <q-btn color="primary" icon="add" label="" @click="addProduct" />
      </q-toolbar>
  <q-table :rows="products" :columns="columns" row-key="id" :pagination="{ rowsPerPage: 10 }">
    <template v-slot:body-cell-quantity="props">
      <q-td :props="props">
        {{ props.row.quantity }} uds
      </q-td>
    </template>
    <template v-slot:body-cell-price="props">
      <q-td :props="props">
        ${{ props.row.price }}
      </q-td>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td :props="props">
        <q-btn class="actions-btn" color="primary" icon="edit" @click="editProduct(props.row)" />
        <q-btn class="actions-btn" color="negative" icon="delete" @click="deleteProduct(props.row)" />
      </q-td>
    </template>
    <!-- <template v-slot:top>
      <q-btn color="primary" icon="add" label="ADD PRODUCT" @click="addProduct" />
    </template> -->
    </q-table>
</template>

<script>
import { getRequest } from 'src/utils/common';

export default {
  data() {
    return {
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
          name: 'name',
          required: true,
          label: 'Name',
          align: 'left',
          field: 'name',
          sortable: true
        },
        {
          name: 'description',
          required: true,
          label: 'Description',
          align: 'left',
          field: 'description',
          sortable: true
        },
        {
          name: 'price',
          required: true,
          label: 'Price',
          align: 'left',
          field: 'price',
          sortable: true
        },
        {
          name: 'quantity',
          required: true,
          label: 'Quantity',
          align: 'left',
          field: 'quantity',
          sortable: true
        },
        {
          name: 'category',
          required: true,
          label: 'Category',
          align: 'left',
          field: 'category',
          sortable: true
        },
        {
          name: 'actions',
          label: 'Actions',
          align: 'left',
          field: 'actions'
        }
      ],
      products: [],
    }
  },
  created() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      try {
        const url = 'http://localhost:8000/product/list/';
        const responseData = await getRequest(url);
        this.products = responseData.results;
      } catch (error) {
        console.error('Error getting products:', error);
      }
    },
  }
}
</script>

<style scoped>
.actions-btn {
  height: 35px;
  width: 35px;
}

.q-btn:nth-child(2) {
  margin-left: 10px;
}
.q-toolbar {
  display: flex;
  justify-content: space-around;
  padding: 0px 100px 20px;
}
</style>
