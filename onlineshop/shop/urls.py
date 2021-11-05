from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    path('category/<slug:slug>/', views.list_by_category, name='list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.category_list, name='category_list'),
    path('search/', views.category_product_search, name='category_product_search'),

]
