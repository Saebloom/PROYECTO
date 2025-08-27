from django.shortcuts import render
from django.http import HttpResponse

def miapp(request):
    return HttpResponse("<BR>Hello world!</BR>")

def acercade(request):
    return HttpResponse("Página acerca de...")

def index(request):
    return render(request, 'index.html')