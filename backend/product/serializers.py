from rest_framework import serializers

from .models import Product, Store, Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Inventory
        fields = ['id', 'stock', 'product']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product_name'] = instance.product.name
        return representation

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'