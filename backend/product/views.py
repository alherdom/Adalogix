import json

from django.http import JsonResponse
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Inventory, Product
from .serializers import ProductDetailSerializer, ProductListSerializer


class ProductMultipleDelete(APIView):
    def delete(self, request):
        data = json.loads(request.body)
        product_ids = data["ID's"]
        for product_id in product_ids:
            Product.objects.get(id=product_id).delete()
        return JsonResponse({'deleted': 'true'})


class ProductListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


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
                    'pirce': product.price,
                    'weight': product.weight,
                    'volume': product.volume,
                }
            )
        return JsonResponse(products_to_return, safe=False)


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
