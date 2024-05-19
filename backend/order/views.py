from django.shortcuts import render
from .models import Order, OrderProduct
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from store.models import Store
from product.models import Product, Inventory
from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView, 
)
from django.http import JsonResponse, HttpResponse


from rest_framework.views import APIView

class OrderListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        store_id = request.data['store']
        store = Store.objects.get(id=store_id)
        order = Order.objects.create(store=store)
        products = request.data['products']
        for product_info in products:
            product = Product.objects.get(id=product_info["product"])
            OrderProduct.objects.create(product=product, order=order, quantity=product_info["quantity"])
            inventory = Inventory.objects.get(product=product, store=store)
            inventory.stock -= product_info["quantity"]
            inventory.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
