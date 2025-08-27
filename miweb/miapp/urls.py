from django.urls import path
from . import views

urlpatterns = [
    path('', views.miapp, name='miapp'),
    path('acercade/', views.acercade, name='acercade'),
    path('index/', views.index, name='index'),  # ← Nueva ruta
]