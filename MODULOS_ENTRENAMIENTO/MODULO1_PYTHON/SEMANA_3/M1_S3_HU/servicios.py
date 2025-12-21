import csv

# Inventario global
inventario = []


# ---------------------------------------------
# Función para agregar productos al inventario
# ---------------------------------------------
def agregar_producto(inventario):
    print("\n--- Agregar producto ---\n")

    nombre_producto = input("Ingresa el nombre del producto: ")

    # Validar precio unitario
    while True:
        try:
            precio_unitario_producto = float(input("\nIngrese el precio unitario del producto: "))
            if precio_unitario_producto > 0:
                break
            else:
                print("Error: el precio debe ser mayor a 0.")
        except ValueError:
            print("Error: ingresa un número válido.")

    # Validar cantidad
    while True:
        try:
            cantidad_producto = int(input("\nIngresa la cantidad a ingresar: "))
            if cantidad_producto > 0:
                break
            else:
                print("Error: la cantidad debe ser mayor a 0.")
        except ValueError:
            print("Error: ingresa un número entero válido.")

    valor_total = precio_unitario_producto * cantidad_producto
    print(f"\nEl valor total del producto '{nombre_producto}' es: ${valor_total:,.0f}\n")

    confirmar = input(f"¿Deseas agregar '{nombre_producto}' al inventario? (si/no): ").lower()
    while confirmar not in ["si", "no"]:
        confirmar = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

    if confirmar == "si":
        producto = {
            "Nombre del producto": nombre_producto,
            "Precio del producto": precio_unitario_producto,
            "Cantidad del producto": cantidad_producto,
            "Total": valor_total
        }

        inventario.append(producto)
        print("\nProducto agregado correctamente.\n")
    else:
        print("\nOperación cancelada.\n")


# ---------------------------------------------
# Mostrar inventario
# ---------------------------------------------
def mostrar_inventario(inventario):
    print("\n--- Inventario ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    for producto in inventario:
        print(
            f"Producto: {producto['Nombre del producto']} | "
            f"Precio: ${producto['Precio del producto']:,.0f} | "
            f"Cantidad: {producto['Cantidad del producto']} | "
            f"Total: ${producto['Total']:,.0f}"
        )
    print()


# ---------------------------------------------
# Buscar producto
# ---------------------------------------------
def buscar_producto(inventario):
    print("\n--- Buscar producto ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el nombre del producto: ").lower()

    for producto in inventario:
        if producto["Nombre del producto"].lower() == nombre_buscar:
            print("\nProducto encontrado:\n")
            print(f"Nombre: {producto['Nombre del producto']}")
            print(f"Precio: ${producto['Precio del producto']:,.0f}")
            print(f"Cantidad: {producto['Cantidad del producto']}")
            print(f"Total: ${producto['Total']:,.0f}\n")
            return

    print(f"\nNo se encontró el producto '{nombre_buscar}'.\n")


# ---------------------------------------------
# Actualizar producto
# ---------------------------------------------
def actualizar_producto(inventario):
    print("\n--- Actualizar producto ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el nombre del producto a actualizar: ").lower()

    for producto in inventario:
        if producto["Nombre del producto"].lower() == nombre_buscar:

            print("\nProducto encontrado:")
            print(f"1. Nombre actual   : {producto['Nombre del producto']}")
            print(f"2. Precio actual   : ${producto['Precio del producto']:,.0f}")
            print(f"3. Cantidad actual : {producto['Cantidad del producto']}")
            print(f"Total actual       : ${producto['Total']:,.0f}\n")

            while True:
                print("¿Qué deseas actualizar?")
                print("1. Nombre")
                print("2. Precio")
                print("3. Cantidad")
                print("4. Cancelar")

                opcion = input("\nSelecciona una opción (1-4): ")

                # Actualizar nombre
                if opcion == "1":
                    nuevo_nombre = input("\nNuevo nombre: ")
                    producto["Nombre del producto"] = nuevo_nombre
                    print("\nNombre actualizado.\n")
                    break

                # Actualizar precio
                elif opcion == "2":
                    while True:
                        try:
                            nuevo_precio = float(input("\nNuevo precio: "))
                            if nuevo_precio > 0:
                                producto["Precio del producto"] = nuevo_precio
                                producto["Total"] = nuevo_precio * producto["Cantidad del producto"]
                                print("\nPrecio actualizado.\n")
                                break
                            else:
                                print("El precio debe ser mayor a 0.")
                        except ValueError:
                            print("Ingresa un número válido.")
                    break

                # Actualizar cantidad
                elif opcion == "3":
                    while True:
                        try:
                            nueva_cantidad = int(input("\nNueva cantidad: "))
                            if nueva_cantidad > 0:
                                producto["Cantidad del producto"] = nueva_cantidad
                                producto["Total"] = nueva_cantidad * producto["Precio del producto"]
                                print("\nCantidad actualizada.\n")
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")
                        except ValueError:
                            print("Ingresa un número válido.")
                    break

                elif opcion == "4":
                    print("\nOperación cancelada.\n")
                    return

                else:
                    print("\nOpción inválida. Intenta nuevamente.\n")

            return

    print(f"\nNo se encontró el producto '{nombre_buscar}'.\n")


# ---------------------------------------------
# Eliminar producto
# ---------------------------------------------
def eliminar_producto(inventario):
    print("\n--- Eliminar producto ---\n")

    if not inventario:
        print("El inventario está vacío.\n")
        return

    nombre_buscar = input("Ingresa el nombre del producto a eliminar: ").lower()

    for producto in inventario:
        if producto["Nombre del producto"].lower() == nombre_buscar:

            print("\nProducto encontrado:\n")
            print(f"Nombre   : {producto['Nombre del producto']}")
            print(f"Precio   : ${producto['Precio del producto']:,.0f}")
            print(f"Cantidad : {producto['Cantidad del producto']}")
            print(f"Total    : ${producto['Total']:,.0f}\n")

            confirmar = input(f"¿Eliminar '{producto['Nombre del producto']}'? (si/no): ").lower()

            while confirmar not in ["si", "no"]:
                confirmar = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

            if confirmar == "si":
                inventario.remove(producto)
                print("\nProducto eliminado.\n")
            else:
                print("\nOperación cancelada.\n")

            return

    print(f"\nNo se encontró el producto '{nombre_buscar}'.\n")


# ---------------------------------------------
# Estadísticas
# ---------------------------------------------
def calcular_estadisticas(inventario):
    print("\n--- Estadísticas ---\n")

    if not inventario:
        print("No hay estadísticas, el inventario está vacío.\n")
        return

    unidades_totales = sum(p["Cantidad del producto"] for p in inventario)
    valor_total = sum(p["Total"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["Precio del producto"])
    producto_mayor_stock = max(inventario, key=lambda p: p["Cantidad del producto"])

    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.0f}")
    print(f"Producto más caro: {producto_mas_caro['Nombre del producto']} (${producto_mas_caro['Precio del producto']:,.0f})")
    print(f"Producto con más stock: {producto_mayor_stock['Nombre del producto']} ({producto_mayor_stock['Cantidad del producto']} unidades)\n")
