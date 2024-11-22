import requests
from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import Http404

# Vista que consume la API y pasa datos al template de LIBRO FISICO
def index(request):
    return render(request,'libro/index.html')

def libro_fisico_list(request):
    api_url = 'http://127.0.0.1:8000/api/libro_fisico/'  # URL de tu API
    response = requests.get(api_url)
    libros = response.json() if response.status_code == 200 else []  # Datos desde la API
    return render(request, 'libro/libro_fisico_list.html', {'libros': libros})


def libro_fisico_detail(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_fisico/{pk}/'  # Endpoint de detalle
    response = requests.get(api_url)
    if response.status_code == 200:  # Si la API devuelve un libro válido
        libro = response.json()
    else:
        raise Http404("El libro físico no existe.")
    return render(request, 'libro/libro_fisico_detail.html', {'libro': libro})


def libro_fisico_create(request):
    if request.method == 'POST':
        api_url = 'http://127.0.0.1:8000/api/libro_fisico/add/'
        data = {
            'titulo': request.POST['titulo'],
            'autor': request.POST['autor'],
            'anioPublicacion': request.POST['anioPublicacion'],
            'numeroPaginas':request.POST['numeroPaginas']
        }
        response = requests.post(api_url, data=data)
        if response.status_code == 201:  # Creación exitosa
            return redirect('LibroFisicoList')
    return render(request, 'libro/libro_fisico_form.html')

def libro_fisico_update(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_fisico/{pk}/'  # URL de la API para un libro específico

    if request.method == 'POST':
        data = {
            'titulo': request.POST['titulo'],
            'autor': request.POST['autor'],
            'anioPublicacion': request.POST['anioPublicacion'],
            'numeroPaginas': request. POST['numeroPaginas']
        }
        response = requests.put(api_url, data=data)  # Llamada a la API para actualizar
        if response.status_code == 200:  # Actualización exitosa
            return redirect('LibroFisicoList')
    else:
        response = requests.get(api_url)  # Obtener los datos del libro desde la API
        if response.status_code == 200:
            libro = response.json()
        else:
            libro = None  # Manejar caso en que no se encuentre el libro

    return render(request, 'libro/libro_fisico_form.html', {'libro': libro})

def libro_fisico_delete(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_fisico/{pk}/'
    
    if request.method == 'POST':
        response = requests.delete(api_url)
        if response.status_code == 204:  # Eliminación exitosa
            return redirect('LibroFisicoList')
    
    # Obtener los datos del libro para confirmación antes de eliminar
    response = requests.get(api_url)
    libro = response.json() if response.status_code == 200 else None

    return render(request, 'libro/libro_fisico_delete.html', {'libro': libro})

# Vista que consume la API y pasa datos al template de LIBRO DIGITAL
def libro_digital_list(request):
    api_url = 'http://127.0.0.1:8000/api/libro_digital/'  # URL de tu API
    response = requests.get(api_url)
    libros = response.json() if response.status_code == 200 else []  # Datos desde la API
    return render(request, 'libro/libro_digital_list.html', {'libros': libros})

def libro_digital_detail(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_fisico/{pk}/'  # Endpoint de detalle
    response = requests.get(api_url)
    if response.status_code == 200:  # Si la API devuelve un libro válido
        libro = response.json()
    else:
        raise Http404("El libro físico no existe.")
    return render(request, 'libro/libro_digital_detail.html', {'libro': libro})


def libro_digital_create(request):
    if request.method == 'POST':
        api_url = 'http://127.0.0.1:8000/api/libro_digital/'
        data = {
            'titulo': request.POST['titulo'],
            'autor': request.POST['autor'],
            'anioPublicacion': request.POST['anioPublicacion'],
            'tamnomb':request.POST['tamnomb'],
            'formato':request.POST['formato']
        }
        response = requests.post(api_url, data=data)
        if response.status_code == 201:  # Creación exitosa
            return redirect('LibroDigitalList')
    return render(request, 'libro/libro_digital_form.html')

def libro_digital_update(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_digital/{pk}/'  # URL de la API para un libro específico

    if request.method == 'POST':
        data = {
            'titulo': request.POST['titulo'],
            'autor': request.POST['autor'],
            'anioPublicacion': request.POST['anioPublicacion'],
            'tamnomb':request.POST['tamnomb'],
            'formato':request.POST['formato']
        }
        response = requests.put(api_url, data=data)  # Llamada a la API para actualizar
        if response.status_code == 200:  # Actualización exitosa
            return redirect('LibroDigitalList')
    else:
        response = requests.get(api_url)  # Obtener los datos del libro desde la API
        if response.status_code == 200:
            libro = response.json()
        else:
            libro = None  # Manejar caso en que no se encuentre el libro

    return render(request, 'libro/libro_digital_form.html', {'libro': libro})

def libro_digital_delete(request, pk):
    api_url = f'http://127.0.0.1:8000/api/libro_digital/{pk}/'
    
    if request.method == 'POST':
        response = requests.delete(api_url)
        if response.status_code == 204:  # Eliminación exitosa
            return redirect('LibroDigitalList')
    
    # Obtener los datos del libro para confirmación antes de eliminar
    response = requests.get(api_url)
    libro = response.json() if response.status_code == 200 else None

    return render(request, 'libro/libro_digital_delete.html', {'libro': libro})


