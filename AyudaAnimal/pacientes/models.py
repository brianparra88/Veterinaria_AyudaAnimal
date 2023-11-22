from django.db import models

# Create your models here.
class Pacientes(models.Model):
    nombre_mascota = models.CharField(max_length=20)
    especie_mascota = models.CharField(max_length=20)
    raza_mascota = models.CharField(max_length=20)
    edad_mascota = models.IntegerField()
    nombre_dueno = models.CharField(max_length=20)
    rut_dueno = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre_mascota}, Dueño: {self.nombre_dueno}, Especie: {self.especie_mascota}, Raza: {self.raza_mascota}, Edad: {self.edad_mascota}, Rut dueño: {self.rut_dueno}"