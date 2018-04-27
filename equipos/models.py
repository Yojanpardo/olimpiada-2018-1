from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Equipo(models.Model):
    serial = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    estado = models.TextField(max_length=500)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def get_absolut_url(self):
        return reverse('details', kwargs={'slug':self.slug})

    def __str__(self):
        return self.tipo

class LogSolicitud(models.Model):
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    equipo = models.ForeignKey(
        'equipos.Equipo',
        on_delete = models.CASCADE,
    )
    estudiante = models.ForeignKey(
        'estudiantes.Estudiante',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return 'equipo {} solicitado'.format(self.equipo)
