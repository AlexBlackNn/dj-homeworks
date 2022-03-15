from django.urls import path

from .views import SensorsInfoView,SensorDetailInfoView

urlpatterns = [
     # TODO: зарегистрируйте необходимые маршруты
     path('sensors-info/', SensorsInfoView.as_view() ),
     path('sensor-detail-info/<pk>', SensorDetailInfoView.as_view() )
 ]
