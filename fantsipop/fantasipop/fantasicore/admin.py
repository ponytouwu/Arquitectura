from django.contrib import admin
from .models import Cola, Atraccion, Ticket, Tipo_atraccion, Tipo_usuario, Usuario

# Register your models here.

admin.site.register(Cola)
admin.site.register(Atraccion)
admin.site.register(Ticket)
admin.site.register(Tipo_atraccion)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
