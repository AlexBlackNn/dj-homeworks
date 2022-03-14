# # TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# # TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class DemoView(ListAPIView):
    sensor_1 = Sensor.objects.create(
        name='ESP32',
        description='Датчик на кухне за холодильником',
    )
    sensor_2 = Sensor.objects.create(
        name='ESP32',
        description='Датчик на балконе',
    )

    mesurement_1 = Measurement.objects.create(
        temperature=25,
        sensor=sensor_1,
    )

    mesurement_2 = Measurement.objects.create(
        temperature=30,
        sensor=sensor_2,
    )

    # откуда брать данные
    queryset = Sensor.objects.all()
    # c помощью чего будем сериализовывать
    serializer_class = SensorDetailSerializer

    # по умолчанию ListAPIView поддерживает только get запрос,
    # а post надо определить
    def post(self, request):
         return Response({'status': 'OK'})
#
# # class WeaponView(RetrieveAPIView):
# #     queryset = Weapon.objects.all()
# #     serializer_class = WeaponSerializer
#
# # @api_view(['GET', 'POST'])
# # def demo(request):
# #     if request.method == 'GET':
# #         Weapon.objects.create(power=10, rarity='epic', value=20)
# #         Weapon.objects.create(power=50, rarity='rare', value=200)
# #         Weapon.objects.create(power=1000, rarity='ooops', value=900)
# #         weapons = Weapon.objects.all()
# #
# #         ser = WeaponSerializer(weapons, many=True)
# #
# #         return Response(ser.data)
# #     if request.method == 'POST':
# #         return Response({'status': 'OK'})
#
# # class DemoView(APIView):
# #     def get(self,request):
# #         Weapon.objects.create(power=10, rarity='epic', value=20)
# #         Weapon.objects.create(power=50, rarity='rare', value=200)
# #         Weapon.objects.create(power=1000, rarity='ooops', value=900)
# #         weapons = Weapon.objects.all()
# #
# #         ser = WeaponSerializer(weapons, many=True)
# #         return Response(ser.data)
# #     def post(self,request):
# #         return Response({'status': 'OK'})