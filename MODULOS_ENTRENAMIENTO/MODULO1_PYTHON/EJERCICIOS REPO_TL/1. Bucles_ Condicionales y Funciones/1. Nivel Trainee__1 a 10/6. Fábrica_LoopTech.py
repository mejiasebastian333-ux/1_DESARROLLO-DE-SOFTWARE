
numeroFinal = int(input("\nIngrese la cantidad de productos fabricados: "))

for producto in range (1, numeroFinal + 1):
    print(f"Producto: {producto}")
    
    if producto % 2 == 0:
        print("-> Producto verificado")     
    else:
        print("-> Producto pendiente")
    
    print()
