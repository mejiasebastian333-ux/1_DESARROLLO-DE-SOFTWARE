numero_de_repeticiones = int(input("\nIngresa la cantidad de repeticioes a realizar: "))

for repeticiones in range (1, numero_de_repeticiones + 1):
    print(f"\nRepetición #{repeticiones} completada")
    
    if numero_de_repeticiones % 3 == 0:
        print("¡Excelente ritmo!\n")
        