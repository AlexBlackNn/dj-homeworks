from django.urls import path

from .views import DemoView

urlpatterns = [
     # TODO: зарегистрируйте необходимые маршруты
     path('', DemoView.as_view()),
     # path('weapon/<pk>/',WeaponView.as_view() )
 ]
