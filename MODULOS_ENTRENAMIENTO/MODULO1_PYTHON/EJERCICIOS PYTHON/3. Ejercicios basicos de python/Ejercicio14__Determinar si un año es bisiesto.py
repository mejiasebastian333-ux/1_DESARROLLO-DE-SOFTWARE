Año = int(input("\nIngresa un año: "))

if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
    print(f"\nEl año {Año} es bisiesto.\n")
else:
    print(f"\nEl año {Año} no es bisiesto.\n")