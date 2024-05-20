from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import StoreListSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Store
from product.models import Inventory
from product.serializers import InventorySerializer
from rest_framework.response import Response
import json


class StoreListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class StoreDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class ProductStoreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stores_to_return = []
        stores = Store.objects.filter(product__id=request.GET['product_id'])
        for store in stores:
            store_info = {}
            store_info['id'] = store.id
            store_info['name'] = store.name
            store_info['address'] = store.address
            store_info['stock'] = store.inventory_set.get(
                product__id=request.GET['product_id']
            ).stock
            stores_to_return.append(store_info)
        return JsonResponse(stores_to_return, safe=False)
    
class ProductStoreInventoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        store = Store.objects.get(id=pk)
        inventories = Inventory.objects.filter(store=store)
        inventory_list = []
        for inventory in inventories:
             inventory_list.append(InventorySerializer(inventory).data)
        return Response(inventory_list)
