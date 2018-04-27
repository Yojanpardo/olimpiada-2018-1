from django.contrib import admin
from equipos.models import *
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display=('tipo','fecha_ingreso',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(LogSolicitud)
