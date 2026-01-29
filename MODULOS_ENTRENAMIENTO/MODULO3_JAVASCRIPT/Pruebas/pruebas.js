/*

function saludar(nombre) {
  console.log("Hola " + nombre);
}

saludar("Sebastián");


function sumar(a, b) {
  return a + b;
}

let resultado = sumar(3, 5);
console.log(resultado); // 8


function despedir() {
  console.log("Adiós");
}


const despedir = function() {
  console.log("Adiós");
};


const despedir = () => {
  console.log("Adiós");
};



function prueba() {
  return "Hola";
  console.log("Esto nunca se ejecuta");
}



function esMayorDeEdad(edad) {
  return edad >= 18;
}

if (esMayorDeEdad(20)) {
  console.log("Acceso permitido");
}



function mostrarUsuario(usuario) {
  console.log(usuario.nombre);
  console.log(usuario.edad);
}

mostrarUsuario({
  nombre: "Ana",
  edad: 20
});



function ejecutar(funcion) {
  funcion();
}

ejecutar(() => {
  console.log("Hola desde el callback");
});



function saludo1() {
  console.log("Hola");
}

function saludo2() {
    console.log("Buenos días");
}

function saludo3() {
    console.log("Buenas tardes")
}

function saludo4() {
    console.log("Buenas Noches")
}



function ejecutarSaludo(saludo) {
  saludo();  
}

ejecutarSaludo(saludo4);



function saludar(nombre) {
  console.log("Hola " + nombre);
}

saludar("Carlos");



function sumarNumeros(num1, num2) {
  return(num1 + num2);
}

let resultado = sumarNumeros(5, 5);



function decirHola() {
  console.log("Hola");
}

setTimeout(decirHola, 1000);


function mostrarPersona(nombre, edad) {
  console.log("Nombre:", nombre);
  console.log("Edad:", edad);
}

mostrarPersona("Ana", 18);



function esPar(numero) {
  return numero % 2 === 0 ? "Par" : "Impar";
}

console.log(esPar(4)); 
console.log(esPar(7)); 



function decirHola() {
  console.log("Hola");
}

let accion = decirHola;



ejecutarAccion(() => {
  console.log("Función flecha");
});



function ejemplo(accion, callback) {
    console.log(accion);
    callback();
}

let accion = "Preparar la comida";

ejemplo(accion, () => {
    console.log("Esto es lo que ejecuta el callback");
});



function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot be divided by zero");
  }
  return a / b;

}

try {
  let result = divide(10, 0);
  console.log(result);
} catch (error) {
  console.error("Error:", error.messaje);
}



const productos = [
  {id }
]



function saludar() {
  return "Hola";
}

console.log(saludar())

const miFuncion = saludar;

*/

