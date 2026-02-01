//task.service.js//

import { save, load } from "../data/storage.js";

let tasks = load("tasks");
let trash = load("trash");

export function getTasks() {
  return tasks;
}

export function getTrash() {
  return trash;
}

export function getTaskById(id) {
  return tasks.find(task => task.id === id);
}

export function addTask(task) {
  tasks.push(task);
  save("tasks", tasks);
}

export function updateTask(updatedTask) {
  tasks = tasks.map(task =>
    task.id === updatedTask.id ? updatedTask : task
  );
  save("tasks", tasks);
}

export function moveTask(id, direction) {
  const task = getTaskById(id);
  if (!task) return;

  if (direction === "right") {
    if (task.status === "pendiente") task.status = "proceso";
    else if (task.status === "proceso") task.status = "completada";
  }

  if (direction === "left") {
    if (task.status === "completada") task.status = "proceso";
    else if (task.status === "proceso") task.status = "pendiente";
  }

  save("tasks", tasks);
}

export function deleteTask(id) {
  const task = getTaskById(id);
  if (!task) return;

  tasks = tasks.filter(t => t.id !== id);
  trash.push(task);

  save("tasks", tasks);
  save("trash", trash);
}

export function restoreTask(id) {
  const task = trash.find(t => t.id === id);
  if (!task) return;

  trash = trash.filter(t => t.id !== id);
  tasks.push(task);

  save("tasks", tasks);
  save("trash", trash);
}

export function deleteForever(id) {
  trash = trash.filter(t => t.id !== id);
  save("trash", trash);
}
