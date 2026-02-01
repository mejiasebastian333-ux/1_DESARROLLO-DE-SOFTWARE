//task.model.js//

export class Task {
  constructor(title, description, priority) {
    this.id = crypto.randomUUID();
    this.title = title;
    this.description = description;
    this.priority = priority; // Alto | Medio | Bajo
    this.status = "pendiente";
  }
}
