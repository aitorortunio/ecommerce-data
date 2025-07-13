import pandas as pd
from pathlib import Path

# BASE_DIR es la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Crear carpeta output si no existe
output_path = BASE_DIR / "etl" / "output"
output_path.mkdir(parents=True, exist_ok=True)

# Leer CSVs desde carpeta /model/
users = pd.read_csv(BASE_DIR / "model" / "users.csv")
products = pd.read_csv(BASE_DIR / "model" / "products.csv")
orders = pd.read_csv(BASE_DIR / "model" / "orders.csv", parse_dates=["order_date"])

# Guardar como .parquet
users.to_parquet(output_path / "stg_users.parquet", index=False)
products.to_parquet(output_path / "stg_products.parquet", index=False)
orders.to_parquet(output_path / "stg_orders.parquet", index=False)

print("✅ Archivos de staging guardados como .parquet")
