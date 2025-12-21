tareas = 0 
tareas_que_faltan = 10
total_tareas = 11


while tareas < 10:
    tareas += 1
    
    if tareas < 10:
        tareas_que_faltan = total_tareas - tareas - 1
        print (f"Tarea #{tareas} recibida, faltan {tareas_que_faltan} por calificar")
        
    else:
        print(f"Tarea #{tareas} ¡Todas las tareas recibidas!")
    