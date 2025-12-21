contador = 1

while contador <= 20:
    print(f"\nVehículo {contador}")

    if contador % 2 == 0:
        print("Vehículo par registrado")

    if contador == 20:
        print("Capacidad completa")

    contador += 1