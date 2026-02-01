//trash.ui.js//

import { getTrash, restoreTask, deleteForever } from "../services/task.service.js";
import { renderAll } from "../main.js";

const modal = document.getElementById("trashModal");
const content = document.getElementById("trashContent");

document.getElementById("openTrash").addEventListener("click", renderTrash);
document.getElementById("closeTrash").addEventListener("click", () => {
  modal.style.display = "none";
});

function renderTrash() {
  content.innerHTML = "";
  const trash = getTrash();

  if (!trash.length) {
    content.innerHTML = "<p>No hay tareas eliminadas</p>";
  }

  trash.forEach(task => {
    const div = document.createElement("div");
    div.className = "border p-2 mb-2";

    div.innerHTML = `
      <strong>${task.title}</strong>
      <div class="mt-2">
        <button class="btn btn-sm btn-success restore">Restaurar</button>
        <button class="btn btn-sm btn-danger delete">Eliminar</button>
      </div>
    `;

    div.querySelector(".restore").onclick = () => {
      restoreTask(task.id);
      renderTrash();
      renderAll();
    };

    div.querySelector(".delete").onclick = () => {
      deleteForever(task.id);
      renderTrash();
    };

    content.appendChild(div);
  });

  modal.style.display = "flex";
}
