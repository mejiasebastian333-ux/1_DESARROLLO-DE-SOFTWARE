
###Las variables se declaran y se definen mediante el signo igual (=)
variablesDesarrolloDeSoftware = "Hola, Mundo!"      #Camel Case
variables_Desarrollo_de_Software = "Hola, Mundo!"   #Snake Case (Recomendado)


###Las variables se pueden modificar reasignandoles un nuevo valor
variablesDesarrolloDeSoftware = "Hola, Python!"
variables_Desarrollo_de_Software = "Hola, Python!"


#Las variables se pueden eliminar usando la palabra clave 'del'
del variablesDesarrolloDeSoftware
del variables_Desarrollo_de_Software


###Las variables deben seguir ciertas reglas:
# 1. Deben comenzar con una letra o un guion bajo (_) 
# 2. No pueden comenzar con un numero
# 3. Solo pueden contener letras, numeros y guiones bajos
# 4. No pueden ser palabras reservadas del lenguaje Python
# 5. Son sensibles a mayusculas y minusculas (case-sensitive)

#Ejemplos de nombres de variables validos
variable1 = "Valido"  # Comienza con una letra y contiene un numero
_variable = "Valido"  # Comienza con un guion bajo
mi_variable = "Valido"  # Contiene guion bajo (_)   

#Ejemplos de nombres de variables invalidos
#1variable = "Invalido"  # Comienza con un numero   
#mi-variable = "Invalido" # Contiene un guion medio (-)
#for = "Invalido" # Palabra reservada




###Las variables se pueden concatenar usando el operador +
saludo = "Hola"
nombre = "Ana"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)  # Salida: Hola, Ana!



###Las variables se pueden formatear usando f-strings
nombre = "Ana"
edad = 30
mensaje_formateado = f"{nombre} tiene {edad} años." #La f se usa para llamar variables dentro de cadenas de texto
print(mensaje_formateado)  # Salida: Ana tiene 30 años.



############################################################################################



###Operadores de pertenencia (in \ not in)
Color= "Negro"
frase = f"Su camisa es de color {Color}"
print("Negro" in frase)  #Salida: True
print("Azul" not in frase)  #Salida: True 

#(Se deben tener en cuenta los espacios y mayusculas/minusculas al usar estos operadores)





