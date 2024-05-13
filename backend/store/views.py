from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import StoreListSerializer
from .models import Store


class StoreListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class StoreDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class ProductStoreView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreListSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Store.objects.filter(products__id=product_id)
