from .models import Order, OrderProduct
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from store.models import Store
from product.models import Product, Inventory
from user.models import Employee
import json

from rest_framework.generics import (
    RetrieveAPIView,
    DestroyAPIView,
    ListAPIView,
)
from django.http import JsonResponse
from datetime import datetime


from rest_framework.views import APIView


class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


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
            product = Product.objects.get(id=product_info['product'])
            OrderProduct.objects.create(
                product=product, order=order, quantity=product_info['quantity']
            )
            inventory = Inventory.objects.get(product=product, store=store)
            inventory.stock -= int(product_info['quantity'])
            inventory.save()
        return JsonResponse({'status': 200})


class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
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
            order.completion_date = completion_date
            order.status = request.data['status']
            order.save()
        return JsonResponse({'status': 200})


class OrderDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.courier:
            instance.courier.route = None
            instance.courier.save()
        self.perform_destroy(instance)
        return JsonResponse({'status': 200})


class OrderMultipleDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        orders_ids = data['orders_ids']
        for order_id in orders_ids:
            order = Order.objects.get(id=order_id)
            if order.courier:
                order.courier.route = None
                order.courier.save()
            order.delete()

        return JsonResponse({'status': 200})


class OrderCourierDelete(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        courier = Employee.objects.get(id=pk)
        order = Order.objects.get(courier=courier)
        order.courier = None
        order.save()
        return JsonResponse({'status': 200})
