from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto'),
]