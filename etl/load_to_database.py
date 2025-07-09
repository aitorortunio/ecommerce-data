import pandas as pd
from sqlalchemy import create_engine

# 1. Conexión a PostgreSQL
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "ecommerce"  # <-- Asegurate de que esta DB exista, o cambiala

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# 2. Leer los .parquet desde /etl/output
path = "./output/"
dim_users = pd.read_parquet(path + "dim_users.parquet")
dim_products = pd.read_parquet(path + "dim_products.parquet")
fct_orders = pd.read_parquet(path + "fct_orders.parquet")

# 3. Subir tablas a PostgreSQL
dim_users.to_sql("dim_users", engine, if_exists="replace", index=False)
print("✅ Tabla dim_users subida")

dim_products.to_sql("dim_products", engine, if_exists="replace", index=False)
print("✅ Tabla dim_products subida")

fct_orders.to_sql("fct_orders", engine, if_exists="replace", index=False)
print("✅ Tabla fct_orders subida")

engine.dispose()
