import pandas as pd
from pathlib import Path

# Ruta al CSV original
input_path = Path("../model/retail_data.csv")
output_dir = Path("../model/")
output_dir.mkdir(exist_ok=True)

# Leer el dataset con codificación especial
df = pd.read_csv(input_path, encoding='ISO-8859-1')

# -----------------------------
# FILTROS DE LIMPIEZA BÁSICOS
# -----------------------------

# 1. Eliminar filas con CustomerID nulo (no podríamos relacionarlas a users)
df = df[df['CustomerID'].notnull()]

# 2. Eliminar devoluciones (InvoiceNo que empiezan con "C")
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# 3. Eliminar productos con cantidad o precio <= 0
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# 4. Quitar espacios y normalizar strings
df['Description'] = df['Description'].str.strip()
df['Country'] = df['Country'].str.strip()

# -----------------------------
# users.csv
# -----------------------------
users = df[['CustomerID', 'Country']].drop_duplicates()
users = users.rename(columns={'CustomerID': 'user_id', 'Country': 'country'})
users['user_id'] = users['user_id'].astype(int)
users.to_csv(output_dir / 'users.csv', index=False)

# -----------------------------
# products.csv
# -----------------------------
products = df[['StockCode', 'Description', 'UnitPrice']].drop_duplicates()
products = products.rename(columns={
    'StockCode': 'product_id',
    'Description': 'product_name',
    'UnitPrice': 'unit_price'
})
products['product_id'] = products['product_id'].astype(str)
products.to_csv(output_dir / 'products.csv', index=False)

# -----------------------------
# orders.csv
# -----------------------------
orders = df[['InvoiceNo', 'CustomerID', 'StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice']].copy()
orders = orders.rename(columns={
    'InvoiceNo': 'order_id',
    'CustomerID': 'user_id',
    'StockCode': 'product_id',
    'InvoiceDate': 'order_date',
    'Quantity': 'quantity',
    'UnitPrice': 'unit_price'
})
orders['user_id'] = orders['user_id'].astype(int)
orders['product_id'] = orders['product_id'].astype(str)
orders['order_date'] = pd.to_datetime(orders['order_date'])
# Calculamos el precio total por orden
orders['total_price'] = orders['quantity'] * orders['unit_price']
orders.to_csv(output_dir / 'orders.csv', index=False)

print("✅ ¡Archivos CSV generados con éxito en la carpeta /model/!")
