# calculator/urls.py
from django.urls import path


from . import views

urlpatterns = [
    # Выдача ингредиентов
    path('',views.index),
    path('<slug:recipe_name>/', views.show_recipe_view),
]
