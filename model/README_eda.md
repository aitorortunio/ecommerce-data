# 🛍️ Modelado de Datos - Proyecto Ecommerce

## 📌 Descripción general

Este modelo corresponde a un mini ecosistema de datos para un negocio de ecommerce, basado en el dataset [**Online Retail**](https://archive.ics.uci.edu/dataset/352/online+retail). El objetivo de esta etapa es simular la capa de staging y construir un modelo estrella (star schema) que represente la relación entre usuarios, productos y órdenes de compra.

---

## 🧱 Archivos incluidos

| Archivo                   | Descripción                            |
|---------------------------|----------------------------------------|
| `retail_data.csv`         | Dataset original crudo en formato CSV  |
| `users.csv`               | Dimensión de usuarios                  |
| `products.csv`            | Dimensión de productos                 |
| `orders.csv`              | Tabla de hechos (órdenes de compra)    |
| `star_schema_diagram.png` | Diagrama del modelo estrella           |
| `README_model.md`         | Documento explicativo del modelo       |

---

## 🧠 Transformaciones aplicadas

Se aplicaron las siguientes reglas de limpieza y normalización:

- Eliminación de filas con `CustomerID` nulo (no asociables a un usuario)
- Remoción de devoluciones (facturas con código que comienza con `"C"`)
- Filtrado de productos con `Quantity` ≤ 0 o `UnitPrice` ≤ 0
- Normalización de strings (`Description`, `Country`) mediante `.strip()`

---

## ⭐ Modelo estrella (Star Schema)

Se diseñó un modelo en estrella compuesto por:

### 🔷 Dimensiones

#### `dim_users` (users.csv)
| Campo     | Tipo     | Descripción                      |
|-----------|----------|----------------------------------|
| user_id   | int      | Identificador único del usuario  |
| country   | string   | País del cliente                 |

#### `dim_products` (products.csv)
| Campo        | Tipo    | Descripción                      |
|--------------|---------|----------------------------------|
| product_id   | string  | Código del producto              |
| product_name | string  | Descripción del producto         |
| unit_price   | float   | Precio unitario                  |

### 🔶 Tabla de hechos

#### `fct_orders` (orders.csv)
| Campo        | Tipo     | Descripción                                |
|--------------|----------|--------------------------------------------|
| order_id     | string   | Número de factura (ID de la orden)         |
| user_id      | int      | Cliente que realizó la compra              |
| product_id   | string   | Producto comprado                          |
| order_date   | datetime | Fecha de la compra                         |
| quantity     | int      | Cantidad de unidades compradas             |
| unit_price   | float    | Precio unitario en ese momento             |
| total_price  | float    | `quantity * unit_price`                    |

---

## 🔄 Relaciones del modelo

- Cada orden está relacionada a **un usuario** (`user_id`)
- Cada orden está relacionada a **un producto** (`product_id`)
- Se asume que el `unit_price` puede cambiar entre órdenes

---

## 🗂️ Carpeta `/model/`

