

// Obtener la tabla
const tablaAutos = document.getElementById('tabla-autos');

// Hacer la solicitud a la API para obtener los datos de los autos
fetch('/api/autos/')
    .then(response => response.json())
    .then(data => {
        mostrarAutosEnTabla(data);
    })
    .catch(error => {
        console.error('Error al recuperar los autos:', error);
    });

// Función para mostrar los autos en la tabla
function mostrarAutosEnTabla(autos) {
    const tbody = tablaAutos.getElementsByTagName('tbody')[0];
    autos.forEach(auto => {
        const fila = tbody.insertRow();
        fila.insertCell(0).textContent = auto.id;
        fila.insertCell(1).textContent = auto.nombre;
        fila.insertCell(2).innerHTML = `<img src="${auto.imagen}" alt="${auto.nombre}" style="max-width: 100px;">`;
        fila.insertCell(3).textContent = `$ ${auto.precio.toFixed(2)}`;
        fila.insertCell(4).textContent = auto.disponibilidad ? 'Disponible' : 'No disponible';
        fila.insertCell(5).textContent = auto.marca.join(', ');
        fila.insertCell(6).textContent = auto.modelo.join(', ');
    });
    console("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
}

