-- ############################################################
-- 📊 Métricas clave para análisis de ecommerce
-- Dataset: Tablas dim_users, dim_products, fct_orders
-- ############################################################


-- 🔹 1. Top 10 productos más vendidos por cantidad de unidades
SELECT
    p.product_id,
    p.product_name,
    SUM(o.quantity) AS total_quantity,
    ROUND(SUM(o.total_price)::numeric, 2) AS total_revenue
FROM
    fct_orders o
JOIN
    dim_products p ON o.product_id = p.product_id
GROUP BY
    p.product_id, p.product_name
ORDER BY
    total_quantity DESC
LIMIT 10;


-- 🔹 2. Revenue total por país (ventas totales agrupadas por país)
SELECT
    u.country,
    ROUND(SUM(o.total_price)::numeric, 2) AS total_revenue
FROM
    fct_orders o
JOIN
    dim_users u ON o.user_id = u.user_id
GROUP BY
    u.country
ORDER BY
    total_revenue DESC;


-- 🔹 3. Valor promedio por orden en cada mes
SELECT
    order_month,
    ROUND((SUM(total_price) / COUNT(DISTINCT order_id))::numeric, 2) AS avg_order_value
FROM
    fct_orders
GROUP BY
    order_month
ORDER BY
    order_month;


-- 🔹 4. Usuarios con mayor Lifetime Value (LTV = gasto total acumulado)
SELECT
    o.user_id,
    ROUND(SUM(o.total_price)::numeric, 2) AS lifetime_value
FROM
    fct_orders o
GROUP BY
    o.user_id
ORDER BY
    lifetime_value DESC
LIMIT 10;


-- 🔹 5. Clientes con mayor cantidad de órdenes realizadas
SELECT
    user_id,
    COUNT(DISTINCT order_id) AS order_count
FROM
    fct_orders
GROUP BY
    user_id
ORDER BY
    order_count DESC
LIMIT 10;


-- 🔹 6. Primer y última compra de cada cliente + total de órdenes
-- (útil para análisis de cohortes o retención)
SELECT
    user_id,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    COUNT(order_id) AS total_orders
FROM
    fct_orders
GROUP BY
    user_id
ORDER BY
    first_order_date;


-- 🔹 7. Productos con precio promedio más alto por unidad vendida
-- (limitado a productos con más de 10 unidades vendidas para relevancia)
SELECT
    p.product_id,
    p.product_name,
    ROUND((SUM(o.total_price) / SUM(o.quantity))::numeric, 2) AS avg_price_per_unit,
    SUM(o.quantity) AS total_units
FROM
    fct_orders o
JOIN
    dim_products p ON o.product_id = p.product_id
GROUP BY
    p.product_id, p.product_name
HAVING
    SUM(o.quantity) > 10
ORDER BY
    avg_price_per_unit DESC
LIMIT 10;


-- 🔹 8. Cantidad de usuarios únicos que realizaron compras por mes
SELECT
    order_month,
    COUNT(DISTINCT user_id) AS active_users
FROM
    fct_orders
GROUP BY
    order_month
ORDER BY
    order_month;
