from django import forms
from app.models import Contacto, Producto


class ContactoForm(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Contacto
        fields = ['nombre','correo','tipo_consulta','mensaje','avisos']
        
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
    
        widgets = {
            "fecha_fabricacion":forms.SelectDateWidget()
        }
        
   