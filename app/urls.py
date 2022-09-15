from django.urls import path, include
from .views import *
from rest_framework import routers 

router = routers.DefaultRouter() # nos permite crear las url necesarias para nuestra api, 
# el router crea las url para add,edite,change,delete (crud) y se pasan por el path de abajo (localhost:8000/api/producto
router.register('producto', ProductoViewset) # entidad 

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto'),
    path('agregar/', agregar, name='agregar'),
    path('listar/', listar, name='listar'),
    path('modificar/<int:pk>', modificar, name='modificar'),
    path('eliminar/<int:pk>', eliminar, name='eliminar'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)), # se registra en el path y se coloca el include
    
    
]
