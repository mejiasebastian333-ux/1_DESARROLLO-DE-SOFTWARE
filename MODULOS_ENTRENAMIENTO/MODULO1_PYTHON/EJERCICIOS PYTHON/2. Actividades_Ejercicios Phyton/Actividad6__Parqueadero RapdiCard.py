
horas = float(input("Ingrese la cantidad de horas en el parqueadero: "))

if horas < 0:
    print("Error: No se permiten números negativos.")
else:
    
    if horas <= 5:
        total = horas * 2000
    else:
        total = (horas * 2000) + 5000 

    print(f"El valor total a pagar es: ${total:,.0f}")
