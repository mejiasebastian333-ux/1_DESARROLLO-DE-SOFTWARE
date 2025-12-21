numero = int(input("\nIngresa un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")