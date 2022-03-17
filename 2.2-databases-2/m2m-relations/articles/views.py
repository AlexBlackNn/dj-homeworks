from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    for article in object_list:
        # print(article)
        for scope in article.scopes.all():
            print(scope.is_main)
            print(scope.scope)
    context = {'object_list': object_list}
    return render(request, template, context)
