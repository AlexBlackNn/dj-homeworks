from django.http import JsonResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import GetInfoSerializer, SensorDetailSerializer


class SensorsView(ListAPIView):
    """
    GET -> Получить список датчиков.Выдается список с краткой информацией по
    датчикам: ID, название и описание.

    POST -> Cоздать новый датчик
    """

    # откуда брать данные
    queryset = Sensor.objects.all()
    # c помощью чего будем сериализовывать
    serializer_class = GetInfoSerializer

    # по умолчанию ListAPIView поддерживает только get запрос,
    # а для создания новой стркои в БД post надо определить
    def post(self, request):
        Sensor.objects.create(
                name=request.data['name'],
                description=request.data['description'],
        )
        return Response({'status': 'OK'})

class SensorDetailView(RetrieveAPIView):
    """
    GET -> Получить информацию по конкретному датчику. Выдается полная информация
    по датчику: ID, название, описание и список всех измерений с
    температурой и временем.

    PATCH -> Изменить данные датчика.
    """

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def get_object(self):
        pk = str(self.kwargs['pk'])
        sensor = Sensor.objects.get(pk=pk)
        return sensor

    def patch(self, request, pk):
        sensor = self.get_object()
        serializer = GetInfoSerializer(
            sensor,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)

class AddMeasurements(APIView):
    def post(self, request):
        sensor_id = request.data['sensor']
        sensor = Sensor.objects.get(pk=sensor_id)
        Measurement.objects.create(
            temperature=request.data['temperature'],
            sensor=sensor
        )
        return Response({'status': 'OK'})

        # serializer = SensorDetailSerializer(
        #     sensor,
        #     data=request.data,
        #     partial=True,
        # )
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(data=serializer.data)