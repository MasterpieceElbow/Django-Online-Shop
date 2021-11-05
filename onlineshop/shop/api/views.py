from rest_framework import generics
from ..models import Product
from .serializers import ProductSerializer


class ProductListSerializer(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailSerializer(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer