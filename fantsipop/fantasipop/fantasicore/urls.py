from django.contrib import admin
from django.urls import path, include
from .views import home, inicio, registro, juego
urlpatterns = [
    path('home', home, name="home"),
    path('', inicio, name="inicio"),
    path('registro', registro, name="registro"),
    path('juego/<int:id>', juego, name="juego"),
]