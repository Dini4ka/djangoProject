from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('страница приложения myself')


def categories(request,resumeid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Мои достижения</h1><p>{resumeid}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')