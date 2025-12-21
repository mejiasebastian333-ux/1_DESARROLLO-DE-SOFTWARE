# libreria/ventas.py
from datetime import datetime
from typing import List, Dict
from .inventario import buscar_libro_por_titulo
from .clientes import buscar_cliente_por_documento

def registrar_venta(ventas: List[Dict], inventario: List[Dict], clientes: List[Dict]):
    print("\n--- Registrar venta ---\n")
    if not inventario:
        print("No hay libros en inventario.\n")
        return
    if not clientes:
        print("No hay clientes registrados.\n")
        return

    documento = input("Documento del cliente: ").strip()
    cliente = buscar_cliente_por_documento(clientes, documento)
    if not cliente:
        print("Cliente no encontrado. Registra el cliente primero.\n")
        return

    titulo = input("Titulo del libro: ").strip()
    libro = buscar_libro_por_titulo(inventario, titulo)
    if not libro:
        print("Libro no encontrado en inventario.\n")
        return

    try:
        cantidad = int(input("Cantidad a vender: ").strip())
        if cantidad <= 0:
            print("Cantidad debe ser mayor a 0.\n")
            return
    except ValueError:
        print("Ingresa una cantidad válida.\n")
        return

    stock_actual = int(float(libro.get("stock", 0)))
    if cantidad > stock_actual:
        print(f"No hay stock suficiente. Stock actual: {stock_actual}\n")
        return

    precio_unitario = float(libro.get("precio", 0.0))
    subtotal = precio_unitario * cantidad

    confirmar = input(f"Confirmar venta de {cantidad} x '{libro.get('titulo')}' a {cliente.get('nombre')} por ${subtotal:,.2f}? (si/no): ").strip().lower()
    if confirmar != "si":
        print("Venta cancelada.\n")
        return

    # actualizar stock
    libro["stock"] = str(stock_actual - cantidad)
    # recalcular total del libro
    try:
        libro["total"] = f"{float(libro.get('precio',0)) * int(libro.get('stock',0)):.2f}"
    except:
        pass

    venta = {
        "id": f"v{len(ventas)+1}",
        "documento_cliente": documento,
        "titulo_libro": libro.get("titulo"),
        "cantidad": str(cantidad),
        "precio_unitario": f"{precio_unitario:.2f}",
        "subtotal": f"{subtotal:.2f}",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ventas.append(venta)
    print("Venta registrada con éxito.\n")

def mostrar_ventas(ventas: List[Dict]):
    print("\n--- Ventas registradas ---\n")
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    for v in ventas:
        print(f"ID: {v.get('id')} | Cliente: {v.get('documento_cliente')} | Libro: {v.get('titulo_libro')} | Cantidad: {v.get('cantidad')} | Precio unitario: ${float(v.get('precio_unitario')):,.2f} | Subtotal: ${float(v.get('subtotal')):,.2f} | Fecha: {v.get('fecha')}")
    print()

def buscar_venta(ventas: List[Dict]):
    print("\n--- Buscar venta ---\n")
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    print("Buscar por:\n1. Documento del cliente\n2. Título del libro\n3. Fecha exacta (YYYY-MM-DD)")
    opcion = input("Selecciona opción (1-3): ").strip()
    term = input("Ingrese término de búsqueda: ").strip()
    resultados = []
    if opcion == "1":
        for v in ventas:
            if v.get("documento_cliente") == term:
                resultados.append(v)
    elif opcion == "2":
        for v in ventas:
            if v.get("titulo_libro","").strip().lower() == term.strip().lower():
                resultados.append(v)
    elif opcion == "3":
        for v in ventas:
            if v.get("fecha","").startswith(term):
                resultados.append(v)
    else:
        print("Opción inválida.")
        return

    if not resultados:
        print("No se encontraron ventas para esa búsqueda.\n")
        return
    print("\n--- Resultados ---\n")
    for v in resultados:
        print(f"ID: {v.get('id')} | Cliente: {v.get('documento_cliente')} | Libro: {v.get('titulo_libro')} | Cantidad: {v.get('cantidad')} | Precio unitario: ${float(v.get('precio_unitario')):,.2f} | Subtotal: ${float(v.get('subtotal')):,.2f} | Fecha: {v.get('fecha')}")
    print()
