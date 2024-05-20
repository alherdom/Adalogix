from django.urls import path

from .views import (
    LowStockProducts,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductList,
    ProductMultipleDelete,
    ProductUpdateView,
    ProductUploadFromCSV,
    ProductUpdateStockView,
)

app_name = 'product'

urlpatterns = [
    path('list/', ProductList.as_view(), name='product_list'),
    path('list/lowstock/', LowStockProducts.as_view(), name='product_list_low_stock'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('delete/multiple/', ProductMultipleDelete.as_view(), name='product_multiple_delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('upload/', ProductUploadFromCSV.as_view(), name='product_upload_csv'),
    path('update/stock/', ProductUpdateStockView.as_view(), name='update_inventory_stock'),
]
