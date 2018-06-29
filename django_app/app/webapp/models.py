import datetime

from django.db import models
from django.utils import timezone

class Extension(models.Model):
    id_extension = models.CharField(max_length=3, primary_key=True)
    extension = models.CharField(max_length=200)

    def __str__(self):
        return self.id_extension + " - " + self.extension

class Reservante(models.Model):
    nombre = models.TextField(max_length=200)
    email = models.EmailField()
    numero_telefono = models.CharField(max_length=8)
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    propietario = models.ForeignKey(Reservante, on_delete=models.CASCADE)
    clave = models.CharField(max_length=50)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def not_reservable(self):
        now = timezone.now()
        return self.fecha_reserva < now