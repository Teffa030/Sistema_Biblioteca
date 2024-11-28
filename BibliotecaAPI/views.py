from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import LibroFisico, LibroDigital
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import LibroForm

# Vista principal que carga la página con el CRUD
def index(request):
    return render(request, 'libro/index.html')

# Vista para crear un evento (Concierto o Conferencia)
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            codigoLibro = form.cleaned_data['codigoLibro']
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            anioPublicacion = form.cleaned_data['anioPublicacion']
            tipo_libro = form.cleaned_data['tipo_libro']

            # Crear el evento según el tipo seleccionado
            if tipo_libro == 'fisico':
                numeroPaginas = form.cleaned_data['numeroPaginas']
                LibroFisico.objects.create(
                    codigoLibro=codigoLibro, titulo=titulo, autor=autor,
                    anioPublicacion=anioPublicacion, numeroPaginas=numeroPaginas
                )
            elif tipo_libro == 'digital':
                tamanomb = form.cleaned_data['tamanomb']
                formato = form.cleaned_data['formato']
                LibroDigital.objects.create(
                    codigoLibro=codigoLibro, titulo=titulo, autor=autor,
                    anioPublicacion=anioPublicacion, tamanomb=tamanomb, formato=formato 
                )
            return redirect('list_libro')  # Redirigir después de guardar el evento
    else:
        form = LibroForm()

    return render(request, 'libro/index.html', {'form': form})

# Vista para listar eventos (Conciertos y Conferencias)
def list_libro(request):
    # Obtener los conciertos y conferencias
    Fisicos = LibroFisico.objects.all()
    Digitales = LibroDigital.objects.all()

    libros = []

    # Agregar libro fisico a la lista de eventos
    for Fisico in Fisicos:
        libro = {
            'tipo_libro': 'fisico',  # Se agrega el tipo de evento explícitamente
            'codigoLibro': Fisico.codigoLibro,
            'titulo': Fisico.titulo,
            'autor': Fisico.autor,
            'anioPublicacion': Fisico.anioPublicacion,
            'numeroPaginas': Fisico.numeroPaginas
        }
        libros.append(libro)

    # Agregar conferencias a la lista de eventos
    for Digital in Digitales:
        libro = {
            'tipo_libro': 'digital',  # Se agrega el tipo de evento explícitamente
            'codigoLibro': Digital.codigoLibro,
            'titulo': Digital.titulo,
            'autor': Digital.autor,
            'anioPublicacion': Digital.anioPublicacion,
            'tamanomb': Digital.tamanomb,
            'formato': Digital.formato
        }
        libros.append(libro)

    return JsonResponse(libros, safe=False)

# Vista para actualizar un evento
@csrf_exempt
def update_libro(request, pk):
    if request.method == 'PUT':
        # Intentar obtener el evento como un Concierto o Conferencia
        try:
            libro = LibroFisico.objects.get(pk=pk)
            libro_tipo = 'fisico'
        except LibroFisico.DoesNotExist:
            libro = get_object_or_404(LibroFisico, pk=pk)
            libro_tipo = 'digital'

        data = json.loads(request.body)

        # Actualizar campos comunes
        libro.codigoLibro = data.get('codigoLibro', libro.codigoLibro)
        libro.titulo = data.get('titulo', libro.titulo)
        libro.autor = data.get('autor', libro.autor)
        libro.anioPublicacion = data.get('anioPublicacion', libro.anioPublicacion)

        # Actualizar campos específicos de libro físico o libro digital
        if libro_tipo == 'fisico':
            libro.numeroPaginas = data.get('numeroPaginas', libro.numeroPaginas)
        else:  # Si es libro digital
            libro.tamanomb = data.get('tamanomb', libro.tamanomb)
            libro.formato = data.get('formato', libro.formato)

        libro.save()

        return JsonResponse({'message': 'Libro actualizado con éxito', 'libro': libro.codigoLibro})


# Vista para eliminar un libro
@csrf_exempt
def delete_libro(request, pk):
    if request.method == 'DELETE':
        # Intentar obtener el libro como un Libro Físico o Libro Digital
        try:
            libro = LibroFisico.objects.get(id=pk)
        except LibroFisico.DoesNotExist:
            libro = get_object_or_404(LibroDigital, id=pk)
        libro.delete()
        return JsonResponse({'message': 'Libro eliminado con éxito'})