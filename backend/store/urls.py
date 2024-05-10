from django.urls import path
from .views import StoreListView

app_name = 'store'

urlpatterns = [
    path('list/', StoreListView.as_view(), name='store_list')
]