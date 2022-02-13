from django.contrib import admin

from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    """Настройка админки."""

    list_display = ('id',
                    'name',
                    'price',
                    'image',
                    'release_date',
                    'lte_exists',
                    'slug'
                    )
    # Позволит изменять поле group из списка постов
    list_editable = ('slug',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name', 'price')
    # Добавляем возможность фильтрации по дате
    list_filter = ('name', 'price')
    empty_value_display = '-пусто-'

admin.site.register(Phone, PhoneAdmin)
