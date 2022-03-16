from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product, Stock

class ProductAdmin(admin.ModelAdmin):
    """Настройка админки."""

    list_display = ('title',
                    'description',
                    )
admin.site.register(Product, ProductAdmin)

class StockAdmin(admin.ModelAdmin):
    """Настройка админки."""

    list_display = ('address',
                    )
admin.site.register(Stock, StockAdmin)