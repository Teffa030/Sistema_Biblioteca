fetch('http://127.0.0.1:8000/api/libros_fisicos/') // Cambia la URL según tu API
    .then(response => response.json())
    .then(data => {
        const formContainer = document.getElementById('form-container');

        // Aquí asumimos que "data" es el formulario recibido desde la API.
        const formHTML = `
            <form id="addBookForm">
                <div class="mb-3">
                    <label for="title" class="form-label">Título</label>
                    <input type="text" id="title" name="title" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label for="author" class="form-label">Autor</label>
                    <input type="text" id="author" name="author" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label for="price" class="form-label">Precio</label>
                    <input type="number" id="price" name="price" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary">Enviar</button>
            </form>
        `;

        // Renderizamos el formulario dentro del contenedor
        formContainer.innerHTML = formHTML;

        // Agregamos el evento de envío del formulario
        const addBookForm = document.getElementById('addBookForm');
        addBookForm.addEventListener('submit', (event) => {
            event.preventDefault();

            // Capturar los datos del formulario
            const formData = {
                title: document.getElementById('title').value,
                author: document.getElementById('author').value,
                price: document.getElementById('price').value
            };

            // Enviar los datos a la API
            fetch('http://127.0.0.1:8000/api/libros-fisicos/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Libro añadido:', data);
                alert('Libro añadido con éxito.');
            })
            .catch(error => {
                console.error('Error al añadir el libro:', error);
            });
        });
    })
    .catch(error => console.error('Error al cargar el formulario:', error));
