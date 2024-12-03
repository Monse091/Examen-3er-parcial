from django.shortcuts import render
from datetime import datetime
from .models import Reloj, Ciudad, HoraEn

def Aplicacion(request):
    # Crear una instancia de reloj
    reloj = Reloj.objects.create()

    # Obtener todas las ciudades
    ciudades = Ciudad.objects.all()

    # Crear observadores para cada ciudad
    observadores = [HoraEn(ciudad) for ciudad in ciudades]

    # Notificar a los observadores
    reloj.notificar_observadores(observadores)

    # Obtener las horas actualizadas
    horas_actualizadas = [observador.obtener_hora() for observador in observadores]

    # Renderizar los datos en la plantilla
    return render(request, "clock/reloj_mundial.html", {"horas_actualizadas": horas_actualizadas})
