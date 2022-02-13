import csv
from django.core.management.base import BaseCommand
from .models import Phone


class Command(BaseCommand):
    """Класс для инициализации БД из csv файла."""

    def add_arguments(self, parser):
        """Парсинг аргументов."""
        pass

    def handle(self, *args, **options):
        """Запись в базу данных."""
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug_name = phone['name'].replace(' ', '_').lower()
            phone = Phone(id=phone['id'],
                          name=phone['name'],
                          price=phone['price'],
                          image=phone['image'],
                          release_date=phone['release_date'],
                          lte_exists=phone['lte_exists'],
                          slug=slug_name, )
            phone.save()
