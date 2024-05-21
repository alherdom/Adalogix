<template>
  <q-btn
    push
    size="12px"
    class="q-ml-xs q-mt-lg action-btn"
    color="white"
    text-color="black"
    :disable="loading"
    icon="qr_code_scanner"
    @click="openDialog = true"
  >
    <q-tooltip
      anchor="bottom middle"
      transition-show="scale"
      transition-hide="scale"
    >
      Code Reader
    </q-tooltip>
  </q-btn>
  <q-dialog v-model="openDialog" persistent>
    <q-card :disable="loading" class="dialog-qr">
      <q-card-section class="row">
        <div class="text-h6" style="font-weight: 400"
          >Scan QR Code
        </div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>
      <StreamBarcodeReader @decode="handleDecode" />
      <q-card-section class="row q-py-xs">
        <div v-if="errorMessage" class="text-negative">
          {{ errorMessage }}
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog v-model="showProductDetail">
    <ProductDetail class="product-detail-table"
      :productId="productId"
      @closeProductDetail="closeProductDetailTable"
    />
  </q-dialog>
</template>

<script setup>
import { ref } from "vue";
import { StreamBarcodeReader } from "vue-barcode-reader";
import ProductDetail from "./ProductDetail.vue";

const loading = ref(false);
const openDialog = ref(false);
const productId = ref(null);
const showProductDetail = ref(false);
const errorMessage = ref("");

const emit = defineEmits(["decodedValues"]);
const handleDecode = (value) => {
  try {
    if (typeof value !== "string") {
      throw new Error("Invalid value type");
    }

    const match = value.match(/^\d+$/);
    if (!match) {
      errorMessage.value = "Please scan a valid product code";
      setTimeout(() => {
        errorMessage.value = "";
      }, 3000);
      return;
    }

    productId.value = value;
    errorMessage.value = ""; // Clear any previous error message
    openDialog.value = false;
    showProductDetail.value = true;
  } catch (error) {
    errorMessage.value = "An error occurred while decoding the QR code!";
    setTimeout(() => {
      errorMessage.value = "";
    }, 3000);
  }
};

const closeProductDetailTable = () => {
  productId.value = null;
  errorMessage.value = "";
  showProductDetail.value = false;
};
</script>

<style scoped>
.text-negative {
  color: #c10015;
  font-size: 15px;
}
</style>
