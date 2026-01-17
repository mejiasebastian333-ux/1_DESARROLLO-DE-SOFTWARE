// gestion_datos.js
// Gestión de datos con Objetos, Sets y Maps en JavaScript
// Objetivo: Consolidar el entendimiento y aplicación de estructuras de datos avanzadas

// =======================
// TASK 1: Creación del objeto de productos
// =======================

// Creamos un objeto con varios productos, cada uno con id, nombre y precio*/
const productos = {
    producto1: { id: 1, nombre: "Laptop", precio: 3500 },
    producto2: { id: 2, nombre: "Mouse", precio: 150 },
    producto3: { id: 3, nombre: "Teclado", precio: 250 },
    producto4: { id: 4, nombre: "Monitor", precio: 1200 }
};

// =======================
// TASK 2: Uso de Set en JavaScript
// =======================

// Creamos un Set con números repetidos
let numeros = new Set([1, 2, 3, 3, 4, 5, 5, 6]);

console.log("Contenido inicial del Set (sin duplicados):", numeros);

// Agregar un nuevo número
numeros.add(7);
console.log("Set después de agregar 7:", numeros);

// Verificar si existe un número
console.log("¿El número 3 está en el Set?", numeros.has(3));

// Eliminar un número
numeros.delete(2);
console.log("Set después de eliminar el número 2:", numeros);

// Recorrer el Set con for...of
console.log("Recorriendo el Set con for...of:");
for (let numero of numeros) {
    console.log(numero);
}

// =======================
// TASK 3: Creación de un Map
// =======================

// Creamos un Map que relaciona categoría con nombre de producto
const categorias = new Map();
categorias.set("Tecnología", "Laptop");
categorias.set("Accesorios", "Mouse");
categorias.set("Periféricos", "Teclado");
categorias.set("Pantallas", "Monitor");

// =======================
// TASK 4: Iteración sobre las estructuras de datos
// =======================

// Iterar sobre el objeto con for...in
console.log("Propiedades y valores del objeto productos:");
for (let key in productos) {
    console.log(`${key}: id=${productos[key].id}, nombre=${productos[key].nombre}, precio=${productos[key].precio}`);
}

// Usar métodos de objetos
console.log("Object.keys(productos):", Object.keys(productos));
console.log("Object.values(productos):", Object.values(productos));
console.log("Object.entries(productos):", Object.entries(productos));

// Iterar sobre el Set con for...of (ya mostrado arriba)

// Iterar sobre el Map con forEach
console.log("Recorriendo el Map con forEach:");
categorias.forEach((valor, clave) => {
    console.log(`Categoría: ${clave} -> Producto: ${valor}`);
});

// =======================
// TASK 5: Validación y pruebas
// =======================

// Función de validación de productos
function validarProducto(producto) {
    return (
        producto &&
        typeof producto.id === "number" &&
        typeof producto.nombre === "string" &&
        typeof producto.precio === "number"
    );
}

// Validar todos los productos
console.log("Validaciones de productos:");
for (let key in productos) {
    console.log(`${key} válido?:`, validarProducto(productos[key]));
}

// Mostrar lista completa de productos
console.log("Lista completa de productos:", productos);

// Mostrar lista de productos únicos (Set de nombres)
const nombresUnicos = new Set(Object.values(productos).map(p => p.nombre));
console.log("Lista de productos únicos (Set):", nombresUnicos);

// Mostrar categorías y nombres de productos (Map)
console.log("Categorías y productos (Map):", categorias);