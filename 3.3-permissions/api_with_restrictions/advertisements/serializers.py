from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context["request"].user
        total_open_posts = user.advertisements.filter(status='OPEN').count()
        # чтобы работал PATCH, для закрытия объявлений, длокируем только post
        print(self.context["request"].method)
        if self.context["request"].method == 'POST':
            if total_open_posts == 10:
                raise serializers.ValidationError(
                    "Всего может быть открыто одновременно"
                    "только 10 объявлений."
                )
        return data
