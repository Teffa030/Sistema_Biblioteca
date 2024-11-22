# urls.py (API)
from django.urls import path
from . import views

urlpatterns = [
    #url para LibroFisico
    path('index/',views.index, name='Index'),
    path('libro_fisico/', views.libro_fisico_list, name='LibroFisicoList'),
    path('libro_fisico/<int:pk>/', views.libro_fisico_detail, name='LibroFisicoDetail'),
    path('libro_fisico/add/', views.libro_fisico_create, name='LibroFisicoCreate'),
    path('libro_fisico/<int:pk>/', views.libro_fisico_update, name='LibroFisicoUpdate'),
    path('libro_fisico/<int:pk>/', views.libro_fisico_delete, name='LibroFisicoDelete'),
    
    #url para LibroDigital
    path('libro_digital/', views.libro_digital_list, name='LibroDigitalList'),
    path('libro_digital/<int:pk>/', views.libro_digital_detail, name='LibroDigitalDetail'),
    path('libro_digital/add/', views.libro_digital_create, name='LibroDigitalCreate'),
    path('libro_digital/<int:pk>/', views.libro_digital_update, name='LibroDigitalUpdate'),
    path('libro_digital/<int:pk>/', views.libro_digital_delete, name='LibroDigitalDelete'),
]