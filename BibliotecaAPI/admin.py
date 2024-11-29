from django.contrib import admin
from .models import Libro, LibroDigital, LibroFisico

# Register your models here.
admin.site.register(Libro)
admin.site.register(LibroFisico)
admin.site.register(LibroDigital)
