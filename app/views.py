from django.shortcuts import render, redirect, get_object_or_404
from app.models import Marca, Producto
from app.forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

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
            messages.success(request,'Agregado Correctamente')
            return redirect(to='listar')
        else:
            data['form'] = form
            return render(request, 'app/producto/agregar.html', data)
    else:
        return render(request, 'app/producto/agregar.html', data)
    
def listar(request):
    productos =Producto.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
        
    except:
        
        raise Http404
    
    data = {
        'entity' : productos,
        'paginator':paginator
    }
    
    return render(request, 'app/producto/listar.html', data )

def modificar(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        form = ProductoForm(data= request.POST, files = request.FILES, instance= producto)
        if form.is_valid():
            form.save()
            messages.success(request,'Modificado Correctamente')
            return redirect(to='listar')
        data['form'] = form
    return render(request, 'app/producto/modificar.html',data)            
    
    
    
def eliminar(request,pk):
    borrar = Producto.objects.get(pk=pk)
    borrar.delete()
    messages.success(request,'Eliminado Correctamente')
    return redirect('listar')


def registro(request):
    data = {
        'form': CustomUserCreationForm
    } 
    if request.method== 'POST':
        formulario = CustomUserCreationForm(data= request.POST)
        if formulario.is_valid:
            formulario.save()
            user = authenticate(username = formulario.cleaned_data['username'], password= formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado Correctamente')
            return redirect('home')
        else:
            print('hola3')
            data['form']= formulario
    return render(request, 'registration/registro.html', data)


    
    