numero = int(input("\nIngresa un número del 1 al 100: "))

while numero < 1 or numero > 100:
    print("El número ingresado está fuera del rango válido (1-100). Inténtalo de nuevo.")
    numero = int(input("Ingresa un número: ")) 
    print(f"El número {numero} está dentro del rango válido (1-100).")