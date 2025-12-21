# libreria/inventario.py
from typing import List, Dict

def agregar_libro(inventario: List[Dict]):
    print("\n--- Agregar libro ---\n")
    titulo = input("Ingresa el titulo del libro: ").strip()
    autor = input("Ingresa el nombre del autor: ").strip()
    categoria = input("Ingresa la categoria del libro: ").strip()

    while True:
        try:
            precio = float(input("Ingrese el precio unitario del libro: ").strip())
            if precio >= 0:
                break
            print("El precio debe ser >= 0.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        try:
            stock = int(input("Digite el stock que desea ingresar al inventario: ").strip())
            if stock >= 0:
                break
            print("El stock debe ser >= 0.")
        except ValueError:
            print("Ingresa un número entero válido.")

    total = precio * stock
    confirmar = input(f"¿Deseas agregar '{titulo}' al inventario? (si/no): ").strip().lower()
    if confirmar != "si":
        print("Operación cancelada.")
        return

    inventario.append({
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "precio": f"{precio:.2f}",
        "stock": str(stock),
        "total": f"{total:.2f}"
    })
    print("Libro agregado correctamente.\n")

def mostrar_inventario(inventario: List[Dict]):
    print("\n--- Inventario ---\n")
    if not inventario:
        print("El inventario está vacío.\n")
        return
    for libro in inventario:
        print(f"{libro.get('titulo')} | {libro.get('autor')} | {libro.get('categoria')} | Precio: ${float(libro.get('precio')):,.2f} | Stock: {libro.get('stock')} | Total: ${float(libro.get('total')):,.2f}")
    print()

def buscar_libro(inventario: List[Dict]):
    print("\n--- Buscar libro ---\n")
    if not inventario:
        print("El inventario está vacío.\n")
        return None
    nombre = input("Ingresa el titulo del libro: ").strip().lower()
    for libro in inventario:
        if libro.get("titulo","").strip().lower() == nombre:
            print("Libro encontrado:")
            print(f"{libro.get('titulo')} | {libro.get('autor')} | Precio: ${float(libro.get('precio')):,.2f} | Stock: {libro.get('stock')}")
            return libro
    print("No se encontró el libro.\n")
    return None

def actualizar_libro(inventario: List[Dict]):
    print("\n--- Actualizar libro ---\n")
    if not inventario:
        print("El inventario está vacío.\n")
        return
    nombre = input("Ingresa el titulo del libro a actualizar: ").strip().lower()
    for libro in inventario:
        if libro.get("titulo","").strip().lower() == nombre:
            print("Libro encontrado:")
            print(libro)
            print("1. Titulo\n2. Autor\n3. Categoria\n4. Precio\n5. Stock\n6. Cancelar")
            opcion = input("Selecciona opción: ").strip()
            if opcion == "1":
                libro["titulo"] = input("Nuevo titulo: ").strip()
            elif opcion == "2":
                libro["autor"] = input("Nuevo autor: ").strip()
            elif opcion == "3":
                libro["categoria"] = input("Nueva categoria: ").strip()
            elif opcion == "4":
                try:
                    nuevo_precio = float(input("Nuevo precio: ").strip())
                    libro["precio"] = f"{nuevo_precio:.2f}"
                except:
                    print("Valor inválido.")
            elif opcion == "5":
                try:
                    nuevo_stock = int(input("Nuevo stock: ").strip())
                    libro["stock"] = str(nuevo_stock)
                except:
                    print("Valor inválido.")
            elif opcion == "6":
                print("Operación cancelada.")
                return
            # recalcular total
            try:
                libro["total"] = f"{float(libro.get('precio',0)) * int(libro.get('stock',0)):.2f}"
            except:
                libro["total"] = "0.00"
            print("Libro actualizado.\n")
            return
    print("Libro no encontrado.\n")

def eliminar_libro(inventario: List[Dict]):
    print("\n--- Eliminar libro ---\n")
    if not inventario:
        print("El inventario está vacío.\n")
        return
    nombre = input("Ingresa el titulo del libro a eliminar: ").strip().lower()
    for libro in inventario:
        if libro.get("titulo","").strip().lower() == nombre:
            confirmar = input(f"¿Eliminar '{libro.get('titulo')}'? (si/no): ").strip().lower()
            if confirmar == "si":
                inventario.remove(libro)
                print("Libro eliminado.\n")
            else:
                print("Operación cancelada.\n")
            return
    print("Libro no encontrado.\n")

# helper para ventas
def buscar_libro_por_titulo(inventario: List[Dict], titulo: str):
    titulo = titulo.strip().lower()
    for libro in inventario:
        if libro.get("titulo","").strip().lower() == titulo:
            return libro
    return None
