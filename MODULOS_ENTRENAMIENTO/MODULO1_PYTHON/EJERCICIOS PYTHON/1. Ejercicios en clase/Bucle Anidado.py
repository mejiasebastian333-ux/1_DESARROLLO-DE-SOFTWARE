print("Inicio del programa: \n")

TotalVueltasCuadra = int(input("Ingrese el total de vueltas a realizar: "))
TotalVueltasCancha = int(input("Ingrese el total de vueltas a la cancha por cada vuelta a la cuadra: "))

for i in range (0, TotalVueltasCuadra + 1):
    for j in range (0, TotalVueltasCancha + 1):
        print(f"i={i}, j={j}")

print("\nFin del programa.")