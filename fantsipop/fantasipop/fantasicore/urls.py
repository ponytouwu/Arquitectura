from django.contrib import admin
from django.urls import path, include
from .views import home, inicio, registro
urlpatterns = [
    path('home', home, name="home"),
    path('', inicio, name="inicio"),
    path('registro', registro, name="registro"),
]