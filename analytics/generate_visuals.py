import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "output"
visuals_dir = base_dir / "visuals"
visuals_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Revenue mensual (línea)
# -----------------------------
revenue_path = output_dir / "revenue_by_month.csv"
df = pd.read_csv(revenue_path)

if not df.empty and {"order_month", "total_revenue"}.issubset(df.columns):
    plt.figure(figsize=(10, 5))
    plt.plot(df["order_month"], df["total_revenue"], marker="o", color="#4CAF50")
    plt.title("Revenue mensual")
    plt.xlabel("Mes")
    plt.ylabel("Revenue ($)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(visuals_dir / "revenue_by_month.png")
    plt.close()
    print("✅ Gráfico revenue mensual generado.")
else:
    print("⚠️ revenue_by_month.csv no contiene los datos esperados.")

# -----------------------------
# 2. Usuarios activos por mes (línea)
# -----------------------------
users_path = output_dir / "active_users_by_month.csv"
if users_path.exists():
    df = pd.read_csv(users_path)
    if not df.empty and {"order_month", "active_users"}.issubset(df.columns):
        plt.figure(figsize=(10, 5))
        plt.plot(df["order_month"], df["active_users"], marker="o", color="#2196F3")
        plt.title("Usuarios activos por mes")
        plt.xlabel("Mes")
        plt.ylabel("Usuarios únicos")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(visuals_dir / "active_users_by_month.png")
        plt.close()
        print("✅ Gráfico usuarios activos generado.")
    else:
        print("⚠️ active_users_by_month.csv no tiene columnas esperadas.")
else:
    print("⚠️ No se encontró active_users_by_month.csv.")

# -----------------------------
# 3. Revenue por país (top 5) - gráfico de torta
# -----------------------------
country_path = output_dir / "revenue_by_country.csv"
if country_path.exists():
    df = pd.read_csv(country_path)
    if not df.empty and {"country", "total_revenue"}.issubset(df.columns):
        plt.figure(figsize=(7, 7))
        plt.pie(df["total_revenue"], labels=df["country"], autopct="%1.1f%%", startangle=140)
        plt.title("Top 5 países por revenue")
        plt.tight_layout()
        plt.savefig(visuals_dir / "revenue_by_country.png")
        plt.close()
        print("✅ Gráfico por país generado.")
    else:
        print("⚠️ revenue_by_country.csv no tiene columnas esperadas.")
else:
    print("⚠️ No se encontró revenue_by_country.csv.")
