from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField(max_length=50)
    value = models.IntegerField()

