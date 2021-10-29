from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'fantasicore/home.html')

def inicio (request):
    return render(request, 'fantasicore/inicio.html')
    
def registro (request):
    return render(request, 'fantasicore/registro.html')
