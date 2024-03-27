from django.urls import path

from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductMultipleDelete,
    ProductUpdateView,
)

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('delete/multiple/', ProductMultipleDelete.as_view(), name='product_multiple_delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]
