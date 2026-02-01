//main.js//

import "./ui/form.ui.js";
import "./ui/task.ui.js";
import "./ui/trash.ui.js";
import { getTasks } from "./services/task.service.js";
import { clearTasksUI, renderTask } from "./ui/task.ui.js";

export function renderAll() {
  clearTasksUI();
  getTasks().forEach(renderTask);
}

document.addEventListener("DOMContentLoaded", renderAll);
