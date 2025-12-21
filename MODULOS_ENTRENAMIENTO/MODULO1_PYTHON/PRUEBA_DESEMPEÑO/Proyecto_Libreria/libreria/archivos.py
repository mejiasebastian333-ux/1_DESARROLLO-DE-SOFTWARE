# libreria/archivos.py
import csv
import os
from datetime import datetime

ENCODING = "utf-8"

# --- Helpers ---
def _asegurar_ruta_csv(ruta_input: str, default_name: str) -> str:
    """
    Recibe la entrada del usuario. Si está vacía -> usa ./data/default_name.
    Si es carpeta -> añade default_name. Si no tiene .csv -> añade .csv.
    Retorna la ruta final.
    """
    ruta = ruta_input.strip()
    if not ruta:
        ruta = os.path.join("data", default_name)
    elif os.path.isdir(ruta):
        ruta = os.path.join(ruta, default_name)
    else:
        # si es ruta de archivo, asegurarse extensión
        if not ruta.lower().endswith(".csv"):
            ruta = ruta + ".csv"
    # crear carpeta si necesita
    carpeta = os.path.dirname(ruta) or "."
    os.makedirs(carpeta, exist_ok=True)
    return ruta

def _leer_csv_generico(ruta: str, expected_header: list):
    """
    Lee CSV y devuelve (lista, num_omitidos).
    Mapea los encabezados esperados a claves internas (minúsculas, sin espacios).
    Si falta archivo -> retorna [], 0
    """
    if not os.path.exists(ruta):
        return [], 0

    lista = []
    omitidos = 0
    with open(ruta, newline='', encoding=ENCODING) as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [], 0

        # normalizar header: strip
        header = [h.strip() for h in header]

        # comprobar que al menos los nombres esperados están presentes (no estricto)
        missing = [h for h in expected_header if h not in header]
        if missing:
            # no coincide encabezado
            raise ValueError(f"Encabezado inválido en {ruta}. Faltan: {missing}")

        for row in reader:
            if len(row) < len(header):
                omitidos += 1
                continue
            row = [c.strip() for c in row]
            d = {header[i]: row[i] for i in range(len(header))}
            lista.append(d)
    return lista, omitidos

def _escribir_csv_simple(ruta: str, header: list, lista_de_filas: list):
    with open(ruta, "w", newline='', encoding=ENCODING) as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in lista_de_filas:
            writer.writerow(row)

# --- Inventario ---
def cargar_inventario(ruta: str = None):
    ruta = ruta or os.path.join("data", "inventario.csv")
    expected = ["Titulo", "Autor", "Categoria", "Precio", "Stock", "Total"]
    try:
        datos, omitidos = _leer_csv_generico(ruta, expected)
    except ValueError as e:
        raise e
    # mapear a estructura interna: keys en minúscula
    inventario = []
    for row in datos:
        try:
            precio = float(row["Precio"])
        except:
            precio = 0.0
        try:
            stock = int(float(row["Stock"]))
        except:
            stock = 0
        try:
            total = float(row.get("Total", precio * stock))
        except:
            total = precio * stock
        inventario.append({
            "titulo": row["Titulo"],
            "autor": row["Autor"],
            "categoria": row["Categoria"],
            "precio": f"{precio:.2f}",
            "stock": str(stock),
            "total": f"{total:.2f}"
        })
    return inventario, omitidos

def guardar_inventario_prompt(inventario):
    entrada = input("Ingrese la ruta o carpeta donde guardar inventario (Enter = ./data): ")
    ruta = _asegurar_ruta_csv(entrada, "inventario.csv")
    header = ["Titulo", "Autor", "Categoria", "Precio", "Stock", "Total"]
    filas = []
    for lib in inventario:
        filas.append([
            lib.get("titulo",""),
            lib.get("autor",""),
            lib.get("categoria",""),
            lib.get("precio","0.00"),
            lib.get("stock","0"),
            lib.get("total", str(float(lib.get("precio",0))*int(lib.get("stock",0))))
        ])
    _escribir_csv_simple(ruta, header, filas)
    print(f"Inventario guardado en: {ruta}")

# --- Clientes ---
def cargar_clientes(ruta: str = None):
    ruta = ruta or os.path.join("data", "clientes.csv")
    expected = ["Nombre", "Documento", "NumeroCelular", "Correo"]
    try:
        datos, omitidos = _leer_csv_generico(ruta, expected)
    except ValueError as e:
        raise e
    clientes = []
    for row in datos:
        clientes.append({
            "nombre": row["Nombre"],
            "documento": row["Documento"],
            "celular": row["NumeroCelular"],
            "correo": row["Correo"]
        })
    return clientes, omitidos

def guardar_clientes_prompt(clientes):
    entrada = input("Ingrese la ruta o carpeta donde guardar clientes (Enter = ./data): ")
    ruta = _asegurar_ruta_csv(entrada, "clientes.csv")
    header = ["Nombre", "Documento", "NumeroCelular", "Correo"]
    filas = []
    for c in clientes:
        filas.append([c.get("nombre",""), c.get("documento",""), c.get("celular",""), c.get("correo","")])
    _escribir_csv_simple(ruta, header, filas)
    print(f"Clientes guardados en: {ruta}")

# --- Ventas ---
def cargar_ventas(ruta: str = None):
    ruta = ruta or os.path.join("data", "ventas.csv")
    expected = ["DocumentoCliente", "TituloLibro", "Cantidad", "PrecioUnitario", "Subtotal", "Fecha"]
    try:
        datos, omitidos = _leer_csv_generico(ruta, expected)
    except ValueError as e:
        raise e
    ventas = []
    for row in datos:
        try:
            cantidad = int(float(row["Cantidad"]))
        except:
            cantidad = 0
        try:
            precio = float(row["PrecioUnitario"])
        except:
            precio = 0.0
        try:
            subtotal = float(row.get("Subtotal", cantidad * precio))
        except:
            subtotal = cantidad * precio
        ventas.append({
            "documento_cliente": row["DocumentoCliente"],
            "titulo_libro": row["TituloLibro"],
            "cantidad": str(cantidad),
            "precio_unitario": f"{precio:.2f}",
            "subtotal": f"{subtotal:.2f}",
            "fecha": row["Fecha"]
        })
    return ventas, omitidos

def guardar_ventas_prompt(ventas):
    entrada = input("Ingrese la ruta o carpeta donde guardar ventas (Enter = ./data): ")
    ruta = _asegurar_ruta_csv(entrada, "ventas.csv")
    header = ["DocumentoCliente", "TituloLibro", "Cantidad", "PrecioUnitario", "Subtotal", "Fecha"]
    filas = []
    for v in ventas:
        filas.append([
            v.get("documento_cliente",""),
            v.get("titulo_libro",""),
            v.get("cantidad","0"),
            v.get("precio_unitario","0.00"),
            v.get("subtotal","0.00"),
            v.get("fecha","")
        ])
    _escribir_csv_simple(ruta, header, filas)
    print(f"Ventas guardadas en: {ruta}")
