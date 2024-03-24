<template>
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
