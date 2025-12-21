ValorUnitarioLibro = 25000

CantidadLibros = int(input("\nIngrese la cantidad de libros que desea comprar: "))

Estudiante = input("\n¿Eres estudiante? (si/no): ").lower()
if Estudiante == "si":
    DescuentoEstudiante = ValorUnitarioLibro * 0.15
    ValorTotal = ValorUnitarioLibro - DescuentoEstudiante
    input ("Tienes un descuento del 15% por ser estudiante.")
    
    cupon = input("\n¿Tienes un cupón de descuento? (si/no): ").lower()
    if cupon == "si":
        CodigoCupon = input("\nIngrese el código de cupón: ")
        if CodigoCupon == "LIBRO10":
            DescuentoCupon = ValorTotal * 0.10
            ValorTotal = ValorTotal - DescuentoCupon
            input("Tienes un descuento adicional del 10% por usar el cupón.")
            TotalPagar = CantidadLibros * ValorTotal
            print(f"\nEl total a pagar es de: ${TotalPagar}")
        else:
            print(f"\nCódigo de cupón inválido.")
            TotalPagar = CantidadLibros * ValorTotal
            print(f"\nEl total a pagar es de: ${TotalPagar}")
    else:
        TotalPagar = CantidadLibros * ValorTotal
        print(f"\nEl total a pagar es de: ${TotalPagar}")
else:
    TotalPagar = CantidadLibros * ValorUnitarioLibro
    print(f"\nEl total a pagar sin descuento es de: ${TotalPagar}")

