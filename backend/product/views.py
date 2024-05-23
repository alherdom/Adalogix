import json
from csv import DictReader
from django.db import transaction
from django.http import JsonResponse
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Inventory, Product, Store
from .serializers import ProductDetailSerializer


class ProductMultipleDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        product_ids = data['product_ids']
        for product_id in product_ids:
            Product.objects.get(id=product_id).delete()
        return JsonResponse({'status': 200})


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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'status': 200})


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


class ProductUpdateStockView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        data = json.loads(request.body)
        product_id = data['product_id']
        store_id = data['store_id']
        new_stock = data['new_stock']
        inventory = Inventory.objects.get(product=product_id, store=store_id)
        inventory.stock = new_stock
        inventory.save()
        return JsonResponse({'status': 200})


class ProductUploadFromCSV(APIView):
    def post(self, request):
        try:
            file_field_name = list(request.FILES.keys())[0]
            file = request.FILES[file_field_name]
            decoded_file = file.read().decode('utf-8')
            reader = DictReader(decoded_file.splitlines())

            required_fields = [
                'Id',
                'Store',
                'Name',
                'Description',
                'Quantity',
                'Category',
                'Price',
                'Weight',
                'Volume',
            ]

            with transaction.atomic():
                for row in reader:
                    missing_fields = [field for field in required_fields if field not in row]
                    if missing_fields:
                        return JsonResponse(
                            {'error': f'Missing fields in CSV file: {", ".join(missing_fields)}'},
                            status=400,
                        )
                    product, created = Product.objects.get_or_create(
                        id=row['Id'],
                        defaults={
                            'name': row['Name'],
                            'description': row['Description'],
                            'category': row['Category'],
                            'price': row['Price'],
                            'weight': row['Weight'],
                            'volume': row['Volume'],
                        },
                    )
                    try:
                        store = Store.objects.get(id=row['Store'])
                    except Store.DoesNotExist:
                        return JsonResponse(
                            {'error': f'Store with id {row["Store"]} does not exist'}, status=400
                        )
                    inventory, created = Inventory.objects.get_or_create(
                        product=product, store=store, defaults={'stock': row['Quantity']}
                    )
                    if not created:
                        inventory.stock += int(row['Quantity'])
                        inventory.save()
            return JsonResponse({'status': 200})
        except Exception as e:
            return JsonResponse(
                {'error': f'An error occurred while processing the file: {e}'}, status=500
            )


class LowStockProducts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products_to_return = []
        products = Product.objects.all()
        for product in products:
            quantity = sum(
                Inventory.stock for Inventory in Inventory.objects.filter(product=product)
            )
            if quantity <= 30:
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
