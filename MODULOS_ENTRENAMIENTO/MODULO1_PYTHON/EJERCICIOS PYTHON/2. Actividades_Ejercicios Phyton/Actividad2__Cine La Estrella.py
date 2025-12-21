edad = int(input("Ingrese su edad: "))

if edad < 5 and edad > 0:
    print("Su entrada es gratis")

elif edad >= 5 and edad <= 11:
    print("El precio de su entrada es de $5.000")

elif edad >= 12 and edad <= 59:
    print("El precio de su entrada es de $8.000")

elif edad >= 60:
    print("\nEl precio de su entrada es de $4.000 (Descuento de adulto mayor)")

else:
    print("Edad no válida.")    

print("Gracias por preferir Cine La Estrella")