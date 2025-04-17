show databases;
CREATE DATABASE studentDB;
USE studentdb;
CREATE TABLE student(
	id INT NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25),
    age INT
);
SHOW TABLES;
DESCRIBE student;

ALTER TABLE student MODIFY age INT NOT NULL; 

INSERT INTO student VALUES(1,'Alex',NULL,20);
INSERT INTO student VALUES(2,NULL,NULL,20);

use librarydb;

DESCRIBE books;

DROP TABLE books;

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(20),
  author_id INT,
  publication_year INT CHECK(publication_year>0),
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
  );
  
CREATE TABLE person(
	id INT PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) UNIQUE,
    age INT
);

DESCRIBE person;

INSERT into person VALUES (1,'Alex',NULL,20);

select * from person;

INSERT into person VALUES (2,'Alex',NULL,20);

INSERT into person VALUES (3,'Alex',NULL,20);

INSERT into person VALUES (4,'Bob','XYZ',20);

INSERT into person VALUES (5,'Jane','ABC',20);


CREATE TABLE members(
id INT PRIMARY KEY,
first_name VARCHAR(25) NOT NULL,
last_name VARCHAR(25),
email VARCHAR(25) UNIQUE,
salary INT DEFAULT 22000
);

INSERT INTO members VALUES (1,'Alex',NULL,'alex@gmail.com',NULL);

SELECT * from members;

INSERT INTO members (id,first_name,email) VALUES (2,'Bob','bob@gmail.com');

CREATE index index_first_name ON members(first_name);

DESCRIBE members;


CREATE TABLE enrollment(
 student_id INT,
 course_id INT,
 enrollment_date DATE,
 PRIMARY KEY(student_id,course_id)
 );


 describe enrollment;
 
 INSERT INTO enrollment VALUES(1,1,'2024-09-09');
INSERT INTO enrollment VALUES(1,1,'2024-09-09');

SELECT * from enrollment;

DROP TABLE enrollment;
 CREATE TABLE enrollment(
 student_id INT PRIMARY KEY,
 course_id INT PRIMARY KEY,
 enrollment_date DATE
  );