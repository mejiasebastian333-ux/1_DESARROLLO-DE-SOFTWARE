# app.py
import os
from libreria.archivos import (
    cargar_inventario, cargar_clientes, cargar_ventas,
    guardar_inventario_prompt, guardar_clientes_prompt, guardar_ventas_prompt
)
from libreria import inventario as mod_inventario
from libreria import clientes as mod_clientes
from libreria import ventas as mod_ventas
from libreria import reportes as mod_reportes

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def cargar_todo():
    # intenta cargar; si no existe, devuelve listas vacías
    try:
        inv, e1 = cargar_inventario(os.path.join(DATA_DIR, "inventario.csv"))
    except Exception as ex:
        print(f"Error cargando inventario: {ex}")
        inv, e1 = [], 0
    try:
        cls, e2 = cargar_clientes(os.path.join(DATA_DIR, "clientes.csv"))
    except Exception as ex:
        print(f"Error cargando clientes: {ex}")
        cls, e2 = [], 0
    try:
        vts, e3 = cargar_ventas(os.path.join(DATA_DIR, "ventas.csv"))
    except Exception as ex:
        print(f"Error cargando ventas: {ex}")
        vts, e3 = [], 0

    total_omitidos = e1 + e2 + e3
    if total_omitidos:
        print(f"Advertencia: se omitieron {total_omitidos} filas inválidas al cargar CSV(s).")

    return inv, cls, vts

def main():
    inventario_db, clientes_db, ventas_db = cargar_todo()

    while True:
        print("\n===== MENÚ PRINCIPAL =====\n")
        print("1. Gestión del inventario")
        print("2. Gestión de ventas")
        print("3. Gestión de clientes")
        print("4. Reportes")
        print("5. Guardar y salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            while True:
                print("\n--- GESTIÓN DEL INVENTARIO ---")
                print("1. Agregar libro")
                print("2. Mostrar inventario")
                print("3. Buscar libro")
                print("4. Actualizar libro")
                print("5. Eliminar libro")
                print("6. Guardar inventario (pregunta ruta)")
                print("7. Volver al menú principal")
                op = input("Opción: ").strip()
                if op == "1":
                    mod_inventario.agregar_libro(inventario_db)
                elif op == "2":
                    mod_inventario.mostrar_inventario(inventario_db)
                elif op == "3":
                    mod_inventario.buscar_libro(inventario_db)
                elif op == "4":
                    mod_inventario.actualizar_libro(inventario_db)
                elif op == "5":
                    mod_inventario.eliminar_libro(inventario_db)
                elif op == "6":
                    guardar_inventario_prompt(inventario_db)
                elif op == "7":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            while True:
                print("\n--- GESTIÓN DE VENTAS ---")
                print("1. Registrar venta")
                print("2. Mostrar ventas")
                print("3. Buscar venta")
                print("4. Guardar ventas (pregunta ruta)")
                print("5. Volver al menú principal")
                op = input("Opción: ").strip()
                if op == "1":
                    mod_ventas.registrar_venta(ventas_db, inventario_db, clientes_db)
                elif op == "2":
                    mod_ventas.mostrar_ventas(ventas_db)
                elif op == "3":
                    mod_ventas.buscar_venta(ventas_db)
                elif op == "4":
                    guardar_ventas_prompt(ventas_db)
                elif op == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "3":
            while True:
                print("\n--- GESTIÓN DE CLIENTES ---")
                print("1. Crear cliente")
                print("2. Mostrar clientes")
                print("3. Buscar cliente")
                print("4. Actualizar cliente")
                print("5. Eliminar cliente")
                print("6. Guardar clientes (pregunta ruta)")
                print("7. Volver al menú principal")
                op = input("Opción: ").strip()
                if op == "1":
                    mod_clientes.crear_cliente(clientes_db)
                elif op == "2":
                    mod_clientes.mostrar_clientes(clientes_db)
                elif op == "3":
                    mod_clientes.buscar_cliente(clientes_db)
                elif op == "4":
                    mod_clientes.actualizar_cliente(clientes_db)
                elif op == "5":
                    mod_clientes.eliminar_cliente(clientes_db)
                elif op == "6":
                    guardar_clientes_prompt(clientes_db)
                elif op == "7":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            while True:
                print("\n--- REPORTES ---")
                print("1. Top 3 productos más vendidos")
                print("2. Ventas totales por autor")
                print("3. Ingreso bruto y neto")
                print("4. Volver al menú principal")
                op = input("Opción: ").strip()
                if op == "1":
                    mod_reportes.top_n_vendidos(ventas_db, n=3)
                elif op == "2":
                    mod_reportes.ventas_totales_por_autor(ventas_db, inventario_db)
                elif op == "3":
                    mod_reportes.ingreso_bruto_neto(ventas_db)
                elif op == "4":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "5":
            # Al salir guardamos en data/ por defecto
            from libreria.archivos import guardar_inventario_prompt, guardar_clientes_prompt, guardar_ventas_prompt
            print("Guardando archivos en ./data por defecto...")
            guardar_inventario_prompt(inventario_db)
            guardar_clientes_prompt(clientes_db)
            guardar_ventas_prompt(ventas_db)
            print("Datos guardados. Saliendo...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
