// sistema_interactivo.js
console.log("JS cargado correctamente");

// Entrada del nombre
let nombre = prompt("Ingresa tu nombre:");

// Variable para la edad
let edad;

// Bucle para validar la edad
do {
  let edadIngresada = prompt("Ingresa tu edad (solo números):");
  edad = Number(edadIngresada);

  if (isNaN(edad) || edad <= 0) {
    alert("Error: Por favor ingresa una edad válida en números.");
  }
} while (isNaN(edad) || edad <= 0);

// Condicionales finales
if (edad < 18) {
  alert(`Hola ${nombre}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`);
  console.log(`Hola ${nombre}, eres menor de edad.`);
} else {
  alert(`Hola ${nombre}, eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!`);
  console.log(`Hola ${nombre}, eres mayor de edad.`);
}