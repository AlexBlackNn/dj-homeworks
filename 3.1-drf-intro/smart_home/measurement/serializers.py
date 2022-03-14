from rest_framework import serializers

from .models import Weapon

# TODO: опишите необходимые сериализаторы
# class WeaponSerializer(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['pk', 'power', 'rarity']