from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'active']
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available', 'created']
    list_filter = ['available']
    list_editable = ['available']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}