estudiantes = [] ##NO VA EN EL CÓDIGO ORIGINAL (Solo es para que VS Code reconozca la variable)

def actualizar():
    if not estudiantes:
        print("La lista está vacía")
        return
    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a actualizar: "))
    except ValueError:
        print("digite un numero valido")
    
    # Buscar estudiante por documento
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar: #validacion numero de documento
            print("Estudiante encontrado:")
            print(estudiante)

            print("\n¿Qué desea actualizar?")
            print("1. Nombre")
            print("2. Documento")
            print("3. Edad")
            print("4. Género")

            try:
                opcion = int(input("Seleccione una opción: "))

            
                if opcion == 1:
                    estudiante["nombre"] = input("Nuevo nombre: ").lower()
                elif opcion == 2:
                    estudiante["documento"] = int(input("Nuevo documento: "))
                elif opcion == 3:
                    estudiante["edad"] = int(input("Nueva edad: "))
                elif opcion == 4:
                    estudiante["genero"] = input("Nuevo género: ").lower()
                else:
                    print("Opción no válida")
            except ValueError:
                print("ingrese un un valor valido")

            print("Datos actualizados con éxito.")
            return
    
    print("No se encontró un estudiante con ese documento.")

#sm

def eliminar_estudiante():
    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a actualizar: "))
    except ValueError:
        print("digite un numero valido")
        for estudiante in estudiantes:
            if estudiante["documento"] == documento_buscar:
                estudiantes.remove(estudiante)
        print("estudiante eliminado con exito")

