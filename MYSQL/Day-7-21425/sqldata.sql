-- Create database
CREATE DATABASE ecommerce;
USE ecommerce;

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    category VARCHAR(50)
);

-- Create order_items table (junction table)
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create employees table for self-join example
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Insert sample data
INSERT INTO customers VALUES 
(1, 'John Smith', 'john@example.com', 'New York'),
(2, 'Jane Doe', 'jane@example.com', 'Los Angeles'),
(3, 'Bob Johnson', 'bob@example.com', 'Chicago'),
(4, 'Alice Brown', 'alice@example.com', 'Miami');

INSERT INTO orders VALUES
(101, 1, '2023-01-15', 150.75),
(102, 1, '2023-02-20', 89.99),
(103, 2, '2023-01-25', 245.50),
(104, 3, '2023-03-10', 45.25),
(105, NULL, '2023-03-15', 199.99);

INSERT INTO products VALUES
(201, 'Laptop', 899.99, 'Electronics'),
(202, 'Headphones', 89.99, 'Electronics'),
(203, 'Coffee Maker', 49.99, 'Kitchen'),
(204, 'Running Shoes', 79.99, 'Clothing'),
(205, 'Backpack', 45.25, 'Accessories');

INSERT INTO order_items VALUES
(101, 201, 1),
(101, 202, 1),
(102, 202, 1),
(103, 203, 2),
(103, 204, 1),
(104, 205, 1);

INSERT INTO employees VALUES
(301, 'Sarah Connor', 'CEO', NULL),
(302, 'Mike Johnson', 'Sales Manager', 301),
(303, 'Lisa Brown', 'Marketing Manager', 301),
(304, 'Tom Wilson', 'Sales Rep', 302),
(305, 'Amy Lee', 'Sales Rep', 302),
(306, 'David Chen', 'Marketing Specialist', 303);