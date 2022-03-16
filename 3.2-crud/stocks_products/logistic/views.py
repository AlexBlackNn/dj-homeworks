from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


# class ProductViewSet(ViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # при необходимости добавьте параметры фильтрации
#
#     def list(self,request):
#         """Перечисление продуктов"""
#         return Response({'status':'ok'})
#
#     def retrive(self,request):
#         """Вывод кокретного продукта"""
#         return Response({'status': 'ok'})
#
#     def destroy(self,request):
#         """"Удаление кокретного продукта"""
#         return Response({'status': 'ok'})
#
#     def update(self,request):
#         """Обновление продукта"""
#         return Response({'status': 'ok'})
#
#     def create(self, request:
#         """Создание продукта"""
#         return Response({'status': 'ok'})

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend, # для поиска через get запрос(/?param=)
        SearchFilter, # для поиска по тексту
        OrderingFilter,  # упорядочевание вывода
    ]
    filterset_fields = ['title']
    # при необходимости добавьте параметры фильтрации
    search_fields = ['description']
    ordering_fields = ['title', 'id']
    pagination_class = LimitOffsetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
