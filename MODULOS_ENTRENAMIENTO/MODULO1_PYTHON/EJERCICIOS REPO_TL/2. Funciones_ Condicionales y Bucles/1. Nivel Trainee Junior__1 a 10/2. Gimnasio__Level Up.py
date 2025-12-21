def repeticiones (n):

    for repeticion in range (1, n + 1):
        print(f"\nRepetición #{repeticion} completada")
        
    if n % 2 == 0:
            print("¡Excelente forma!\n")
            print("")
        
    else:
            print("Mantén el ritmo")
            print("")

n = int(input("\nIngresa la cantidad de repeticiones a realizar: "))
repeticiones (n)
