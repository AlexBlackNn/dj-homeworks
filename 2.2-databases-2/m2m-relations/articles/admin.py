from django.contrib import admin

from .models import Article, Scope, ArticleScope


class ArticleScopeInline(admin.TabularInline):
    model = Scope.article.through
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]
