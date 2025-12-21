// -------------------------
// MENSAJE DE BIENVENIDA
// -------------------------

document.addEventListener("DOMContentLoaded", () => {
    alert("¡Bienvenido a mi portafolio!");
});

// -------------------------
// CAMBIAR TEXTO AL HACER CLIC
// -------------------------

const btnCambiarTexto = document.createElement("button");
btnCambiarTexto.textContent = "Cambiar descripción";
btnCambiarTexto.style.marginTop = "10px";

const parrafoSobreMi = document.querySelector("#sobre-mi p");
parrafoSobreMi.after(btnCambiarTexto);

btnCambiarTexto.addEventListener("click", () => {
    parrafoSobreMi.textContent = "Soy un desarrollador web apasionado por aprender, mejorar constantemente y crear experiencias digitales claras y funcionales.";
});

// -------------------------
// MOSTRAR / OCULTAR PROYECTOS
// -------------------------

const btnToggle = document.createElement("button");
btnToggle.textContent = "Mostrar / Ocultar proyectos";
btnToggle.style.marginBottom = "20px";

const seccionProyectos = document.querySelector("#proyectos ul");
seccionProyectos.before(btnToggle);

btnToggle.addEventListener("click", () => {
    seccionProyectos.style.display = seccionProyectos.style.display === "none" ? "grid" : "none";
});
