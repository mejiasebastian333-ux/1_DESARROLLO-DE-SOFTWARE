# Panaderia_DonPacho.py

CantidadPan = int(input("\nIngrese la cantidad de panes que desea comprar: "))
PrecioUnitarioPan = float(300)
TotalPagar = CantidadPan * PrecioUnitarioPan
Descuento10 = 0.10
Descuento20 = 0.20

if CantidadPan > 0 and CantidadPan <= 20:
    print(f"El total a pagar sin descuento es: {TotalPagar}")
    print("\nGracias por su compra en Panadería Don Pacho.")
elif CantidadPan > 20 and CantidadPan <= 50:
    TotalPagar = TotalPagar - (TotalPagar * Descuento10)
    print(f"El total a pagar con descuento del 10% es: {TotalPagar}")
    print("\nGracias por su compra en Panadería Don Pacho.")
elif CantidadPan > 50:
    TotalPagar = TotalPagar - (TotalPagar * Descuento20)
    print(f"El total a pagar con descuento del 20% es: {TotalPagar}")
    print("\nGracias por su compra en Panadería Don Pacho.")
else:
    print("Error: La cantidad de panes no puede ser negativa o cero.")
    PrecioUnitarioPan = 0