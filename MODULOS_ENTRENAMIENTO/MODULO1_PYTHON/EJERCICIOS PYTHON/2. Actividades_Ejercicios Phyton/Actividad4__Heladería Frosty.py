PrecioHeladoChocolate = 4000
PrecioHeladoVainilla = 3500
PrecioTopping = 1000

SaborHelado = input("\nIngrese el sabor de helado que desea (chocolate/vainilla): ").lower()
AgregarTopping = input("\n¿Desea agregar topping a su helado? (si/no): ").lower()

if SaborHelado == "chocolate":
    ValorTotal = PrecioHeladoChocolate
elif SaborHelado == "vainilla":
    ValorTotal = PrecioHeladoVainilla
else:
    print("\nSabor de helado no válido.")

if AgregarTopping == "si":
    PrecioTotal = ValorTotal + PrecioTopping
else:
    PrecioTotal = ValorTotal

if PrecioTotal > 0:
    print(f"\nEl precio total de su helado es: ${PrecioTotal}\n")