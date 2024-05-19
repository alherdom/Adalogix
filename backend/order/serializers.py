from rest_framework import serializers
from .models import Order, OrderProduct
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(source='orderproduct_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'store', 'courier', 'order_products', 'created_at', 'status']

    def create(self, validated_data):
        products_data = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            OrderProduct.objects.create(order=order, **product_data)
            
        return order


