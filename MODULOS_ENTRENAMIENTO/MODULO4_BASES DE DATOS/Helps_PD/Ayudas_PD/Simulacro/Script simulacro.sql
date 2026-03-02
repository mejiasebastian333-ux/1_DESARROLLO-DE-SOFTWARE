
-- Aquí se importan los datos del CSV desde DBeaver.
CREATE TABLE food_delivery_orders_raw (
    order_id UUID PRIMARY KEY,
    customer_name VARCHAR(150),
    restaurant_name VARCHAR(150),
    delivery_address TEXT,
    food_items TEXT,
    total_cost NUMERIC(10,2),
    delivery_status VARCHAR(50),
    order_time TIMESTAMP,
    estimated_delivery_time TIMESTAMP,
    payment_status VARCHAR(50)
);


-- Se crean las tablas con base al DER o Modelo relacional Normalizado
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    delivery_address TEXT NOT NULL
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE orders (
    id UUID PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    restaurant_id INTEGER REFERENCES restaurants(id),
    total_cost NUMERIC(10,2) NOT NULL,
    delivery_status VARCHAR(50),
    order_time TIMESTAMP,
    estimated_delivery_time TIMESTAMP,
    payment_status VARCHAR(50)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id UUID REFERENCES orders(id) ON DELETE CASCADE,
    food_item TEXT NOT NULL
);


-- Se migran los datos desde la tabla que se construyó con base al excel hacía las tablas normalizadas
INSERT INTO customers (name, delivery_address)
SELECT DISTINCT customer_name, delivery_address
FROM food_delivery_orders_raw;

INSERT INTO restaurants (name)
SELECT DISTINCT restaurant_name
FROM food_delivery_orders_raw;

INSERT INTO orders (
    id,
    customer_id,
    restaurant_id,
    total_cost,
    delivery_status,
    order_time,
    estimated_delivery_time,
    payment_status
)
SELECT 
    r.order_id,
    c.id,
    res.id,
    r.total_cost,
    r.delivery_status,
    r.order_time,
    r.estimated_delivery_time,
    r.payment_status
FROM food_delivery_orders_raw r
JOIN customers c 
    ON r.customer_name = c.name
   AND r.delivery_address = c.delivery_address
JOIN restaurants res 
    ON r.restaurant_name = res.name;

-- El campo food_items viene como texto con varios productos separados por coma. Hay que separarlos
INSERT INTO order_items (order_id, food_item)
SELECT 
    order_id,
    TRIM(item)
FROM (
    SELECT 
        order_id,
        unnest(string_to_array(food_items, ',')) AS item
    FROM food_delivery_orders_raw
) sub;

-- Verificar que todo esté bien relacionado
SELECT 
    o.id,
    c.name,
    res.name,
    oi.food_item
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN restaurants res ON o.restaurant_id = res.id
JOIN order_items oi ON oi.order_id = o.id;






-- Consultas

/* ========================================================= */
/* ===================== NIVEL BÁSICO ====================== */
/* ========================================================= */

/* 1️⃣ Listar todos los pedidos con cliente y restaurante */
SELECT 
    o.id,
    c.name AS customer,
    r.name AS restaurant,
    o.total_cost,
    o.delivery_status,
    o.payment_status
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN restaurants r ON o.restaurant_id = r.id;


/* 2️⃣ Ver los productos de un pedido específico */
SELECT 
    o.id,
    oi.food_item
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
WHERE o.id = 'UUID_AQUI';


/* 3️⃣ Pedidos entregados */
SELECT *
FROM orders
WHERE delivery_status = 'Delivered';



/* ========================================================= */
/* ================== NIVEL INTERMEDIO ===================== */
/* ========================================================= */

/* 4️⃣ Total gastado por cliente */
SELECT 
    c.name,
    SUM(o.total_cost) AS total_spent
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.name
ORDER BY total_spent DESC;


/* 5️⃣ Cantidad de pedidos por restaurante */
SELECT 
    r.name,
    COUNT(o.id) AS total_orders
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.id
GROUP BY r.name
ORDER BY total_orders DESC;


/* 6️⃣ Promedio de valor de pedido */
SELECT 
    AVG(total_cost) AS average_order_value
FROM orders;


/* 7️⃣ Clientes con más de 1 pedido */
SELECT 
    c.name,
    COUNT(o.id) AS total_orders
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.name
HAVING COUNT(o.id) > 1;



/* ========================================================= */
/* ==================== NIVEL AVANZADO ===================== */
/* ========================================================= */

/* 8️⃣ Restaurante con mayores ingresos */
SELECT 
    r.name,
    SUM(o.total_cost) AS total_revenue
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.id
GROUP BY r.name
ORDER BY total_revenue DESC
LIMIT 1;


/* 9️⃣ Producto más vendido */
SELECT 
    food_item,
    COUNT(*) AS times_ordered
FROM order_items
GROUP BY food_item
ORDER BY times_ordered DESC
LIMIT 1;


/* 🔟 Pedidos con más de 2 productos */
SELECT 
    o.id,
    COUNT(oi.id) AS total_items
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id
HAVING COUNT(oi.id) > 2;


/* 1️⃣1️⃣ Pedidos entregados pero no pagados */
SELECT *
FROM orders
WHERE delivery_status = 'Delivered'
AND payment_status != 'Paid';


/* 1️⃣2️⃣ Tiempo estimado de entrega en minutos */
SELECT 
    id,
    EXTRACT(EPOCH FROM (estimated_delivery_time - order_time)) / 60 AS estimated_minutes
FROM orders;


/* 1️⃣3️⃣ Clientes cuyo gasto total está por encima del promedio */
SELECT 
    c.name,
    SUM(o.total_cost) AS total_spent
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.name
HAVING SUM(o.total_cost) > (
    SELECT AVG(total_cost) * COUNT(*)
    FROM orders
);

