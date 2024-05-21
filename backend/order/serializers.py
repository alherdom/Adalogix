from rest_framework import serializers
from .models import Order, OrderProduct
from product.models import Product
from store.serializer import StoreListSerializer
from user.serializers import EmployeeSerializer, EmployeeOrderSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(source='orderproduct_set', many=True, required=False)
    store = StoreListSerializer(required=False)
    courier = EmployeeOrderSerializer()

    class Meta:
        model = Order
        fields = ['id', 'store', 'courier', 'order_products', 'created_at', 'status', 'completion_date']

    def create(self, validated_data):
        products_data = validated_data.pop('order_products', [])
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            OrderProduct.objects.create(order=order, **product_data)
            
        return order

    def update(self, instance, validated_data):
        courier_data = validated_data.pop('courier', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if courier_data is not None:
            # Check if the order has an existing courier
            if instance.courier:
                # Update the existing courier
                courier_serializer = EmployeeOrderSerializer(instance.courier, data=courier_data, partial=True)
            else:
                # Create a new courier
                courier_serializer = EmployeeOrderSerializer(data=courier_data)

            if courier_serializer.is_valid(raise_exception=True):
                courier_serializer.save()
                # Set the updated or newly created courier back to the order
                instance.courier = courier_serializer.instance

        return instance
