suma = float(input("\nIngresa un número: "))

while True:
    numero = float(input("\nAñade un número para ser sumado (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"\nLa suma total es: {suma}\n")
