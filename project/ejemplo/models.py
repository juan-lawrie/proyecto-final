from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    #nacimiento = models.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Animales(models.Model):
  nombre_del_animal = models.CharField(max_length=60)  
  reino = models.CharField(max_length=60)
  clase= models.CharField(max_length=60)
  def __str__(self):
      return f"{self.nombre_del_animal}, {self.reino}, {self.clase}"

class Mascotas(models.Model):
  nombre_de_la_mascota= models.CharField(max_length=60)
  tipo_de_mascota= models.CharField(max_length=60)
  def __str__(self):
      return f"{self.nombre_de_la_mascota}, {self.tipo_de_mascota}"


