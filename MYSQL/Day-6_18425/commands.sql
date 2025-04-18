CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department_id INT,
    hire_date DATE NOT NULL,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

SHOW TABLES;

INSERT INTO departments (department_name) VALUES
('HR'),
('Finance'),
('Engineering'),
('Marketing');

INSERT INTO employees (first_name, last_name, salary, department_id, hire_date, manager_id) VALUES
('Alice', 'Smith', 75000, 1, '2020-01-15', NULL),
('Bob', 'Johnson', 60000, 2, '2019-03-10', 1),
('Charlie', 'Brown', 90000, 3, '2021-06-01', 2),
('Diana', 'Prince', 85000, 3, '2020-09-12', 2),
('Eve', 'Davis', 50000, 4, '2022-02-20', 3),
('Frank', 'Miller', 45000, 4, '2023-05-05', 3),
('Grace', 'Lee', 70000, 1, '2021-11-11', NULL),
('Hannah', 'White', 95000, 2, '2018-07-22', 1),
('Ian', 'Black', 48000, 4, '2023-01-10', 3),
('Jack', 'Green', 82000, 3, '2019-12-05', 2);


SELECT * FROM departments ;
SELECT * FROM employees;


-- Operators 
SELECT * FROM employees WHERE department_id  = 3;

SELECT * FROM employees WHERE department_id  != 3;

SELECT * FROM employees WHERE salary > 80000;

SELECT * FROM employees WHERE salary < 50000;

SELECT * FROM employees WHERE salary >= 80000;

SELECT * FROM employees WHERE salary <= 50000;

SELECT * FROM employees WHERE salary BETWEEN 50000 AND 60000;

SELECT first_name FROM employees WHERE first_name like 'A%';

SELECT * FROM employees WHERE manager_id is  NULL;


-- Logical operators

SELECT * FROM employees WHERE salary > 60000 AND department_id  = 3 ;

SELECT * FROM employees WHERE salary > 97000 OR department_id  = 2 ;

SELECT * FROM employees WHERE NOT department_id = 1;

SELECT * FROM employees WHERE salary > 60000 AND department_id  = 3  AND manager_id = 2;
SELECT * FROM employees WHERE (salary > 60000 AND department_id  = 3)  OR manager_id != 2;

-- Aggregate Functions
SELECT count(*) from employees;

SELECT SUM(salary) from employees;

SELECT SUM(salary) from employees where department_id = 2;

SELECT * FROM employees ;

SELECT AVG(salary) from employees ;

SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary from employees;

-- Group by and Having 
SELECT department_id, count(*) AS total_employees FROM employees GROUP BY department_id;

SELECT department_id, AVG(salary) AS avg_salary FROM employees GROUP BY department_id HAVING avg_salary < 60000;

SELECT department_id,count(*) FROM employees  WHERE salary > 60000 GROUP BY department_id;

-- Keyword based operators
 SELECT first_name AS employee_name from employees WHERE department_id IN (1,3);
  SELECT first_name AS employee_name from employees WHERE department_id NOT IN (1,3);
  
-- CASE statements 
  SELECT first_name, salary,
			CASE
				 WHEN salary > 80000 THEN 'High'
				 WHEN salary BETWEEN 50000 AND 80000 THEN 'Medium'
                 ELSE 'Low'
			END as salary_category,
            CASE 
				WHEN department_id =  1 THEN 'HR'
                WHEN department_id = 2 THEN 'Finance'
                WHEN department_id = 3 THEN 'Eng'
                 WHEN department_id = 4 THEN 'Sales'
				ELSE 'NA'
			END as department
FROM employees;


-- STRING FUNCTIONS

SELECT CONCAT(first_name,' ',last_name)   AS full_name FROM employees;  

SELECT UPPER(first_name)   AS upper_name FROM employees;          
            
-- DATE FUNCTIONS

SELECT first_name ,DATEDIFF(CURDATE(),hire_date) AS days_worked FROM employees;

SELECT first_name ,DATE_FORMAT(hire_date,'%d %M %y') AS date_joined FROM employees; 
 
SELECT first_name ,DATE_FORMAT(hire_date,'%d-%m-%Y') AS date_joined FROM employees; 
            
-- OTHERS

SELECT first_name, salary from employees ORDER BY salary DESC;

SELECT first_name, salary from employees limit 2;

SELECT first_name, salary from employees  limit 2 offset 2;
