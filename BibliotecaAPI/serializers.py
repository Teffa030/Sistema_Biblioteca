
from rest_framework import serializers
from django import forms
from .models import LibroFisico, LibroDigital # Asegúrate de importar el modelo correspondiente

# Serializador para la API
class LibroFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroFisico
        fields = ['_codigoLibro', '_titulo', '_autor', '_anioPublicacion', '_numeroPaginas']

# Formulario para el manejo en Django Forms
class LibroFisicoForm(forms.ModelForm):
    class Meta:
        model = LibroFisico
        fields = ['_codigoLibro', '_titulo', '_autor', '_anioPublicacion', '_numeroPaginas']
       

class LibroDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDigital
        fields = ['_codigoLibro', '_titulo','_autor','_anioPublicacion', '_tamanomb', '_formato']
        
class LibroDigitalForm(forms.ModelForm):
    class Meta:
        model = LibroDigital
        fields = ['_codigoLibro', '_titulo', '_autor', '_anioPublicacion', '_tamanomb','_formato']