<!-- <template>
  <q-toolbar>
    <q-input
      class="rounded"
      v-model="filter"
      debounce="300"
      placeholder="Search"
    >
      <template v-slot:prepend>
        <q-icon name="search" />
      </template>
    </q-input>
    <q-btn
      class="add-btn"
      color="primary"
      push
      size="md"
      icon="add"
      label="add item"
      @click="addProduct"
    />
  </q-toolbar>
  <q-table
    table-header-class="table_header"
    :rows="products"
    :columns="columns"
    filter=""
    class="full-width"
    flat bordered
    virtual-scroll
    virtual-scroll-item-size="1"
    row-key="id"
    :pagination="{ rowsPerPage: 50 }"
  >
    <template v-slot:body-cell-quantity="props">
      <q-td :props="props"> {{ props.row.quantity }} units </q-td>
    </template>
    <template v-slot:body-cell-price="props">
      <q-td :props="props"> {{ props.row.price }} € </q-td>
    </template>
    <template v-slot:body-cell-actions="props">
      <q-td :props="props">
        <q-btn
          class="actions-btn"
          color="primary"
          push
          size="sm"
          icon="edit"
          @click="editProduct(props.row)"
        />
        <q-btn
          class="actions-btn"
          color="negative"
          push
          size="sm"
          icon="delete"
          @click="deleteProduct(props.row)"
        />
      </q-td>
    </template>
  </q-table>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "src/utils/common";

export default {
  data() {
    return {
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
          name: "name",
          required: true,
          label: "Name",
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
          name: "price",
          required: true,
          label: "Price",
          align: "left",
          field: "price",
          sortable: true,
        },
        {
          name: "quantity",
          required: true,
          label: "Quantity",
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
          name: "actions",
          label: "Actions",
          align: "left",
          field: "actions",
        },
      ],
      products: [],
    };
  },
  created() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      try {
        const url = "http://localhost:8000/product/list/";
        const responseData = await getRequest(url);
        this.products = responseData.results;
      } catch (error) {
        console.error("Error getting products:", error);
      }
    },
    deleteProduct(product) {
      Swal.fire({
        title: "Are you sure?",
        text: "You will not be able to recover this product!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, keep it",
      }).then((result) => {
        if (result.isConfirmed) {
          const url = `http://localhost:8000/product/delete/${product.id}/`;
          fetch(url, {
            method: "DELETE",
          }).then(() => {
            this.getProducts();
            Swal.fire("Deleted!", "Your product has been deleted.", "success");
          });
        }
      });
    },
  },
};
</script>

<style scoped>
.thead tr {
  height: 50px;
  background-color: red !important;
}

.actions-btn {
  height: 20px;
  width: 20px;
}

.q-btn:nth-child(2) {
  margin-left: 10px;
}

.q-toolbar {
  display: flex;
  justify-content: space-around;
  padding: 0px 0px 20px 0px;
}

.search-input {
  width: 20%;
  font-size: 15px;
}

.add-btn {
  width: 115px;
  padding: 0px 5px 0px 0px;
  font-weight: bolder;
}
</style> -->
<!-- <template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-dynamic"
      flat
      bordered
      title=""
      :rows="rows"
      :columns="columns"
      :loading="loading"
      row-key="index"
      virtual-scroll
      :virtual-scroll-item-size="48"
      :virtual-scroll-sticky-size-start="48"
      :pagination="pagination"
      :rows-per-page-options="[0]"
      @virtual-scroll="onScroll"
      selection="multiple"
      v-model:selected="selected"
    >
      <template v-slot:bottom-row>
        <q-tr>
          <q-td colspan="100%"> Bottom row </q-td>
        </q-tr>
      </template>

      <template v-slot:bottom> Bottom </template>
    </q-table>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "src/utils/common";
import { ref, computed, nextTick, onMounted } from "vue";

const columns = [
  {
    name: "id",
    required: true,
    label: "Id",
    align: "left",
    field: "id",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "Product Name",
    align: "left",
    field: (row) => row.name,
    format: (val) => val,
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
    name: "price",
    required: true,
    label: "Price",
    align: "left",
    field: "price",
    sortable: true,
  },
  {
    name: "quantity",
    required: true,
    label: "Quantity",
    align: "left",
    field: "quantity",
    sortable: true,
  },
  {
    name: "actions",
    label: "Actions",
    align: "left",
    field: "actions",
  },
];

// const allRows = [
//   { name: 'Product 1', description: 'Description 1', price: 100, quantity: 10 },
//   { name: 'Product 2', description: 'Description 2', price: 200, quantity: 20 },
//   { name: 'Product 3', description: 'Description 3', price: 300, quantity: 30 }]

// const pageSize = 50
// const lastPage = Math.ceil(allRows.length / pageSize)

