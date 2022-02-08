from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def show_recipe_view(request, recipe_name):
    """Выдает рецепты"""
    servings = int(request.GET.get('servings', 1))
    context = {'recipe_name': DATA.get(recipe_name, {}).copy()}
    print(context)
    for key, values in context['recipe_name'].items():
        context['recipe_name'][key] = values * servings
    print(DATA.get(recipe_name))
    return render(request, 'calculator/index.html', context)


def index(request):
    """Главная страница"""
    return HttpResponse(f'Главная страница')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
