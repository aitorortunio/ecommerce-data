# ⚙️ ETL - Ecommerce Project

## 📁 Estructura del módulo `/etl/`

| Archivo                | Descripción                                         |
|------------------------|-----------------------------------------------------|
| `load_staging.py`      | Carga los CSV de `/model/` y los guarda como `.parquet` en `/etl/output/` |
| `transform_clean.py`   | Limpieza y transformación de datos: generación de `dim_users`, `dim_products`, `fct_orders` |
| `load_to_database.py`  | Inserta las tablas finales en PostgreSQL           |
| `/output/`             | Archivos de staging y cleaned en formato `.parquet` |

---

## 🧱 Capas del pipeline

### 1. 📦 Staging
- Fuente: `users.csv`, `products.csv`, `orders.csv`
- Formato: `.parquet`
- Ubicación: `/etl/output/stg_*.parquet`

### 2. 🧹 Cleaned
- Tablas generadas:
  - `dim_users.parquet`
  - `dim_products.parquet`
  - `fct_orders.parquet`
- Validaciones aplicadas:
  - Remoción de duplicados
  - Consistencia de claves entre hechos y dimensiones
  - Derivación de columna `order_month`

### 3. 🛢️ Carga en PostgreSQL
- Base de datos destino: `ecommerce`
- Tablas creadas:
  - `dim_users`
  - `dim_products`
  - `fct_orders`
- Herramienta de conexión: `SQLAlchemy`

---

## 🧪 Validaciones realizadas

- Comprobación de unicidad en claves primarias de dimensiones
- Revisión manual de tablas en pgAdmin
- Filtrado de órdenes sin correspondencia válida en dimensiones

