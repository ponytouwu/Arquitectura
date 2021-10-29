from django.db import models
from django.contrib.auth.models import User

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.nombre_tipo

class Usuario(models.Model):
    num_run = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1,null=True)
    nombres_us = models.CharField(max_length=50,null=True)
    appellidos_us = models.CharField(max_length=50)
    fono_us = models.CharField(max_length=12)
    email_us = models.CharField(max_length=30,null=True)
    estatura_us = models.FloatField(null=True)
    edad = models.IntegerField(null=True)
    
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE)


    def __str__(self):
        return self.nombres_us

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    fecha_comp = models.DateField(null=True)
    numero_tick = models.IntegerField(null=True)
    estado_tick = models.CharField(max_length=10, null=True)

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.estado_tick        

class Tipo_atraccion(models.Model):
    id_tipo_atr = models.IntegerField(primary_key=True)
    nomb_tip_at = models.CharField(max_length=30,null=True) 

    def __str__(self):
        return self.nomb_tip_at

class Cola(models.Model):
    id_cola = models.IntegerField(primary_key=True)
    cantidad_us = models.IntegerField(null=True)
    tiempo_max = models.IntegerField(null=True)  

    def __str__(self):
        return self.cantidad_us 

class Atraccion(models.Model):
    id_atr = models.AutoField(primary_key=True)
    nombre_atr = models.CharField(max_length=20,null=True)
    capacidadd_atr = models.IntegerField(null=True)
    descrip_atr = models.CharField(max_length=200,null=True)
    tiempo_medio = models.IntegerField(null=True)
    estatura_min = models.FloatField(null=True)

    tipo_atraccion = models.ForeignKey(Tipo_atraccion, on_delete=models.CASCADE)
    cola = models.ForeignKey(Cola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_atr
