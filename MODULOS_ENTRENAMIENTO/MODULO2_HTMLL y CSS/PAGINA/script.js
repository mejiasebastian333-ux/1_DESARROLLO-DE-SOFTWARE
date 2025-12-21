// script.js
// Archivo JavaScript encargado de la lógica del carrito de compras.
// Permite agregar productos, eliminarlos individualmente
// y vaciar completamente el carrito mediante eventos.

// ==============================
// VARIABLES PRINCIPALES
// ==============================
// Se seleccionan los elementos del DOM que se usarán
// para manipular el carrito y los productos.

const carrito = document.getElementById('carrito');
const elementos1 = document.getElementById('lista-1');
const lista = carrito.querySelector('tbody'); // referencia segura al cuerpo de la tabla
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

// ==============================
// INICIALIZACIÓN DE EVENTOS
// ==============================
// Se cargan los event listeners necesarios
// al iniciar el script.

cargarEventListeners();

// ==============================
// FUNCIÓN: cargarEventListeners
// ==============================
// Asigna los eventos principales:
// - Click para agregar productos al carrito
// - Click para eliminar productos individuales
// - Click para vaciar completamente el carrito

function cargarEventListeners() {
    elementos1.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
}

// ==============================
// FUNCIÓN: comprarElemento
// ==============================
// Detecta cuando se hace clic en el botón
// "Agregar al carrito" y obtiene el producto
// correspondiente.

function comprarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.closest('.product'); // selecciona el contenedor del producto
        leerDatosElemento(elemento);
    }
}

// ==============================
// FUNCIÓN: leerDatosElemento
// ==============================
// Extrae la información relevante del producto
// (imagen, título, precio e id)
// y la organiza en un objeto.

function leerDatosElemento(elemento) {
    const infoElemento = {
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id: elemento.querySelector('a').getAttribute('data-id')
    };
    insertarCarrito(infoElemento);
}

// ==============================
// FUNCIÓN: insertarCarrito
// ==============================
// Crea dinámicamente una fila en la tabla
// del carrito con la información del producto
// seleccionado.

function insertarCarrito(elemento) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td><img src="${elemento.imagen}" width="100"></td>
        <td>${elemento.titulo}</td>
        <td>${elemento.precio}</td>
        <td><a href="#" class="borrar" data-id="${elemento.id}">x</a></td>
    `;
    lista.appendChild(row);
}

// ==============================
// FUNCIÓN: eliminarElemento
// ==============================
// Permite eliminar un producto específico
// del carrito al hacer clic en el botón "x".

function eliminarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('borrar')) {
        e.target.parentElement.parentElement.remove(); // elimina la fila completa
    }
}

// ==============================
// FUNCIÓN: vaciarCarrito
// ==============================
// Elimina todos los productos del carrito
// recorriendo y limpiando el tbody.

function vaciarCarrito() {
    while(lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    return false;
}