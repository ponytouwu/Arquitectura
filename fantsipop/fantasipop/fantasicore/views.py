from django.shortcuts import render,redirect
from .models import Atraccion, Usuario, Tipo_usuario, User, Cola
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home (request):
    var_juegos = Atraccion.objects.all()
    usuarios = Usuario.objects.all()
    cola1 = Cola.objects.all()
    contexto = {
        'juegos' : var_juegos,
        'usuarios' : usuarios,
        'cola1' : cola1
    }
    return render(request, 'fantasicore/home.html',contexto)

def inicio (request):
    return render(request, 'fantasicore/inicio.html')
    
def registro (request):
    usuario = Usuario.objects.all()
    contexto ={
        "usuario":usuario

    }
    return render(request,'fantasicore/registro.html',contexto)

def juego (request,id):
    var_obt_game = Atraccion.objects.get(id_atr = id)
    contexto = {
        'juegoselec' : var_obt_game
    }
    return render(request, 'fantasicore/juego.html', contexto)

def registrar (request):
    nombre_u = request.POST['Nombre']
    apellidos_u = request.POST['Apellidos']
    rut_u = request.POST['Rut']
    dv_u = request.POST['dv']
    correo_u = request.POST['correo']
    Numero_u = request.POST['Numero']
    edad_u = request.POST['Edad']
    est_u = request.POST['est']
    pass_u = request.POST['pass']
    pass_u2 = request.POST['pass2']
    tip_u = request.POST['tipu']
    tip_o = Tipo_usuario.objects.get(id_tipo_usuario = tip_u)
    
   

    try:
        a= User.objects.get(username=rut_u )
        messages.error(request,'Nombre de usuario no disponible')
        return redirect('registro')

    except User.DoesNotExist:
        
        user1 = User.objects.create_user(rut_u, correo_u, pass_u)
        user1.first_name = nombre_u
        user1.last_name = apellidos_u
        user1.is_staff = 0
        user1.save() 
        if pass_u == pass_u2:
            Usuario.objects.create(num_run= rut_u,dv_run= dv_u,nombres_us=nombre_u,appellidos_us=apellidos_u,fono_us=Numero_u,email_us=correo_u,estatura_us=est_u,edad=edad_u, clave=pass_u, tipo_usuario=tip_o)
            messages.success(request,'Usuario registrado')
        
            return redirect('home')
        else:
            messages.error(request,'La contraseña no coinside')    
            return redirect('registro')

    return render(request, 'fantasicore/registro.html')
 
def encolar(request):
    cantidad_us1 = request.POST['cantidad']
    tiempo_max1= request.POST['tiempo']
    atrac1 = request.POST['id_atrac']
    atrac2 = Atraccion.objects.get(id_atr=atrac1)
    user1 = request.POST['id_user']
    user2 = Usuario.objects.get(num_run = user1)
    Cola.objects.create(cantidad_us=cantidad_us1 ,tiempo_max=tiempo_max1 ,usuario=user2 , atraccion=atrac2)

    return redirect(home)

def form_login(request):
    usuario = Usuario.objects.all()
    contexto ={
        "usuario":usuario
    }
    return render(request,'fantasicore/inicio.html',contexto)

def login_view(request):
    username_u = request.POST['Rut']
    password_u = request.POST['Contraseña']
    user= authenticate(username = username_u, password = password_u)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request,'Bienvenido '+username_u+ ', has iniciado sesion ')
            return redirect('home')
        else:
            messages.error(request,'Usuario inactivo')
    else:
        messages.error(request,'El nombre de usuario y la contraseña que ingresaste no coinciden con nuestros registros. Por favor, revisa e inténtalo de nuevo.')
    return redirect('login')

def logout_view(request):

    logout(request)

    return redirect('inicio') 