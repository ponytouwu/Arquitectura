from django.contrib import admin
from django.urls import path, include
from .views import home, inicio, registro, juego,registrar,form_login,login_view,logout_view,encolar
urlpatterns = [
    path('home', home, name="home"),
    path('', inicio, name="inicio"),
    path('registro', registro, name="registro"),
    path('juego/<int:id>', juego, name="juego"),
    path('registrar', registrar, name="registrar"),
    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
    path('encolar', encolar, name="encolar")
]