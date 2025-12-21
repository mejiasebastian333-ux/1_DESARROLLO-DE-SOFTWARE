total = 0

for mes in range (1, 7):
    ahorro = float(input(f"\nIngrese el ahorro del mes {mes}: "))
    total += ahorro
    
    if total > 1000000:
        print("\nMeta alcanzada")

print(f"\nEl ahorro total durante los 6 meses es de: ${total}")