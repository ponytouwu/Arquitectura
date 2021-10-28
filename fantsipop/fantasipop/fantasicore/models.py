from django.db import models

class Tipo_usuario(models.Model):
    id_tipo_usuario = model.AutoField(primary_key=True)
    nombre_tip = models.CharField(max_length=30)

    def _str_(self):
        return self.nombre

class Usuario(models.Model):
    num_run = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1,null=True)