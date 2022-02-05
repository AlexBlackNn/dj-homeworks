from __future__ import annotations
from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir, getcwd
from datetime import datetime
from tzlocal import get_localzone


def home_view(request):
    template_name: str = 'app/home.html'
    pages: dict[str, str] = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': 'workdir'
    }
    context: dict[str, dict] = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    """Возвращает текущее время."""
    current_time: datetime = datetime.now().astimezone()
    current_time = current_time.strftime('%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    """Возвращает получения списка файлов в рабочей директории."""
    listdir_of_cwd = str(listdir(getcwd()))
    return HttpResponse(listdir_of_cwd)
