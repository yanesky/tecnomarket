from wsgiref.validate import validator
from .models import Producto, Marca
from rest_framework import serializers
from .validators import MaxSizeFileValidator


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    #nombre_marca = serializers.CharField(read_only=True, source='marca.nombre')
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca')
    nombre = serializers.CharField(required=True)
    imagen = serializers.ImageField(required=True, validators=[MaxSizeFileValidator(max_file_size=2)])
    
    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()
        if existe:
            raise serializers.ValidationError('Este producto ya existe')
        return value
    class Meta:
        model = Producto
        fields = '__all__'
        
        
