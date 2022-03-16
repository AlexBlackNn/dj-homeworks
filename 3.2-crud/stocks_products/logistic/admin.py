from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product, Stock

from .models import Stock, StockProduct, Product


class StockProductInline(admin.TabularInline):
    model = StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['pk','address']



