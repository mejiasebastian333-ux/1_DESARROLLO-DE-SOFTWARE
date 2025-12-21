DiasdeEntrenamiento = int(input("Ingrese el número de días de entrenamiento de esta semana: "))    

if DiasdeEntrenamiento == 0 or DiasdeEntrenamiento == 1:
    print("No aflojes, tú puedes mejorar")
    PuntosxSemana = 0
    
elif DiasdeEntrenamiento == 2 or DiasdeEntrenamiento == 3:
    print("Bien, pero puedes dar más de ti")
    PuntosxSemana = 0

elif DiasdeEntrenamiento >= 4 and DiasdeEntrenamiento <=7:
    print("¡Excelente disciplina! Has ganado 1 punto de energía.")
    PuntosxSemana = 1

else:
    print("Número de días no válido. Por favor ingrese un número entre 0 y 7.")

print(f"\nPuntos de energía obtenidos esta semana: {PuntosxSemana}")