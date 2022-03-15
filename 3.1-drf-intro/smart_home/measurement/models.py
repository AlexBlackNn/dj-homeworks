from django.db import models


class Sensor(models.Model):
    """Датчик, который производит измерения."""
    name = models.TextField()
    description = models.TextField(blank=True)


class Measurement(models.Model):
    """Измерения датчика."""

    temperature = models.FloatField()
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
