Puntos_Iniciales = int(input("Ingresa la cantidad inicial de puntos: "))

if Puntos_Iniciales > 0:
    Puntos_perdidos = int(input("Ingresa la cantidad de puntos perdidos: "))

    if Puntos_perdidos > 0:
        Resultado = Puntos_Iniciales - Puntos_perdidos
        print(f"El total de puntos es {Resultado}")
    else:
        print("El valor a restar debe ser un número positivo.")
else:
    print("La cantidad inicial de puntos debe ser mayor que cero.")