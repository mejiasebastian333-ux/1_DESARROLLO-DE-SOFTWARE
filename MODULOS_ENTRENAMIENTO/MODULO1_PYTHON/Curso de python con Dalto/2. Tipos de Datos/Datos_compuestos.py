###Un dato compuesto es una estructura que puede almacenar múltiples valores en una sola variable.

### La lista es una colección ordenada (Con posiciones) y mutable (se puede modificar) de elementos.
Lista = [3, "Sebastian", 3.14, True] # Elementos (Desde 1) y posiciones (Desde 0) #Entre corchetes y separados por comas
print(Lista [1])  # Acceder a la posicion 1 (segundo elemento) de la lista 



### La tupla es similar a la lista, pero es inmutable (no se puede modificar después de su creación).
Tupla = (2, "Laura", 3.71, False) # Entre paréntesis y separados por comas
print(Tupla[3])  # Acceder a la posicion 3 (cuarto elemento) de la tupla



### El conjunto es una colección no ordenada (sin posiciones definidas) y sin elementos duplicados.
Conjunto = {1, 2, 3, 4, 5} # Entre llaves y separados por comas
print(Conjunto)  # Imprime el conjunto completo (el orden puede variar)



### El diccionario es una colección de pares clave-valor, donde cada clave es única.
Diccionario = { 
    'Clave': "Valor",
    'nombre': "Carlos", 
    'edad': 28,
    'ciudad': "Madrid"
} 
# Entre llaves, con pares clave-valor separados por comas y cada clave y valor separados por dos puntos
print(Diccionario['edad'])  # Acceder al valor asociado a la clave "edad" en el diccionario 