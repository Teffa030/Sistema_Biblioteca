from django.db import models
from django.core.validators import MinValueValidator


class Libro(models.Model):
    codigoLibro = models.CharField(max_length=10, null= True)
    titulo = models.CharField(max_length=50, null= True)
    autor = models.CharField(max_length=50, null=True)
    anioPublicacion = models.DateField(null=True, blank=True)

    def MostrarInfo(self):
        return f"Código libro: {self.codigoLibro}, Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anioPublicacion}"

class LibroFisico(Libro):
    numeroPaginas = models.PositiveIntegerField(null=True)
    tipo_libro = models.CharField(default='fisico', max_length=10)

    def MostrarInfo(self):
        return super().MostrarInfo() + f", Número de páginas: {self.numeroPaginas}"

class LibroDigital(Libro):
    tamanomb = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    formato = models.CharField(max_length=50, null=True)
    tipo_libro = models.CharField(default='digital', max_length=10)

    def MostrarInfo(self):
        return super().MostrarInfo() + f", Tamaño MB: {self.tamanomb}, Formato: {self.formato}"