export default {
  setup() {
    const nextPage = ref(2);
    const loading = ref(false);
    const allRows = ref([]);
    const selected = ref([]);
    const pageSize = 50;
    const lastPage = Math.ceil(allRows.value.length / pageSize);
    const rows = computed(() =>
      allRows.value.slice(0, pageSize * (nextPage.value - 1))
    );
    const fetchData = async () => {
      try {
        loading.value = true;
        const response = await getRequest("http://localhost:8000/product/list"); // Reemplaza '/api/products' con tu ruta de la API
        allRows.value = response.results; // Asumiendo que los datos de la API están en un objeto con una propiedad 'products'
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

    const onScroll = ({ to, ref }) => {
      const lastIndex = rows.value.length - 1;

      if (
        !loading.value &&
        nextPage.value < lastPage.value &&
        to === lastIndex
      ) {
        loading.value = true;

        setTimeout(() => {
          nextPage.value++;
          nextTick(() => {
            ref.refresh();
            loading.value = false;
          });
        }, 500);
      }
    };

    return {
      selected,
      columns,
      rows,

      nextPage,
      loading,

      pagination: { rowsPerPage: 0 },

      onScroll({ to, ref }) {
        const lastIndex = rows.value.length - 1;

        if (
          loading.value !== true &&
          nextPage.value < lastPage &&
          to === lastIndex
        ) {
          loading.value = true;

          setTimeout(() => {
            nextPage.value++;
            nextTick(() => {
              ref.refresh();
              loading.value = false;
            });
          }, 500);
        }
      },
    };
  },
};
</script>

<style lang="sass">
.my-sticky-dynamic
  /* height or max-height is important */
  height: 90vh

  .q-table__top,
  thead tr:first-child th /* bg color is important for th; just specify one */
    background-color: #5840FF
    color: white

  thead tr th
    position: sticky
    z-index: 1
  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
  thead tr:first-child th
    top: 0

  /* prevent scrolling behind sticky top row on focus */
  tbody
    /* height of all previous header rows */
    scroll-margin-top: 48px
</style> -->
<template>
  <div class="q-pa-md">
    <q-table class="my-sticky-dynamic" flat bordered title="" :rows="rows" :columns="columns" :loading="loading"
      row-key="id" virtual-scroll :virtual-scroll-item-size="48" :virtual-scroll-sticky-size-start="48"
      :pagination="pagination" :rows-per-page-options="[0]" @virtual-scroll="onScroll" v-model:selected="selectedRows"
      selection="multiple">
      <template v-slot:bottom-row>
        <q-tr>
          <q-td colspan="100%">
            Bottom row
          </q-td>
        </q-tr>
      </template>

      <template v-slot:bottom>
        Bottom
      </template>
    </q-table>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import { getRequest } from "src/utils/common";
import { ref, computed, nextTick, onMounted } from "vue";

const columns = [
  {
    name: "id",
    required: true,
    label: "Id",
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
    format: (val) => val,
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
    name: "price",
    required: true,
    label: "Price",
    align: "left",
    field: "price",
    sortable: true,
  },
  {
    name: "quantity",
    required: true,
    label: "Quantity",
    align: "left",
    field: "quantity",
    sortable: true,
  },
  {
    name: "actions",
    label: "Actions",
    align: "left",
    field: "actions",
  },
];

export default {
  setup() {
    const nextPage = ref(2);
    const loading = ref(false);
    const lastPage = ref(0);
    const allRows = ref([]);
    const selectedRows = ref([]);
    const rows = ref([]);
    let pageSize = 0;
    
    const fetchData = async () => {
      try {
        loading.value = true;
        const response = await getRequest("http://localhost:8000/product/list");
        allRows.value = response.results;
        pageSize = allRows.value.length;
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

    const onScroll = ({ index, ref }) => {
      const lastIndex = rows.value.length - 1;

      if (
        !loading.value &&
        nextPage.value < lastPage.value &&
        index === lastIndex
      ) {
        loading.value = true;

        setTimeout(() => {
          nextPage.value++;
          nextTick(() => {
            ref.refresh();
            loading.value = false;
          });
        }, 500);
      }
    };

    return {
      selectedRows,
      columns,
      rows: computed(() => allRows.value.slice(0, pageSize * (nextPage.value - 1))),
      nextPage,
      loading,
      pagination: { rowsPerPage: 0 },
      onScroll,
    };
  },
};
</script>

<style lang="sass">
.my-sticky-dynamic
  /* height or max-height is important */
  height: 90vh

  .q-table__top,
  thead tr:first-child th /* bg color is important for th; just specify one */
    background-color: #5840FF
    color: white

  thead tr th
    position: sticky
    z-index: 1
  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
  thead tr:first-child th
    top: 0

  /* prevent scrolling behind sticky top row on focus */
  tbody
    /* height of all previous header rows */
    scroll-margin-top: 48px
</style>
