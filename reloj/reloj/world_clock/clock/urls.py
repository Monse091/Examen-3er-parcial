from django.urls import path
from . import views

# URL patrones de la aplicacion
urlpatterns = [
    path('', views.Aplicacion, name='reloj_mundial'),
]
