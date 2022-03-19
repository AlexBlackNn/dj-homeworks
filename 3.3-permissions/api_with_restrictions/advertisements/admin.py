from django.contrib import admin

from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'description',
        'status',
        'creator',
        'created_at',
    ]
    list_editable = ('status',)