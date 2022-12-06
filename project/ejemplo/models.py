from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    #nacimiento = models.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

