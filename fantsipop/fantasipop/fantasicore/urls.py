from django.contrib import admin
from django.urls import path, include
from .views import home, inicio
urlpatterns = [
    path('', home, name="home"),
    path('inicio', inicio, name="inicio"),
]