from django.urls import path
from . import views

app_name = 'shop_api'

urlpatterns = [
    path('products/',
         views.ProductListSerializer.as_view(),
         name='product_list'),
    path('products/<pk>',
         views.ProductDetailSerializer.as_view(),
         name='product_detail'),
]