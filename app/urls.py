from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto'),
    path('agregar/', agregar, name='agregar'),
    path('listar/', listar, name='listar'),
    path('modificar/<int:pk>', modificar, name='modificar'),
    path('eliminar/<int:pk>', eliminar, name='eliminar'),
    
]
