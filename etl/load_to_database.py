import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Definir la raíz del proyecto y la ruta a los archivos .parquet
BASE_DIR = Path(__file__).resolve().parent.parent
output_path = BASE_DIR / "etl" / "output"

# Conexión a PostgreSQL
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "ecommerce"

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# Leer .parquet
dim_users = pd.read_parquet(output_path / "dim_users.parquet")
dim_products = pd.read_parquet(output_path / "dim_products.parquet")
fct_orders = pd.read_parquet(output_path / "fct_orders.parquet")

# Subir a PostgreSQL
dim_users.to_sql("dim_users", engine, if_exists="replace", index=False)
print("✅ Tabla dim_users subida")

dim_products.to_sql("dim_products", engine, if_exists="replace", index=False)
print("✅ Tabla dim_products subida")

fct_orders.to_sql("fct_orders", engine, if_exists="replace", index=False)
print("✅ Tabla fct_orders subida")

engine.dispose()
