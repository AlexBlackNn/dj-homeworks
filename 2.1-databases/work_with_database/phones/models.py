from django.db import models


class Phone(models.Model):
    """Класс телефона"""
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)
