from django.urls import path
from . import views
app_name = 'order'

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create')
]