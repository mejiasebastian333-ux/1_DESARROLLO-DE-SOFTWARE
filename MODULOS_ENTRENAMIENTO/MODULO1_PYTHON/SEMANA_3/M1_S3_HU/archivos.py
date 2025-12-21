# ---------------------------------------------
# Guardar CSV
# ---------------------------------------------
import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de diccionarios con productos.
        ruta (str): Ruta del archivo CSV a guardar.
        incluir_header (bool): Si True, escribe encabezado.
    """

    # Validar inventario vacío
    if not inventario:
        print("\nEl inventario está vacío.")
        confirmar = input("¿Deseas guardar un archivo vacío? (si/no): ").lower()

        while confirmar not in ["si", "no"]:
            confirmar = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

        if confirmar == "no":
            print("\nOperación cancelada.\n")
            return
        else:
            print("\nGuardando archivo vacío...\n")

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            # Escribir el encabezado
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            # Escribir filas del inventario
            for producto in inventario:
                escritor.writerow([
                    producto["Nombre del producto"],
                    producto["Precio del producto"],
                    producto["Cantidad del producto"]
                ])

        print(f"\nInventario guardado en: {ruta}\n")

    except PermissionError:
        print("\nError: No tienes permisos para escribir en esa ubicación.\n")

    except OSError:
        print("\nError: No se pudo escribir el archivo. Verifica la ruta o permisos.\n")



# ---------------------------------------------
# Cargar CSV
# ---------------------------------------------
def cargar_csv(ruta, inventario):
    print("\n--- Cargar archivo CSV ---\n")

    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # Validar encabezado
            try:
                encabezado = next(lector)
            except StopIteration:
                print("\nEl archivo CSV está vacío.\n")
                return inventario

            encabezado_esperado = ["nombre", "precio", "cantidad"]
            if [col.lower().strip() for col in encabezado] != encabezado_esperado:
                print("\nError: El encabezado del CSV no es válido. Debe ser:")
                print("nombre,precio,cantidad\n")
                return inventario

            # Validar filas
            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_cargados.append({
                        "nombre": nombre.strip(),
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1
                    continue

    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo '{ruta}'.\n")
        return inventario

    except UnicodeDecodeError:
        print("\nError: No se pudo leer el archivo. Codificación inválida.\n")
        return inventario

    except Exception as e:
        print(f"\nError inesperado: {e}\n")
        return inventario

    # Si no se cargó nada válido
    if not productos_cargados:
        print("\nNo se encontró ningún producto válido en el archivo.")
        print("El inventario no será modificado.\n")
        return inventario

    # Muestra resumen y pregunta
    print(f"\nProductos válidos encontrados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}\n")

    opcion = input("\n¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == "S":
        nuevo_inventario = []
        for p in productos_cargados:
            nuevo_inventario.append({
                "Nombre del producto": p["nombre"],
                "Precio del producto": p["precio"],
                "Cantidad del producto": p["cantidad"],
                "Total": p["precio"] * p["cantidad"]
            })

        print("\nInventario sobrescrito correctamente.\n")
        return nuevo_inventario

    # Fusionar inventarios
    print("\nFusionando inventarios...\n")

    inventario_por_nombre = {
        p["Nombre del producto"].lower(): p for p in inventario
    }

    for producto in productos_cargados:
        nombre = producto["nombre"].lower()

        if nombre in inventario_por_nombre:
            existente = inventario_por_nombre[nombre]

            existente["Cantidad del producto"] += producto["cantidad"]

            if existente["Precio del producto"] != producto["precio"]:
                existente["Precio del producto"] = producto["precio"]

            existente["Total"] = (
                existente["Precio del producto"] *
                existente["Cantidad del producto"]
            )

        else:
            inventario_por_nombre[nombre] = {
                "Nombre del producto": producto["nombre"],
                "Precio del producto": producto["precio"],
                "Cantidad del producto": producto["cantidad"],
                "Total": producto["precio"] * producto["cantidad"]
            }

    final = list(inventario_por_nombre.values())

    print("\nInventario fusionado correctamente.\n")
    print(f"Productos añadidos/actualizados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}\n")

    return final
