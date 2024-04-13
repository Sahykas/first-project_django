import django.http
from django.shortcuts import render, reverse
import time
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = time.ctime(time.time())
    msg = f'Текущее время: {current_time}'
    return django.http.HttpResponse(msg)


def workdir_view(request):
    dir_file = ''
    for name in os.listdir():
        dir_file = dir_file + '<br>' + name
    return django.http.HttpResponse(dir_file)
