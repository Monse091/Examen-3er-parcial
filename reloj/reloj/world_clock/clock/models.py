from django.db import models
from datetime import datetime, timedelta

class Ciudad(models.Model): # Almacena el nombre y la diferencia horaria
    nombre = models.CharField(max_length=100) # nombre de la ciudad
    diferencia_horaria = models.IntegerField() # diferencia horaria (-12 a 12)

    def __str__(self):
        return self.nombre

class Reloj(models.Model): # Representa el reloj central
    
    hora_actual = models.DateTimeField(auto_now=True)

    def notificar_observadores(self, observadores):
        for observador in observadores:
            observador.actualizar(self.hora_actual)


class Ciudad(models.Model): # Aqui tambien se almacena el nombre y la diferencia de horario 
    
    nombre = models.CharField(max_length=100)  # Nombre de la ciudad
    diferencia_horaria = models.IntegerField()  # Diferencia horaria (-12 a 12)

    def __str__(self):
        return self.nombre


class HoraEn: # Observador que muestra la hora para una ciudad
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.hora_actualizada = None

    def actualizar(self, hora_central):
        # Ajusta la hora central según la diferencia horaria
        self.hora_actualizada = hora_central + timedelta(hours=self.ciudad.diferencia_horaria)

    def obtener_hora(self): # Devuelve la hora actualizada
        return f"{self.ciudad.nombre}, {self.hora_actualizada.strftime('%H:%M:%S')}"
