from rest_framework import routers
from django.urls import path, include  # Asegúrate de importar 'include'
from . import views
from .api import LibroFisicoViewSet, LibroDigitalViewSet

# Registrar las vistas para la API
router = routers.DefaultRouter()
router.register('Fisico', LibroFisicoViewSet, 'Fisico')
router.register('Digital', LibroDigitalViewSet, 'Digital')

urlpatterns = [
    #url para LibroFisico
    path('', views.index, name='Index'),
    path('crear/', views.crear_libro, name='Create'),
    path('listar/', views.list_libro, name='List'),
    path('actualizar/<int:pk>/', views.update_libro, name='Update'),
    path('eliminar/<int:pk>/', views.delete_libro, name='Delete'),
    
    path('api/', include(router.urls))
]