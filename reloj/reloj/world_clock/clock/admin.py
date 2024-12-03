from django.contrib import admin
from .models import Ciudad  # Cambia a Ciudad si corresponde

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'diferencia_horaria')
