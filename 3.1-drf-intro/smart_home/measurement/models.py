from django.db import models


class Sensor(models.Model):
    """Объект на котором проводят измерения."""
    name = models.TextField()
    description = models.TextField(blank=True)


class Measurement(models.Model):
    """Измерение температуры на объекте."""

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