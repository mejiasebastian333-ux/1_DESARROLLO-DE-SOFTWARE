
// Array

let precios = [1000, 2000, 3000];


// Objeto 

let producto = {
  nombre: "Mouse",
  precio: 30000
};


// Array de objetos

const productos = [
  { id: 1, nombre: "Laptop", precio: 3500 },
  { id: 2, nombre: "Mouse", precio: 50 },
  { id: 3, nombre: "Teclado", precio: 120 }
];

console.log(productos)

// Operaciones comunes:

//Recorrer con ForEach
productos.forEach(p => {
  console.log(`${p.nombre} cuesta $${p.precio}`);
});

// Filtrar con filtrer
const baratos = productos.filter(p => p.precio < 100);
console.log(baratos);

// Transformar con map
const resumen = productos.map(p => {
  return { id: p.id, nombre: p.nombre };
});

console.log(resumen);




//  Ejemplo práctico: Tienda de productos

const carrito = [
  { producto: "Café", cantidad: 2, precio: 5 },
  { producto: "Pan", cantidad: 3, precio: 2 }
];

const total = carrito.reduce((acc, item) => acc + item.cantidad * item.precio, 0);
console.log(`Total: $${total}`);    




//  Ejemplo: Aplicación en APIs

fetch("https://fakestoreapi.com/products")
  .then(res => res.json())
  .then(data => {
    data.forEach(p => {
      console.log(`${p.title} cuesta $${p.price}`);
    });
  });