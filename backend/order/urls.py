from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('delete/multiple/', views.OrderMultipleDelete.as_view(), name='order_multiple_delete'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('courier/delete/<int:pk>/', views.OrderCourierDelete.as_view(), name='order_courier_delete'),
]
