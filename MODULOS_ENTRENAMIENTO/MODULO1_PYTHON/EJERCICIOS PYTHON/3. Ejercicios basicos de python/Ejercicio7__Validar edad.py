Edad = int(input("\nIngresa tu edad: "))

if Edad < 18 and Edad > 0:
    print("\nEres menor de edad.\n")
elif Edad >= 18:
    print("\nEres mayor de edad.\n")
else:
    print("\nEdad no valida.\n")    