import pandas as pd
import psycopg2
from pathlib import Path

# -----------------------------
# Conexión a PostgreSQL
# -----------------------------
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "ecommerce"

conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# -----------------------------
# Directorio de salida
# -----------------------------
output_dir = Path(__file__).resolve().parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Revenue mensual
# -----------------------------
query1 = """
SELECT 
    order_month,
    ROUND(SUM(total_price)::numeric, 2) AS total_revenue
FROM 
    fct_orders
GROUP BY 
    order_month
ORDER BY 
    order_month;
"""
df1 = pd.read_sql(query1, conn)
df1.to_csv(output_dir / "revenue_by_month.csv", index=False)
print("✅ KPI: Revenue mensual generado.")

# -----------------------------
# 2. Usuarios activos por mes
# -----------------------------
query2 = """
SELECT 
    order_month,
    COUNT(DISTINCT user_id) AS active_users
FROM 
    fct_orders
GROUP BY 
    order_month
ORDER BY 
    order_month;
"""
df2 = pd.read_sql(query2, conn)
df2.to_csv(output_dir / "active_users_by_month.csv", index=False)
print("✅ KPI: Usuarios activos por mes generado.")

# -----------------------------
# 3. Revenue por país (top 5)
# -----------------------------
query3 = """
SELECT 
    country,
    ROUND(SUM(total_price)::numeric, 2) AS total_revenue
FROM 
    fct_orders
JOIN 
    dim_users USING(user_id)
GROUP BY 
    country
ORDER BY 
    total_revenue DESC
LIMIT 5;
"""
df3 = pd.read_sql(query3, conn)
df3.to_csv(output_dir / "revenue_by_country.csv", index=False)
print("✅ KPI: Revenue por país (top 5) generado.")

# -----------------------------
# Cerrar conexión
# -----------------------------
conn.close()
