// task.ui.js

import { moveTask, deleteTask } from "../services/task.service.js";
import { renderAll } from "../main.js";

const taskList = document.getElementById("taskList");
const doing = document.getElementById("doing");
const done = document.getElementById("done");

export function clearTasksUI() {
  taskList.innerHTML = "";
  doing.innerHTML = "";
  done.innerHTML = "";
}

export function renderTask(task) {
  const div = document.createElement("div");
  div.className = "border rounded p-2 task mb-2";
  div.dataset.id = task.id;
  div.dataset.state = task.status;

  const collapseId = `collapse-${task.id}`;

  div.innerHTML = `
    <div class="d-flex justify-content-between align-items-center mb-2">
      <strong>${task.title}</strong>
      <div>
        <button class="btn btn-sm btn-secondary edit">✏️</button>
        <button class="btn btn-sm btn-danger delete">X</button>
      </div>
    </div>

    <div class="accordion mb-2">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button
            class="accordion-button collapsed"
            data-bs-toggle="collapse"
            data-bs-target="#${collapseId}"
          >
            Descripción
          </button>
        </h2>
        <div id="${collapseId}" class="accordion-collapse collapse">
          <div class="accordion-body">
            ${task.description}
          </div>
        </div>
      </div>
    </div>

    <span class="badge ${task.priority}">
      ${task.priority}
    </span>

    <div class="actions mt-2"></div>
  `;

  updateButtons(div, task);

  if (task.status === "pendiente") taskList.appendChild(div);
  if (task.status === "proceso") doing.appendChild(div);
  if (task.status === "completada") done.appendChild(div);
}

function updateButtons(container, task) {
  const actions = container.querySelector(".actions");
  actions.innerHTML = "";

  if (task.status !== "pendiente") {
    actions.innerHTML += `
      <button class="btn btn-sm btn-outline-dark left">&larr;</button>
    `;
  }

  if (task.status !== "completada") {
    actions.innerHTML += `
      <button class="btn btn-sm btn-outline-dark right">&rarr;</button>
    `;
  }
}

document.addEventListener("click", e => {
  const taskEl = e.target.closest(".task");
  if (!taskEl) return;

  const id = taskEl.dataset.id;

  if (e.target.classList.contains("right")) {
    moveTask(id, "right");
    renderAll();
  }

  if (e.target.classList.contains("left")) {
    moveTask(id, "left");
    renderAll();
  }

  if (e.target.classList.contains("delete")) {
    deleteTask(id);
    renderAll();
  }

  if (e.target.classList.contains("edit")) {
    document.dispatchEvent(
      new CustomEvent("edit-task", { detail: { id } })
    );
  }
});
