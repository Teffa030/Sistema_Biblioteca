from .models import LibroFisico, LibroDigital
from rest_framework import viewsets, permissions  # Importa las vistas de Django REST Framework
# from rest_framework.permissions import IsAuthenticated,   # Permiso para autenticación
from .serializers import LibroFisicoSerializer, LibroDigitalSerializer  # Corrige el nombre del archivo


class LibroFisicoViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar los conciertos (CRUD).
    """
    queryset = LibroFisico.objects.all()  # Consulta todos los conciertos
    serializer_class = LibroFisicoSerializer  # Usa el serializador de conciertos
    permission_classes = [permissions.AllowAny]  # Solo accesible por usuarios autenticados

class LibroDigitalViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar las conferencias (CRUD).
    """
    queryset = LibroDigital.objects.all()  # Consulta todas las conferencias
    serializer_class = LibroDigitalSerializer  # Usa el serializador de conferencias
    permission_classes = [permissions.AllowAny]  # Solo accesible por usuarios autenticados
    # permission_classes = [IsAuthenticated]  # Solo accesible por usuariospermissions.AllowAny