import json

from django.http import JsonResponse
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductDetailSerializer, ProductListSerializer


class ProductMultipleDelete(APIView):
    def delete(self, request):
        data = json.loads(request.body)
        product_ids = data["ID's"]
        for product_id in product_ids:
            Product.objects.get(id=product_id).delete()
        return JsonResponse({'deleted': 'true'})


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
