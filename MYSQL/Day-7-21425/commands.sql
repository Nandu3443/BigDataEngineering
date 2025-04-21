SHOW TABLES;

select * from customers;

DESCRIBE customers;

DESCRIBE orders;

-- INNER JOIN 
-- GET all customers with their orders
SELECT c.customer_id , c.name , o.order_id, o.order_date, o.total_amount FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT JOIN 
-- Get all customers and their order(including customer with no orders) 
SELECT * FROM orders; 

SELECT c.customer_id , c.name , o.order_id, o.order_date, o.total_amount FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- RIGHT JOIN 
-- Get all order and their customer(including orders without customers) 
SELECT * FROM orders; 

SELECT  o.order_id, c.customer_id , c.name ,o.order_date, o.total_amount FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- CROSS JOIN
--  Get all possible combinations of products and customers

SELECT c.name , p.name FROM customers c CROSS JOIN products p;

-- SELF JOIN
-- Get all employees with their managers  
DESCRIBE employees;   

SELECT e.name, m.name FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id;


-- Multitable-Join
-- Get Customer, their orders and the products they purchased  


SELECT c.name,o.order_id,p.name,oi.quantity from customers c 
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id;

