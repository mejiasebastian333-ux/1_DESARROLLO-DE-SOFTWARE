# Solicita al usuario el nombre del producto
nombreproducto = input("\nIngrese el nombre del producto: ")

# Solicita el precio unitario y valida que sea mayor a 0
precioUnitarioproducto = float(input("\nIngrese el precio unitario del producto: $"))
while precioUnitarioproducto <= 0:
    print("\nEl precio ingresado debe ser mayor a 0. Por favor intente nuevamente\n")
    precioUnitarioproducto = float(input("\nIngrese el precio unitario del producto: $"))

# Solicita la cantidad del producto y valida que sea mayor a 0
Cantidadproducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: "))
while Cantidadproducto <= 0:
    print("\nLa cantidad ingresada debe ser mayor a 0. Por favor intente nuevamente\n")
    Cantidadproducto = int(input("\nDigita la cantidad que deseas ingresar al inventario: "))

# Solicita confirmación para agregar el producto al inventario
confirmar = input(f"\n¿Confirma que deseas agregar {Cantidadproducto} unidades del producto '{nombreproducto}' al inventario? (si/no): ").lower()
while confirmar not in ["si", "no"]:
    print("\nRespuesta no válida. Por favor responde con 'si' o 'no'.\n")
    confirmar = input(f"\n¿Confirma que deseas agregar {Cantidadproducto} unidades del producto '{nombreproducto}' al inventario? (si/no): ").lower()

# Si confirma, muestra resumen del producto ingresado; si no, cancela la operación
if confirmar == "si":
    costoTotal = precioUnitarioproducto * Cantidadproducto
    print(f"\nProducto ingresado exitosamente.\n\nNombre del producto: {nombreproducto}\nPrecio unitario: ${precioUnitarioproducto:,.0f}\nCantidad ingresada: {Cantidadproducto}\nCosto total: ${costoTotal:,.0f}\n")
else:
    print("\nOperación cancelada. No se realizaron cambios en el inventario.\n")