-- Insert records into departments
INSERT INTO departments (department_name) VALUES
('HR'),
('Finance'),
('Engineering'),
('Marketing');

-- Insert records into employees
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