//status.service.js//

export const STATUS_FLOW = {
  pendiente: ["proceso"],
  proceso: ["pendiente", "completada"],
  completada: ["proceso"]
};
