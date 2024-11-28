from django import forms
from django.core.validators import MinValueValidator
from .models import Libro,LibroFisico, LibroDigital

class LibroForm(forms.Form):
    tipo_libro = forms.ChoiceField(
        choices=[('LibroFisico', 'LibroFisico'), ('LibroDigital', 'librodigital')],
        widget=forms.RadioSelect,  # Muestra las opciones como botones de radio
        required=True
    )
    codigoLibro = forms.CharField(max_length=10)

    def clean_codigoLibro(self):
        codigo = self.cleaned_data.get('codigoLibro')
        if Libro.objects.filter(codigoLibro=codigo).exists():
            raise forms.ValidationError("El código del libro ya existe.")
        return codigo

    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    anioPublicacion = forms.DateField(required=False)

    # Campos específicos para LibroFisico (solo visibles cuando se selecciona "Concierto")
    numeroPaginas = forms.CharField(max_length=20)

    # Campos específicos para LibroDigital (solo visibles cuando se selecciona "Conferencia")
    tamanomb = forms.IntegerField(validators=[MinValueValidator(1)], required=False)
    formato = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        tipo_libro = cleaned_data.get('tipo_libro')

        # Validación para LibroFisico
        if tipo_libro == 'fisico':
            numeroPaginas = cleaned_data.get('numeroPaginas')
            if not numeroPaginas:
                raise forms.ValidationError("Debe ingresar el numero de paginas.")
        
        # Validación para LibroDigital
        elif tipo_libro == 'digital':
            tamanomb = cleaned_data.get('tamanomb')
            formato = cleaned_data.get('formato')
            if not tamanomb or not formato:
                raise forms.ValidationError("Debe ingresar el tamaño en mb y el formato para el libro digital.")
        
        return cleaned_data
        

    