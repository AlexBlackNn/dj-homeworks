from django.contrib import admin

from .models import Article, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'text', 'published_at', 'image']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['is_main', 'tag']
