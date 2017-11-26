from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def new(request):
    return render(request, 'blog/login.html')
