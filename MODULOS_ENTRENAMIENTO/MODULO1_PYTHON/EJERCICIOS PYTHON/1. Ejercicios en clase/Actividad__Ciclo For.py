# Actividad: Ciclo For

limite = int(input("\nIngresa un número: "))

print("\nLista de números:")

for i in range(1, limite + 1):
    print (i)

if i % 2 == 0:
    print(f"\nLa posición {i} es par\n")
else:
    print(f"\nLa posición {i} es impar\n")