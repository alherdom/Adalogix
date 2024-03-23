<template>
    <q-table
      :rows="products"
      :columns="columns"
      row-key="id"
      :pagination="true"
    >
      <template v-slot:body-cell-quantity="props">
        <q-td :props="props">
          {{ props.row.quantity }} unidades
        </q-td>
      </template>
      <template v-slot:body-cell-price="props">
        <q-td :props="props">
          ${{ props.row.price.toFixed(2) }}
        </q-td>
      </template>
    </q-table>
</template>

<script>
export default {
  data() {
    return {
      columns: [
        {
          name: 'name',
          required: true,
          label: 'Name',
          align: 'left',
          field: 'name',
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
          name: 'price',
          required: true,
          label: 'Price',
          align: 'left',
          field: 'price',
          sortable: true
        }
      ],
      products: [
        { id: 1, name: 'Producto 1', quantity: 10, price: 15.99 },
        { id: 2, name: 'Producto 2', quantity: 5, price: 24.99 },
        { id: 3, name: 'Producto 3', quantity: 20, price: 9.99 },
        { id: 4, name: 'Producto 4', quantity: 15, price: 19.99},
        { id: 5, name: 'Producto 5', quantity: 30, price: 14.99},
        { id: 6, name: 'Producto 6', quantity: 25, price: 29.99},
        { id: 7, name: 'Producto 7', quantity: 40, price: 19.99},
        { id: 8, name: 'Producto 8', quantity: 35, price: 24.99},
        { id: 9, name: 'Producto 9', quantity: 50, price: 14.99},
        { id: 10, name: 'Producto 10', quantity: 45, price: 29.99},
        { id: 11, name: 'Producto 11', quantity: 60, price: 19.99},
        { id: 12, name: 'Producto 12', quantity: 55, price: 24.99},
        { id: 13, name: 'Producto 13', quantity: 70, price: 14.99},
        { id: 14, name: 'Producto 14', quantity: 65, price: 29.99},
        { id: 15, name: 'Producto 15', quantity: 80, price: 19.99},
        { id: 16, name: 'Producto 16', quantity: 75, price: 24.99},
        { id: 17, name: 'Producto 17', quantity: 90, price: 14.99},
        { id: 18, name: 'Producto 18', quantity: 85, price: 29.99},
        { id: 19, name: 'Producto 19', quantity: 100, price: 19.99},
        { id: 20, name: 'Producto 20', quantity: 95, price: 24.99},
        // Agrega más productos aquí si es necesario
      ]
    }
  }
}
</script>
