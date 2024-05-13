import json
from csv import DictReader

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

from .models import Inventory, Product, Store
from .serializers import ProductDetailSerializer, ProductListSerializer


class ProductMultipleDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        product_ids = data['product_ids']
        for product_id in product_ids:
            Product.objects.get(id=product_id).delete()
        return JsonResponse({'status': 200})


class ProductListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products_to_return = []
        products = Product.objects.all()
        for product in products:
            quantity = sum(
                Inventory.stock for Inventory in Inventory.objects.filter(product=product)
            )
            stores = []
            for store in product.stores.all():
                store_info = {}
                store_info['id'] = store.id
                store_info['name'] = store.name
                store_info['quantity'] = Inventory.objects.get(
                    product=product.id, store=store.id
                ).stock
                store_info['address'] = store.address
                stores.append(store_info)
            products_to_return.append(
                {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'quantity': quantity,
                    'category': product.category,
                    'price': product.price,
                    'weight': product.weight,
                    'volume': product.volume,
                    'stores': json.dumps(stores),
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

    def patch(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse(dict(status=200, message='Product successfully updated'))


class ProductUploadFromCSV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_field_name = list(request.FILES.keys())[0]
        file = request.FILES[file_field_name]
        decoded_file = file.read().decode('utf-8')
        reader = DictReader(decoded_file.splitlines())
        general_store = Store.objects.get(id=1)
        for row in reader:
            print(row)
            new_product = Product.objects.create(
                name=row['Name'],
                description=row['Description'],
                price=row['Price'],
                category=row['Category'],
                weight=row['Weight'],
                volume=row['Volume'],
            )
            Inventory.objects.create(
                product=new_product, store=general_store, stock=row['Quantity']
            )
        return JsonResponse({'status': 200})


class LowStockProducts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products_to_return = []
        products = Product.objects.all()
        for product in products:
            quantity = sum(
                Inventory.stock for Inventory in Inventory.objects.filter(product=product)
            )
            if quantity <= 15:
                stores = []
                for store in product.stores.all():
                    store_info = {}
                    store_info['id'] = store.id
                    store_info['name'] = store.name
                    store_info['quantity'] = Inventory.objects.get(
                        product=product.id, store=store.id
                    ).stock
                    store_info['address'] = store.address
                    stores.append(store_info)
                products_to_return.append(
                    {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'quantity': quantity,
                        'category': product.category,
                        'price': product.price,
                        'weight': product.weight,
                        'volume': product.volume,
                        'stores': json.dumps(stores),
                    }
                )
        return JsonResponse(products_to_return, safe=False)
