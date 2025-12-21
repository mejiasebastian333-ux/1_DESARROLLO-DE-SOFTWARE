## if anidados y else if(elif)

ingresoMensual = 81000
gastoMensual = 80000

if ingresoMensual > 10000:
    if ingresoMensual-gastoMensual < 0:
        print("Estás en dificit")
        
    elif ingresoMensual-gastoMensual > 3000:
        print("Estás bien")
    
    else:
        print("Estás gastando un montón, hay que ver si te alcanza")
        
elif ingresoMensual > 1000:
    print("Estás bien en Latinoamerica")

elif ingresoMensual > 500:
    print("Estás bien en Argentina")

elif ingresoMensual > 200:
    print("Estás bien en Venezuela")
    
else:
    print("Complicada la situación")

