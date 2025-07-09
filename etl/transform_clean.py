import pandas as pd
from pathlib import Path

# Leer datos desde staging (parquet)
path = Path("./output")
stg_users = pd.read_parquet(path / "stg_users.parquet")
stg_products = pd.read_parquet(path / "stg_products.parquet")
stg_orders = pd.read_parquet(path / "stg_orders.parquet")

# --- CLEANED LAYER ---

# 1. dim_users (limpiar duplicados, ordenar)
dim_users = stg_users.drop_duplicates(subset=["user_id"]).sort_values("user_id")
dim_users.to_parquet(path / "dim_users.parquet", index=False)

# 2. dim_products (limpiar duplicados, ordenar)
dim_products = stg_products.drop_duplicates(subset=["product_id"]).sort_values("product_id")
dim_products.to_parquet(path / "dim_products.parquet", index=False)

# 3. fct_orders (validar joins y agregar columnas)
fct_orders = stg_orders.copy()

# Asegurarse de que todas las claves estén en las dimensiones
fct_orders = fct_orders[
    fct_orders["user_id"].isin(dim_users["user_id"]) &
    fct_orders["product_id"].isin(dim_products["product_id"])
]

# Agregar columna mes (útil para analytics)
fct_orders["order_month"] = fct_orders["order_date"].dt.to_period("M").astype(str)

fct_orders.to_parquet(path / "fct_orders.parquet", index=False)

print("✅ Archivos cleaned generados (dim y fct) en formato .parquet")
