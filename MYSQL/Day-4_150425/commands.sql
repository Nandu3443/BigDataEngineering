CREATE DATABASE companyDB;
USE companyDB;
CREATE TABLE employees(
	employeeID INT,
    firstName varchar(50),
    lastName varchar(50),
    email VARCHAR(50),
    hireDate DATE,
    salary DECIMAL(10,2)
);
show tables;

describe employees;


INSERT INTO employees VALUES (1,'John','Doe','John.doe@mail.com','2025-01-02',50000.00,NULL);

SELECT * FROM employees;

INSERT INTO employees VALUES (2,'Alex',NULL,'alex@mail.com','2025-01-04',50000.00,NULL);
INSERT INTO employees VALUES (3,'Bob',NULL,'bob@mail.com','2025-01-04',50000.00,NULL);

SELECT * FROM employees WHERE lastname is null;

UPDATE employees SET email = 'jhon.doe@mail.com' WHERE employeeid = 1;

INSERT INTO employees VALUES (1,'Bob','Doe','bob.doe@mail.com','2025-01-02',50000.00);

-- Deleting single record 

DELETE FROM employees WHERE firstName = 'Bob';

-- DELETE Multiple Records 

DELETE FROM employees WHERE lastname is NULL; 

-- COMPLETE DELETE of records 

DELETE FROM employees;



ALTER TABLE employees 
ADD COLUMN phone_number VARCHAR(25),
ADD COLUMN date_of_birth VARCHAR(25);

ALTER TABLE employees
MODIFY COLUMN phone_number VARCHAR(20);

ALTER TABLE employees
MODIFY COLUMN salary INT;

ALTER TABLE employees
CHANGE COLUMN lastname middlename VARCHAR(50);

ALTER TABLE employees 
DROP COLUMN date_of_birth,
DROP COLUMN phone_number;


CREATE DATABASE librarydb;

USE librarydb;

CREATE TABLE authors(
	author_id INT PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    email VARCHAR(25)
);

DESCRIBE authors;

INSERT INTO authors VALUES (1,'Chris','Joe','chris@email.com');
INSERT INTO authors VALUES (2,'Alex','Jane','alex@email.com');

SELECT * fROM authors;

INSERT INTO authors VALUES (1,'Chris','Joe','chris@email.com');

ALTER TABLE employees 
MODIFY employeeID INT PRIMARY KEY;


ALTER TABLE employees
DROP PRIMARY KEY;

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(20),
  author_id INT,
  publication_year INT,
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
  );
  
describe books;

INSERT INTO books VALUES (1,'Harry Potter',1,2022);
INSERT INTO books VALUES (2,'Another Book',2,2023);
  
select * from books;
