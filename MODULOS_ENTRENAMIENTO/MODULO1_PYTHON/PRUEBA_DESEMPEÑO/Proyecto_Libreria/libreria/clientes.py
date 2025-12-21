# libreria/clientes.py
from typing import List, Dict

def crear_cliente(clientes: List[Dict]):
    print("\n--- Crear cliente ---\n")
    nombre = input("Ingrese el nombre del cliente: ").strip()
    documento = input("Ingrese el numero de documento del cliente: ").strip()
    celular = input("Ingrese el numero de celular del cliente: ").strip()
    correo = input("Ingrese el correo electronico del cliente: ").strip()

    if not documento:
        print("Documento obligatorio.")
        return
    # evitar duplicados
    if any(c.get("documento")==documento for c in clientes):
        print("Ya existe un cliente con ese documento.")
        return

    clientes.append({
        "nombre": nombre,
        "documento": documento,
        "celular": celular,
        "correo": correo
    })
    print("Cliente creado con exito.\n")

def mostrar_clientes(clientes: List[Dict]):
    print("\n--- Lista de clientes ---\n")
    if not clientes:
        print("La lista de clientes está vacía.\n")
        return
    for c in clientes:
        print(f"{c.get('nombre')} | Documento: {c.get('documento')} | Celular: {c.get('celular')} | Correo: {c.get('correo')}")
    print()

def buscar_cliente(clientes: List[Dict]):
    print("\n--- Buscar cliente ---\n")
    if not clientes:
        print("La lista de clientes está vacía.\n")
        return None
    documento = input("Ingresa el documento del cliente: ").strip()
    for c in clientes:
        if c.get("documento") == documento:
            print(f"Cliente: {c.get('nombre')} | Documento: {c.get('documento')} | Celular: {c.get('celular')} | Correo: {c.get('correo')}\n")
            return c
    print("Cliente no encontrado.\n")
    return None

def actualizar_cliente(clientes: List[Dict]):
    print("\n--- Actualizar cliente ---\n")
    if not clientes:
        print("La lista de clientes está vacía.\n")
        return
    documento = input("Ingrese el documento del cliente: ").strip()
    for c in clientes:
        if c.get("documento") == documento:
            print(c)
            print("1. Nombre\n2. Documento\n3. Celular\n4. Correo\n5. Cancelar")
            opcion = input("Selecciona la opción: ").strip()
            if opcion == "1":
                c["nombre"] = input("Nuevo nombre: ").strip()
            elif opcion == "2":
                nuevo_doc = input("Nuevo documento: ").strip()
                if any(x.get("documento")==nuevo_doc for x in clientes if x is not c):
                    print("Ya existe otro cliente con ese documento.")
                    return
                c["documento"] = nuevo_doc
            elif opcion == "3":
                c["celular"] = input("Nuevo celular: ").strip()
            elif opcion == "4":
                c["correo"] = input("Nuevo correo: ").strip()
            elif opcion == "5":
                print("Operación cancelada.")
                return
            else:
                print("Opción inválida.")
                return
            print("Datos actualizados con éxito.\n")
            return
    print("Cliente no encontrado.\n")

def eliminar_cliente(clientes: List[Dict]):
    print("\n--- Eliminar cliente ---\n")
    if not clientes:
        print("La lista de clientes está vacía.\n")
        return
    documento = input("Ingrese el documento del cliente: ").strip()
    for c in clientes:
        if c.get("documento") == documento:
            confirmar = input(f"¿Eliminar al cliente {c.get('nombre')}? (si/no): ").strip().lower()
            if confirmar == "si":
                clientes.remove(c)
                print("Cliente eliminado con éxito.\n")
            else:
                print("Operación cancelada.\n")
            return
    print("Cliente no encontrado.\n")

# helper para ventas
def buscar_cliente_por_documento(clientes: List[Dict], documento: str):
    for c in clientes:
        if c.get("documento") == documento:
            return c
    return None
