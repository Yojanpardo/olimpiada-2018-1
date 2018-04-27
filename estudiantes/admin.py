from django.contrib import admin
from estudiantes.models import *
# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display=('nombre',)

admin.site.register(Estudiante, EstudianteAdmin)
