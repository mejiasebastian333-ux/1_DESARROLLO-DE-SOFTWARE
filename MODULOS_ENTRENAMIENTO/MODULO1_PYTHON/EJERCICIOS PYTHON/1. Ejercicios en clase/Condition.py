#Edad de una persona, si es mayor de edad puede ingresar y si es menor de edad no puede ingresar.

edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 18:
    print("Usted es menor de edad, no puede ingresar.")

elif edad >= 18:
    print("Usted es mayor de edad, puede ingresar.")

else:
    print("Edad no válida.")

print("Fin del programa")