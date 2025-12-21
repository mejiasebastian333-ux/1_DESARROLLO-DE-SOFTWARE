Producto1 = float(input("\nIngresa el precio del primer producto: "))
Producto2 = float(input("\nIngresa el precio del segundo producto: "))
Resultado = Producto1 + Producto2

if Producto1 < 0 or Producto2 < 0:
    print("\nError: El precio de los productos no puede ser negativo.\n")
else:
    print (f"\nEl total es {Resultado}\n") 