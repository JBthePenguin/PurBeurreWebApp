from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('id', 'product_name', 'brands', 'code')
    list_display = ('id', 'product_name', 'brands', 'code')
