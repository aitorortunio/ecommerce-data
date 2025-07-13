# 🚀 Proyecto de Orquestación de Pipeline – Ecommerce Data

## 🎯 Objetivo

Automatizar y orquestar el pipeline ETL del proyecto de ecommerce utilizando **Prefect**. Esto permite ejecutar el proceso completo (ingesta, transformación, carga) de manera controlada, reproducible y robusta.

---

## 📁 Estructura del proyecto

/orchestration/
├── flow.py # Definición del flujo con Prefect
├── README_pipeline.md # Este archivo
└── /outputs/ # (opcional) Carpeta con artefactos del pipeline

/etl/
├── load_staging.py # Carga archivos CSV y los guarda como .parquet
├── transform_clean.py # Genera tablas limpias desde staging
├── load_to_database.py # Inserta datos en PostgreSQL

/analytics/
├── generate_kpis.py # Ejecuta consultas SQL y guarda KPIs como CSV
├── generate_visuals.py # Genera gráficos con matplotlib a partir de KPIs
├── /output/ # KPIs exportados (.csv)
└── /visuals/ # Gráficos (.png) generados automáticamente


---

## 🔄 Descripción del flujo (`flow.py`)

El flujo ejecuta las siguientes tareas en orden:

1. **load_staging**: carga los CSV desde `/model/` y los convierte en archivos `.parquet` en la capa de staging
2. **transform_clean**: transforma los archivos de staging y genera tablas `dim_users`, `dim_products`, `fct_orders`
3. **load_to_database**: carga los datos limpios a PostgreSQL en sus tablas respectivas

### 📌 Dependencias entre tareas

```text
load_staging → transform_clean → load_to_database
```

