from django.forms import ValidationError
#esto es para personalizar las validaciones
#validador como function 
#validador como clase

class MaxSizeFileValidator:

    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size
        
    def __call__(self, value): # inyecto lo que el usuario escriba en la caja, si es un archivo inyecta el archivo
        size = value.size
        max_size = self.max_file_size * 1048576
        if size > max_size:
            raise ValidationError(f'El tamano maximo del archivo debe ser de {self.max_file_size}MB')
        return value


