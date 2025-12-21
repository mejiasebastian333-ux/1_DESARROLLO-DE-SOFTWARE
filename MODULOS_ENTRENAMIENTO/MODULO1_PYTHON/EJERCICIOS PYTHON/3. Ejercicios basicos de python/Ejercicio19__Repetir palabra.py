palabra = str(input("\nIngresa una palabra: "))
Repeticiones = int(input("\n¿Cuántas veces quieres repetir la palabra?:"))

while Repeticiones <= 0:
    print("\nEl número de repeticiones debe ser mayor que cero.")
    Repeticiones = int(input("\nPor favor, ingresa un número válido de repeticiones: "))

print("\nResultado:\n") 
for i in range (Repeticiones):
    print(f"{i+1}. {palabra}")
print("\n¡Proceso completado!\n")   