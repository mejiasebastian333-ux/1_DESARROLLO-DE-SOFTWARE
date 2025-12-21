# ---------------------------------------------
# Función para agregar productos al inventario
# ---------------------------------------------
def agregar_producto(inventario):
    print("\n")
    print("--- Agregar producto ---\n")
    
    nombre_producto = input("\nIngresa el nombre del producto: ")
    print("")
    
    # Validar precio unitario del producto
    while True:
        try:
            precio_unitario_producto = float(input("\nIngrese el precio unitario del producto: "))
            print("")

            if precio_unitario_producto > 0:
                break
            else:
                print("Error: el precio debe ser mayor a 0. Intenta nuevamente.")
                print("\n")                

        except ValueError:
            print("\nError: ingresa un número entero válido.")
            print("\n")

    # Validar cantidad del producto
    while True:
        try:
            cantidad_producto = int(input("\nDigita la cantidad que deseas ingresar al inventario: "))
            print("")

            if cantidad_producto > 0:
                break
            else:
                print("Error: la cantidad debe ser mayor a 0. Intenta nuevamente.")
                print("\n")
                
        except ValueError:
            print("\nError: ingresa un número entero válido.")
            print("\n")
            
    valor_total = precio_unitario_producto * cantidad_producto
    print(f"\nEl valor total a ingresar del producto: '{nombre_producto}' es de ${valor_total:,.0f}")
    print("")
    
    confirmar = str(input(f"\nConfirma que deseas agregar {cantidad_producto} unidades del producto '{nombre_producto}' al inventario? (si/no): ")).lower()
    while confirmar not in ["si", "no"]: 
            print("\nRespuesta no válida. Por favor responde con 'si' o 'no'.")
            print("\n") 
            confirmar = str(input(f"\nConfirma que deseas agregar {cantidad_producto} unidades del producto '{nombre_producto}' al inventario? (si/no): ")).lower()
        
    # Crear diccionario del producto
    if confirmar == "si": 
        producto = {
            "Nombre del producto": nombre_producto,
            "Precio del producto": precio_unitario_producto,
            "Cantidad del producto": cantidad_producto,
            "Total ingresado": valor_total
        }

        inventario.append(producto)
        print("")
        print("\nProducto agregado correctamente.\n")

    else:
        print("\nOperación cancelada. No se realizaron cambios en el inventario.\n")

# ---------------------------------------------
# Función para mostrar el inventario completo
# ---------------------------------------------
def mostrar_inventario(inventario):
    print("\n")
    print("\n--- Inventario ---")

    if not inventario:
        print("\nEl inventario está vacío.\n")
        print("")
        return

    # Recorrer los productos
    for producto in inventario:
        print(f"\nProducto: {producto['Nombre del producto']} | Precio: {producto['Precio del producto']:,.0f} | Cantidad: {producto['Cantidad del producto']} | Total: {producto['Total ingresado']:,.0f}")
    print()  # Línea vacía


# ---------------------------------------------
# Función para calcular estadísticas
# ---------------------------------------------
def calcular_estadisticas(inventario):
    print("\n")
    print("\n--- Estadísticas del inventario ---")

    if not inventario:
        print("\nNo hay productos. El inventario está vacío.\n")
        print("")
        return

    valor_total_inventario = 0
    cantidad_total_productos_inventario = 0

    # Recorrer inventario y acumular datos
    for producto in inventario:
        valor_total_inventario += producto["Total ingresado"]
        cantidad_total_productos_inventario += producto["Cantidad del producto"]

    print("\n")
    print(f"Valor total del inventario: ${valor_total_inventario:,.0f}")
    print(f"Cantidad total de productos: {cantidad_total_productos_inventario} unidades")


# ---------------------------------------------
# Programa principal con menú
# ---------------------------------------------
inventario = []

while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("\nSelecciona una opción: ")

    # Procesar opción usando if, elif y else
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        calcular_estadisticas(inventario)
    elif opcion == "4":
        print("\nSaliendo del programa...\n")
        break
    else:
        print("\nOpción inválida. Intenta nuevamente.\n")

# -------------------------------------------------------
# Resumen final de la semana:
# Esta actividad refuerza el uso de condicionales, bucles,
# manejo de listas y diccionarios, modularización con
# funciones y validación de datos.
# -------------------------------------------------------
