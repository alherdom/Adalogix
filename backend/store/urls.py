from django.urls import path
from .views import StoreListView, ProductStoreView, ProductStoreInventoryView

app_name = 'store'

urlpatterns = [
    path('list/', StoreListView.as_view(), name='store_list'),
    path('product/', ProductStoreView.as_view(), name='store_product_list'),
    path('detail/<int:pk>/', ProductStoreInventoryView.as_view(), name='inventory_product_list')
]
