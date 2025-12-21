def calcular_propina(total_cuenta):
    # Determinar porcentaje de propina
    if total_cuenta > 100000:
        propina = total_cuenta * 0.15
    else:
        propina = total_cuenta * 0.10

    # Calcular total final
    total_final = total_cuenta + propina

    # Mostrar resultados
    print("")
    print(f"=> Total de la cuenta: ${total_cuenta:,.0f}")
    print(f"=> Propina aplicada: ${propina:,.0f}")
    print(f"=> Total final a pagar: ${total_final:,.0f}")
    print("")
    return total_final


# Ejemplo de uso
cuenta = float(input("\nIngresa el total de la cuenta: "))
calcular_propina(cuenta)
