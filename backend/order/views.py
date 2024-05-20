from django.shortcuts import render
from .models import Order, OrderProduct
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from store.models import Store
from product.models import Product, Inventory
from rest_framework.response import Response
from user.models import Employee

from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView, 
)
from django.http import JsonResponse, HttpResponse
from datetime import datetime


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
        print(products)
        for product_info in products:
            product = Product.objects.get(id=product_info["product"])
            OrderProduct.objects.create(product=product, order=order, quantity=product_info["quantity"])
            inventory = Inventory.objects.get(product=product, store=store)
            inventory.stock -= int(product_info["quantity"])
            inventory.save()
        return JsonResponse({"status": 200})

# class OrderUpdateView(UpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()

class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        print(request.data)
        order = Order.objects.get(id=pk)
        completion_date = None
        courier = None
        if request.data.get('courier'):
            if request.data['courier']:
                courier = Employee.objects.get(id=request.data['courier'])
            order.courier = courier
            order.save()
        if request.data.get('status') and request.data.get('completion_date'):
            if request.data['completion_date']:
                completion_date = datetime.fromisoformat(request.data['completion_date'])
            print(completion_date)
            order.completion_date = completion_date
            order.status = request.data['status']
            order.save()
        return JsonResponse({"status": 200})