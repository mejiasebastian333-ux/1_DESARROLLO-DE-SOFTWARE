# libreria/reportes.py
from collections import Counter, defaultdict

def top_n_vendidos(ventas, n=3):
    contador = Counter()
    for v in ventas:
        try:
            cantidad = int(float(v.get("cantidad",0)))
        except:
            cantidad = 0
        contador[v.get("titulo_libro")] += cantidad
    top = contador.most_common(n)
    print(f"\n--- Top {n} libros más vendidos ---\n")
    if not top:
        print("No hay ventas registradas.\n")
        return
    for i,(titulo,cant) in enumerate(top, start=1):
        print(f"{i}. {titulo} — {cant} unidades")
    print()

def ventas_totales_por_autor(ventas, inventario):
    # mapa titulo->autor
    mapa = {lib.get("titulo"): lib.get("autor") for lib in inventario}
    por_autor = defaultdict(int)
    for v in ventas:
        try:
            cantidad = int(float(v.get("cantidad",0)))
        except:
            cantidad = 0
        autor = mapa.get(v.get("titulo_libro"), "Autor desconocido")
        por_autor[autor] += cantidad
    print("\n--- Ventas totales por autor (unidades) ---\n")
    if not por_autor:
        print("No hay ventas registradas.\n")
        return
    for autor, total in por_autor.items():
        print(f"{autor}: {total}")
    print()

def ingreso_bruto_neto(ventas):
    bruto = 0.0
    for v in ventas:
        try:
            bruto += float(v.get("subtotal",0.0))
        except:
            pass
    neto = bruto  # sin descuentos en el modelo actual
    print("\n--- Ingresos ---\n")
    print(f"Ingreso bruto: ${bruto:,.2f}")
    print(f"Ingreso neto : ${neto:,.2f}\n")
    return bruto, neto
