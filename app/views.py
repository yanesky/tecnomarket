from django.shortcuts import render, redirect
from app.models import Marca, Producto
from app.forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {'test':productos})

def contacto(request):
    data = {
        
        'form' : ContactoForm(),
        'mensaje' : None
    }    
    if request.method == 'POST':
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            data['form'] = form
            return render(request, 'app/contacto.html', data)           
    else:
        data['form'] = ContactoForm

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar(request):
    data={

        'form' : ProductoForm(),

    }

    if request.method == 'POST':
        form = ProductoForm(data=request.POST, files= request.FILES)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            data['form'] = form
            return render(request, 'app/producto/agregar.html', data)
    else:
        return render(request, 'app/producto/agregar.html', data)
    
def listar(request):
    data = {
        'lista' : Producto.objects.all(),
    }
    
    return render(request, 'app/producto/listar.html', data )

def modificar(request,pk):
    
    data={

        'form' : ProductoForm()

    }

    if request.method == 'POST':
        form = ProductoForm(data=request.POST, files= request.FILES)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            data['form'] = form
            return render(request, 'app/producto/modificar.html', data)
    else:
        instancia = Producto.objects.get(id=pk)
        data['form']= ProductoForm(instance=instancia)
        return render(request, 'app/producto/modificar.html', data)

def eliminar(request):
    pass
    