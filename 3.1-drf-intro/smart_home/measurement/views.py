# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weapon
from .serializers import WeaponSerializer


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         Weapon.objects.create(power=10, rarity='epic', value=20)
#         Weapon.objects.create(power=50, rarity='rare', value=200)
#         Weapon.objects.create(power=1000, rarity='ooops', value=900)
#         weapons = Weapon.objects.all()
#
#         ser = WeaponSerializer(weapons, many=True)
#
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})

# class DemoView(APIView):
#     def get(self,request):
#         Weapon.objects.create(power=10, rarity='epic', value=20)
#         Weapon.objects.create(power=50, rarity='rare', value=200)
#         Weapon.objects.create(power=1000, rarity='ooops', value=900)
#         weapons = Weapon.objects.all()
#
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     def post(self,request):
#         return Response({'status': 'OK'})


class DemoView(ListAPIView):
    Weapon.objects.create(power=10, rarity='epic', value=20)
    Weapon.objects.create(power=50, rarity='rare', value=200)
    Weapon.objects.create(power=1000, rarity='ooops', value=900)

    # откуда брать данные
    queryset = Weapon.objects.all()
    # c помощью чего будем сериализовывать
    serializer_class = WeaponSerializer

    # по умолчанию ListAPIView поддерживает только get запрос,
    # а post надо определить

    def post(self, request):
         return Response({'status': 'OK'})

class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer