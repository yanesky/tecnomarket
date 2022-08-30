from django.shortcuts import render
from app.models import Marca, Producto

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {'test':productos})

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')
