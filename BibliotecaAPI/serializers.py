
from rest_framework import serializers
from .models import LibroFisico, LibroDigital # Asegúrate de importar el modelo correspondiente

# Serializador para la API
class LibroFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroFisico
        fields = '__all__'
       

class LibroDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDigital
        fields = '__all__'
        