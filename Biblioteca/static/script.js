fetch('http://127.0.0.1:8000/api/libros_fisicos/') // Cambia la URL según tu API
    .then(response => response.json())
    .then(data => {

        alert('Hola bb')
        // Crear un contenedor para el formulario
        const formContainer = document.createElement('div');
        
        // Generar el HTML del formulario dinámicamente (ejemplo básico)
        const formHTML = `
            <form id="addBookForm">
                {% csrf_token %}
                <label for="codigoLibro">Codigo del Libro:</label>
                <input type="number" id="title" name="codigoLibro" required/>

                <label for="titulo">Título:</label>
                <input type="text" id="title" name="titulo" required/>
                
                <label for="autor">Autor:</label>
                <input type="text" id="autor" required/>
                
                <label for="aniopublicacion">Precio:</label>
                <input type="data" id="aniopublicacion" required/>

                <label for="numeropagina">Numero de paginas:</label>
                <input type="number" id="numeropagina" required/>
                
                <button type="submit">Añadir Libro</button>
            </form>
        `;

        // Agregar el formulario al contenedor
        formContainer.innerHTML = formHTML;
        document.body.appendChild(formContainer); // Añadirlo al DOM

        // Capturar el formulario después de agregarlo al DOM
        const addBookForm = document.getElementById('addBookForm');

        // Agregar el evento de envío
        addBookForm.addEventListener('submit', (event) => {
            event.preventDefault();

            // Capturar los datos del formulario
            const formData = {
                title: document.getElementById('codigoLibro').value,
                author: document.getElementById('titulo').value,
                price: document.getElementById('autor').value,
                price: document.getElementById('aniopublicacion').value,
                price: document.getElementById('numeropagina').value
            };

            // Enviar los datos a la API
            fetch('http://127.0.0.1:8000/api/libros_fisicos/', { // Ajustar URL si es necesario
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
                alert('Error al añadir el libro. Por favor, inténtalo de nuevo.');
            });
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

