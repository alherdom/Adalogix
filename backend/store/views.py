from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import StoreListSerializer
from .models import Store

class StoreListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer