import csv  #Esto se pone hasta arriba para vincular otra libreria.

def exportar_a_csv():
    """
    Convierte la lista de estudiantes a un archivo CSV.
    Cada estudiante será una fila.
    """
    if not estudiantes:# Verificar contenido de estudiantes 
        print("La lista de estudiantes está vacía. No hay nada para exportar.")
        return
    # Abrimos (o creamos) el archivo CSV en modo escritura
    # newline="" evita que se creen líneas vacías entre filas
    with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)# Objeto que permite escribir filas en formato CSV


      # Esta es la primera fila (encabezados). Explica qué va en cada columna.
        escritor.writerow(["nombre", "documento", "edad", "genero"])

        # Filas de datos
        for est in estudiantes:  # Recorremos cada estudiante del programa
            escritor.writerow([   # Escribimos una fila nueva con sus datos
                est["nombre"],    # 1° columna: nombre
                est["documento"], # 2° columna: documento
                est["edad"],      # 3° columna: edad
                est["genero"]     # 4° columna: género
            ])

    print("Datos exportados correctamente a estudiantes.csv")


import json  # Libreria para manejar archivos JSON 

estudiantes = []  # Lista donde se guardarán los estudiantes


#  Cargar datos al inicio
def cargar_datos():
    """
    Carga los datos guardados en estudiantes.json
    Si el archivo no existe, simplemente se inicia una lista vacia
    """
    global estudiantes
    try:
        with open("estudiantes.json", "r") as archivo: #open(..., "r") abre el archivo llamado estudiantes.json en modo lectura ("r").
            estudiantes = json.load(archivo)  #with es un context manager: asegura que el archivo se cierre automáticamente al terminar el bloque
            print(" Datos cargados correctamente.") #lee el contenido del archivo abierto y lo interpreta como JSON, devolviendo la estructura de Python correspondiente
    except FileNotFoundError:
        print(" No se encontro el archivo. Se creará al guardar los datos")
        estudiantes = []


#  Guardar datos después de cada cambio
def guardar_datos():
    """
    Guarda la lista de estudiantes en un archivo JSON
    asi nada se pierde cuando cierres el programa! 
    """
    with open("estudiantes.json", "w") as archivo: #open("estudiantes.json", "w") abre el archivo en modo escritura ("w").
        json.dump(estudiantes, archivo, indent=4) #indent=4 → hace que el archivo JSON quede bonito y legible, con sangría de 4 espacios.
    print(" Datos guardados.") #json.dump() convierte el contenido de la variable estudiantes (por lo general una lista o diccionario)


def crear_estudiante(estudiantes): #Definimos una función llamada crear estudiantes que recibe como parametro un directorio (compuesto de listas).  
    try: #try es para que en caso de fallas el programa muestre un mensaje especifico(Riesgo calculado).
        #Valores que se pedirán al usuario por consola.
        nombre=str(input("Ingrese nombre: ")).lower() #el .lower es para poner todos los caracteres en minusculas
        documento=int(input("Ingrese el numero de documento: "))
        edad=int(input("Ingrese una edad:  "))
        genero=str(input("Ingrese el genero: ")).lower()   
    except ValueError:
        print("agregue parametros correctos")

    #Guarda la información de un estudiante como un diccionario y lo agrega a una lista llamada estudiantes.
    estudiantes.append({"nombre":nombre,
                         "documento":documento, 
                         "edad":edad, 
                         "genero":genero })
    
    print("Estudiante creado con exito")
    

def consultar():
    if not estudiantes: #el if not sirve para validar si el diccionario(Estudiantes) tiene contenido 
        print("\nla lista esta vacia\n")
        return []
    for i in estudiantes: #Se muestra el diccionario en un bucle for.
        print(f"Nombre: {i['nombre']}- Documento: {i['documento']}- Edad: {i['edad']}- Genero: {i['genero']}")  #Llamar los valores del diccionario ej= (['genero']) y eso lo muestra 


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


def eliminar_estudiante():
    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a eliminar: "))
    except ValueError:
        print("digite un numero valido")
        return
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            estudiantes.remove(estudiante)
            print("estudiante eliminado con exito")
            return


while True:
    
    print("\n<====MENU====>\n")
    print("1. consultar")
    print("2. subir")
    print("3. crear")
    print("4. actualizar")
    print("5. eliminar")
    print("6. Cargar")
    print("7. Exporta a csv")
    print("8. Salir")

    try:

        opcion=int(input("\nSelecciona una opción: "))
        if opcion <= 0 or opcion > 8:
            print("\ningrese un número valido\n")

    except ValueError:
        print("\nIngrese un número del 1 al 8\n")
        continue

    if opcion == 1:
        consultar()

    elif opcion == 2:
        guardar_datos()

    elif opcion == 3:
        crear_estudiante(estudiantes)

    elif opcion == 4:
        actualizar()

    elif opcion == 5:
        eliminar_estudiante()

    elif opcion ==6:
        cargar_datos()

    elif opcion ==7:
        exportar_a_csv()

    elif opcion == 8:
        print("\nUsted ha salido del programa\n")
        break
    else:
        print("\ningresa un valor correcto\n")