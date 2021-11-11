from django.contrib import admin
from django.urls import path, include
from .views import home, inicio, registro, juego,registrar,form_login,login_view,eliminar_cola1,logout_view,encolar,eliminar_cola,escanear,buscar_elemento
urlpatterns = [
    path('home', home, name="home"),
    path('', inicio, name="inicio"),
    path('registro', registro, name="registro"),
    path('juego/<int:id>', juego, name="juego"),
    path('registrar', registrar, name="registrar"),
    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
    path('encolar', encolar, name="encolar"),
    path('escanear', escanear, name="escanear"),
    path('eliminar_cola/<int:id>', eliminar_cola, name= "eliminar_cola"),
    path('buscar_elemento', buscar_elemento, name= "buscar_elemento"),
    path('eliminar_cola1/<int:id>',eliminar_cola1 ,name= "eliminar_cola1" )
]