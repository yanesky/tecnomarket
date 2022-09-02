from mailbox import NoSuchMailboxError
from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50) 
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to='producto', null = True, blank= True)

    def __str__(self):
            return self.nombre
 
opciones_consulta = (
    (0, 'Consulta'),
    (1, 'Reclamo'),
    (2, 'sugerencia'),
    (3, 'Felicitaciones'),
) 
class Contacto(models.Model):
     nombre = models.CharField(max_length=50)
     correo = models.EmailField(unique=True)
     tipo_consulta = models.IntegerField(choices = opciones_consulta)
     mensaje = models.TextField()
     avisos = models.BooleanField()
     
     def __str__(self):
            return self.nombre
