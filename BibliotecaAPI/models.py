from django.db import models


#definición de la clase padre, en este caso la clase es libro
class Libro(models.Model):
    _codigoLibro = models.CharField(max_length=10,unique=True)
    _titulo = models.CharField(max_length=50,unique=True)
    _autor = models.CharField(max_length=50,)
    _anioPublicacion = models.DateField(null=True)
    
    def MostrarInfo(self):
        return f"codigo libro: {self._codigoLibro}, Titulo: {self._titulo}, Autor: {self._autor}, Año de Publicación: {self._anioPublicacion}"

    # Metodo get
    @property
    def GetCodigoLibro(self):
        return self._codigoLibro
    
    @GetCodigoLibro.setter
    def codigoLibro(self,value):
        if len(value)>10:
            raise ValueError("El código no puede tener más de 10 caracteres.")
        self._codigoLibro =value
    
    
    @property
    def GetTitulo(self):
        return self._titulo
    
    @GetTitulo.setter
    def titulo(self, value):
        if value < 0:
            raise ValueError("El titulo no puede tener más de 50 caracteres.")
        self._titulo=value
    
    @property
    def GetAutor(self):
        return self._autor
    
    @GetAutor.setter
    def autor(self, value):
        if value < 0:
            raise ValueError("El Autor no puede tener más de 50 caracteres.")
        self._autor=value
    
    @property
    def GetAnioPublicacion(self):
        return self._anioPublicacion
    
    @GetAnioPublicacion.setter
    def anioPublicacion(self, value):
        if value < 0:
            raise ValueError("El año de publiccion no puede ser D/M/A.")
        self._anioPublicacion=value
    

# Create your models here.

#Clase hija "LibroFisico" de clase padre "Libro"
class LibroFisico(Libro):
    _numeroPaginas = models.CharField(max_length=20)
        
    #Metodo Get
    @property
    def GetNumeroPaginas(self):
        return self._numeroPaginas
    
    @GetNumeroPaginas.setter
    def numeroPaginas(self, value):
        if value < 0:
            raise ValueError("El año de páginas no puede tener más de 50 caracteres.")
        self._numeroPaginas=value
    
    def MostrarInfo(self):
        return super().MostrarInfo() + f"Número de páginas: {self._numeroPaginas}"
    
    
    

#Clase hija "LibroDigital" de clase padre "Libro"
class LibroDigital(Libro):
    # Constructor de la clase hija
    _tamanomb = models.PositiveIntegerField()
    _formato = models.CharField(max_length=50)
            
    @property
    def GetTamanomb(self):
        return self._tamanomb
    
    @GetTamanomb.setter
    def tamanomb(self, value):
        if value < 0:
            raise ValueError("El tamaño MB no puede tener.")
        self._tamanomb=value
    
    @property
    def GetFormato(self):
        return self._formato
    
    @GetFormato.setter
    def formato(self, value):
        if value < 0:
            raise ValueError("El formato no es un número.")
        self._formato=value
    
    def MostrarInfo(self):
        return super().MostrarInfo() + f"Tamaño MB: {self._tamanomb}, Formato: {self._formato}"
# Create your models here.

# Create your models here.
