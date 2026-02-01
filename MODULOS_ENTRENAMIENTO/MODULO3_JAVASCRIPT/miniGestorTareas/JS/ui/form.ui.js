//form.ui.js//

import { Task } from "../models/task.model.js";
import { addTask, getTaskById, updateTask } from "../services/task.service.js";
import { renderAll } from "../main.js";

const form = document.getElementById("formMain");
const panel = document.getElementById("taskPanel");
const formBox = document.getElementById("taskForm");

let editingTaskId = null;

document.getElementById("createTask").addEventListener("click", () => {
  panel.style.display = "none";
  formBox.style.display = "block";
});

document.getElementById("cancelForm").addEventListener("click", () => {
  editingTaskId = null;
  form.reset();
  formBox.style.display = "none";
  panel.style.display = "block";
});

document.addEventListener("edit-task", e => {
  const task = getTaskById(e.detail.id);
  if (!task) return;

  editingTaskId = task.id;

  document.getElementById("nameTask").value = task.title;
  document.getElementById("description").value = task.description;
  document.getElementById("selecPriority").value = task.priority;

  panel.style.display = "none";
  formBox.style.display = "block";
});

form.addEventListener("submit", e => {
  e.preventDefault();

  const title = document.getElementById("nameTask").value.trim();
  const description = document.getElementById("description").value.trim();
  const priority = document.getElementById("selecPriority").value;

  if (!title || priority === "Nivel de urgencia") {
    alert("Completa todos los campos");
    return;
  }

  if (editingTaskId) {
    const current = getTaskById(editingTaskId);

    updateTask({
      id: editingTaskId,
      title,
      description,
      priority,
      status: current.status
    });
  } else {
    addTask(new Task(title, description, priority));
  }

  editingTaskId = null;
  renderAll();

  form.reset();
  formBox.style.display = "none";
  panel.style.display = "block";
});
