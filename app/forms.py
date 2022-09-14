from django import forms
from app.models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.core import validators
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Contacto
        fields = ['nombre','correo','tipo_consulta','mensaje','avisos']
        
        
class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)]) # ojo en el modelo debe ser null=True
    precio = forms.IntegerField(min_value= 1, max_value=14000)
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError('esta duplicado este nombre')
        return nombre
    
    class Meta:
        model = Producto
        fields = '__all__'
    
        widgets = {
            "fecha_fabricacion":forms.SelectDateWidget()
        }
        
class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(required=False, validators=[ validators.MinLengthValidator(3, 'El titulo es demasiado corto'),
        validators.MaxLengthValidator(20, 'El titulo sobrepasa mucho texto')])
    first_name = forms.CharField(required=False, validators=[ validators.MinLengthValidator(3, 'El nombre es demasiado corto'),
        validators.MaxLengthValidator(20, 'El nombre sobrepasa mucho texto')])
    last_name = forms.CharField(required=False, validators=[ validators.MinLengthValidator(3, 'El apellido es demasiado corto'),
        validators.MaxLengthValidator(20, 'El apellido sobrepasa mucho texto')])
    email = forms.EmailField(validators=[validators.EmailValidator])
    
    class Meta:
        model=User
        fields = ['username','first_name','last_name', 'email','password1','password2']
        