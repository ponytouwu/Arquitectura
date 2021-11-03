from django.shortcuts import render
from .models import Atraccion

# Create your views here.

def home (request):
    var_juegos = Atraccion.objects.all()
    contexto = {
        'juegos' : var_juegos
    }
    return render(request, 'fantasicore/home.html',contexto)

def inicio (request):
    return render(request, 'fantasicore/inicio.html')
    
def registro (request):
    return render(request, 'fantasicore/registro.html')

def juego (request,id):
    var_obt_game = Atraccion.objects.get(id_atr = id)
    contexto = {
        'juegoselec' : var_obt_game
    }
    return render(request, 'fantasicore/juego.html', contexto)
