from servicios import ( 
    agregar_producto, mostrar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

inventario = []

while True:
    print("\n===== INVENTARIO =====")
    print("")    
    print("===== MENÚ PRINCIPAL =====")
    print("")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        agregar_producto(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        buscar_producto(inventario)

    elif opcion == "4":
        actualizar_producto(inventario)

    elif opcion == "5":
        eliminar_producto(inventario)

    elif opcion == "6":
        calcular_estadisticas(inventario)

    elif opcion == "7":
        ruta = input("\nIngresa la ruta del archivo CSV a guardar: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("\nIngresa la ruta del archivo CSV a cargar: ")
        inventario = cargar_csv(ruta, inventario)

    elif opcion == "9":
        print("\nSaliendo del programa...\n")
        break

    else:
        print("\nOpción inválida. Intenta nuevamente.\n")
