import pandas as pd

df = pd.read_csv('../model/retail_data.csv', encoding='ISO-8859-1')

# Ver las primeras filas
print("Primeras filas:")
print(df.head())

# Ver las columnas y tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Ver cantidad de filas y columnas
print(f"\nShape del dataset: {df.shape}")

# Ver valores nulos por columna
print("\nValores nulos:")
print(df.isnull().sum())

# Ver cantidad de valores únicos por columna
print("\nValores únicos por columna:")
print(df.nunique())

# Estadísticas numéricas básicas
print("\nResumen estadístico:")
print(df.describe())

# Ver columnas únicas tipo string (como Country, Description)
print("\nPaíses únicos:")
print(df['Country'].unique())