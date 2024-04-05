import csv
import json

from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from store.models import Store

from .models import Inventory, Product
from .serializers import ProductDetailSerializer


class ProductMultipleDelete(APIView):
    def delete(self, request):
        data = json.loads(request.body)
        product_ids = data['product_ids']
        for product_id in product_ids:
            Product.objects.get(id=product_id).delete()
        return JsonResponse({'status': 200})


class ProductList(APIView):
    def get(self, request):
        products_to_return = []
        products = Product.objects.all()
        for product in products:
            quantity = Inventory.objects.filter(product=product).count()
            products_to_return.append(
                {
                    'id': product.id,
                    'description': product.description,
                    'quantity': quantity,
                    'category': product.category,
                    'pirce': product.price,
                    'weight': product.weight,
                    'volume': product.volume,
                }
            )
        return JsonResponse(products_to_return, safe=False)


class ProductCreateCsv(APIView):
    def post(self, request):
        if file := request.FILES.get('products'):
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            general_store = Store.objects.get(id=0)
            for row in reader:
                name, description, price, category, weight, volume, quantity = (
                    row['name'],
                    row['description'],
                    row['price'],
                    row['category'],
                    row['weight'],
                    row['volume'],
                    row['quantity'],
                )
                new_product = Product.objects.create(
                    name, description, price, category, weight, volume
                )
                Inventory.objects.create(product=new_product, store=general_store, stock=quantity)
            return JsonResponse({'status', 200})
        return JsonResponse({'status', 400})


class ProductDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
