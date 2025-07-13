# 🛒 Ecommerce Data Pipeline

Este proyecto simula un ecosistema de datos para un negocio de ecommerce, abordando el flujo completo desde la ingesta de datos crudos hasta la generación de KPIs y visualizaciones, utilizando buenas prácticas de ingeniería y análisis de datos.

---

## 🎯 Objetivo del proyecto

Diseñar y ejecutar un pipeline de datos completo que cubra:

- Modelado dimensional basado en un esquema en estrella
- ETL automatizado en Python (con pandas)
- Almacenamiento en base de datos PostgreSQL
- Orquestación del flujo con **Prefect**
- Generación automática de KPIs y visualizaciones
- Buenas prácticas de versionado y modularidad

---

## 🧱 Estructura del repositorio

/ecommerce-data/
│
├── model/ # Simulación de datos crudos + modelo estrella
│ ├── retail_data.csv
│ ├── users.csv, products.csv, orders.csv
│ └── README_model.md
│
├── etl/ # Scripts de carga, transformación y staging
│ ├── load_staging.py
│ ├── transform_clean.py
│ ├── load_to_database.py
│ └── output/ # Archivos .parquet por capa
│
├── analytics/ # Capa final de análisis
│ ├── generate_kpis.py
│ ├── generate_visuals.py
│ ├── output/ # CSVs de métricas
│ └── visuals/ # Gráficos generados (.png)
│
├── orchestration/ # Orquestación completa con Prefect
│ ├── flow.py
│ └── README_pipeline.md
│
├── README.md # Este archivo
└── requirements.txt # (opcional) Dependencias del proyecto

---

## ⚙️ Tecnologías utilizadas

- **Python 3.11+**
- **pandas**, **matplotlib**
- **Prefect** (orquestación)
- **PostgreSQL** (almacenamiento relacional)
- **SQLAlchemy**, **psycopg2**
- **pgAdmin** (exploración de datos)

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio y crear un entorno virtual (opcional)
```bash
git clone https://github.com/aitorortunio/ecommerce-data.git
cd ecommerce-data
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Asegurar que PostgreSQL esté corriendo
    Base de datos: ecommerce

    Usuario: postgres

    Contraseña: postgres

    Puerto: 5432 (por defecto)

Podés modificar estos valores en load_to_database.py si es necesario.

### 4. Ejecutar el flujo de orquestación
```bash
python orchestration/flow.py
```

# 🙋 Autor

Este proyecto fue desarrollado por Aitor Ortuño como práctica personal de Data Science & Analytics.
Se enfoca en aplicar conceptos reales de modelado de datos, ETL y orquestación con herramientas actuales.