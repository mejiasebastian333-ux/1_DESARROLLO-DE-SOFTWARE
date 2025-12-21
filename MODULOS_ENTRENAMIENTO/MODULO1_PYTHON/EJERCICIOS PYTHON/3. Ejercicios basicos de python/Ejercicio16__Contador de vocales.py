palabra = input("\nIngresa una palabra: ")
contador_consonantes = 0
contador_vocales = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales += 1
    else:
        contador_consonantes += 1

print(f"\nLa palabra '{palabra}' tiene {contador_vocales} vocales y {contador_consonantes} consonantes.\n")