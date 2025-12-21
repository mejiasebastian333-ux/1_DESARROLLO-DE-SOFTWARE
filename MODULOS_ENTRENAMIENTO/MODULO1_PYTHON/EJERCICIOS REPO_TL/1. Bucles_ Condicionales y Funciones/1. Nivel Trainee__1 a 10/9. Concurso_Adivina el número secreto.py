
correcto = 3  

while True:  
    
    while True:
        numero = int(input("Ingresa un número entre 1 y 5: "))
        if 1 <= numero <= 5:
            break  
        else:
            print("Número inválido. Debe ser entre 1 y 5.")

    if numero == correcto:
        print("¡Correcto!")
        break
    else:
        print("Intenta otra vez")

