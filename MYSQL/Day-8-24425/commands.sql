show databases;
use ecommerce;
show tables;

select * from products;
select * from order_items;

-- subqueries single-row
SELECT * from customers where customer_id = (select customer_id from orders where order_id = (select order_id from order_items where product_id = (select product_id 
from products where name = 'Backpack')));

-- join
SELECT c.customer_id,c.name,c.email,c.city FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id INNER JOIN order_items oi on o.order_id = oi.order_id INNER JOIN 
products p ON oi.product_id = p.product_id WHERE p.name = 'Backpack'; 


-- subqueries multi-row
-- Subquery operators using IN NOT IN , ANY, ALL, EXISTS, NOT EXISTS 
select * from orders;

select customer_id,name,email from customers where customer_id IN (SELECT customer_id from orders where customer_id is not null); 


SELECT customer_id,name,email from customers
where customer_id  NOT IN (SELECT customer_id from orders WHERE customer_id is not null);


SELECT product_id,name,price from products WHERE price > ALL(select price from products where category='Accessories');

SELECT product_id,name,price from products WHERE price > ANY(select price from products where category='Kitchen');


select customer_id,name,email from customers c where EXISTS (SELECT 1 FROM orders o where o.customer_id = c.customer_id ); 


SELECT customer_id,name,email from customers c
where NOT EXISTS (SELECT 1 from orders o WHERE c.customer_id = o.customer_id);

-- Subquery SELECT clause  

select * from customers;

SELECT c.customer_id, c.name, (SELECT o.order_date from orders o where o.customer_id = c.customer_id) AS order_date FROM customers c
WHERE C.name = 'Bob Johnson';


SELECT p.product_id,p.name, p.price, (SELECT count(*) from order_items oi where oi.product_id = p.product_id) AS times_ordered FROM products p;

-- Subquery FROM clause 
SELECT  cat_stats.category, cat_stats.avg_price, cat_stats.num_products FROM
(SELECT category,AVG(price) AS avg_price, count(*) AS num_products from products GROUP BY category) AS cat_stats
WHERE cat_stats.num_products >1;

SELECT * from products;

-- CHECKING COST BTW JOIN & SubQuery
-- subquery 
EXPLAIN ANALYZE SELECT * from customers where customer_id = (select customer_id from orders where order_id = (select order_id from order_items where product_id = (select product_id 
from products where name = 'Backpack')));

-- join
EXPLAIN ANALYZE SELECT c.customer_id,c.name,c.email,c.city FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id INNER JOIN order_items oi on o.order_id = oi.order_id INNER JOIN 
products p ON oi.product_id = p.product_id WHERE p.name = 'Backpack';

--  subquery in DELETE
DELETE from customers
where customer_id  NOT IN (SELECT customer_id from orders WHERE customer_id is not null);

--  subquery in UPDATE
SELECT * from customers;

 SELECT * from orders where customer_id in (select customer_id from customers);
 
 UPDATE orders SET total_amount = total_amount+1 where customer_id in (select customer_id from customers);
 
 --  subquery in INSERT
 DESCRIBE customers;
 
INSERT INTO customers (customer_id,name,email,city)  SELECT customer_id+1,name,email,city from customers c where customer_id = 3;

SELECT customer_id+1,name,email,city from customers c where customer_id = 3;

INSERT INTO customers (customer_id,name,email,city)  SELECT customer_id+1,'Alex' as name ,email,city from customers c where customer_id = 4;
 
 SELECT * from customers;
 
 