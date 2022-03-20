from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope
from django.core.exceptions import ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            was_tag_main = form.cleaned_data['is_main']

            if 'article' in form.cleaned_data:
                for item in form.cleaned_data['article'].scopes.all():
                    if item.is_main == True and was_tag_main == True:
                        # вызовом исключения ValidationError можно указать админке о наличие ошибки
                        # таким образом объект не будет сохранен,
                        # а пользователю выведется соответствующее сообщение об ошибке
                        raise ValidationError('Уже есть основной тег.')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = Scope.article.through
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]
