Dulces = int(input("Ingrese la cantidad de dulces disponibles: "))
Coders = int(input("Ingrese la cantidad de coders: "))

if Dulces > 0:
    Dulcesxcoders = Dulces / Coders 
    print(f"A cada coders le corresponde {Dulces} dulce(s)")

else:
    print("Error")