from django.urls import path

from .views import SensorsView, SensorDetailView, AddMeasurements

urlpatterns = [
     path('sensors/', SensorsView.as_view() ),
     path('sensors/<pk>', SensorDetailView.as_view() ),
     path('measurements/', AddMeasurements.as_view()),
 ]
