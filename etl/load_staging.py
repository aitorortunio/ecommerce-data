import pandas as pd
from pathlib import Path

# Crear carpeta output si no existe
output_path = Path("./output")
output_path.mkdir(parents=True, exist_ok=True)

# Leer CSVs desde la carpeta model
users = pd.read_csv("../model/users.csv")
products = pd.read_csv("../model/products.csv")
orders = pd.read_csv("../model/orders.csv", parse_dates=["order_date"])

# Guardar como archivos parquet en la capa staging
users.to_parquet(output_path / "stg_users.parquet", index=False)
products.to_parquet(output_path / "stg_products.parquet", index=False)
orders.to_parquet(output_path / "stg_orders.parquet", index=False)

print("✅ Archivos de staging guardados como .parquet")
