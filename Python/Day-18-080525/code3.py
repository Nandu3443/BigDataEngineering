import sqlite3

# Creating a connection to database
conn = sqlite3.connect('example.db') # file-based database
# sqlite3.connect(':memory:')  # In-memory database

#helps to execute SQL commands
cursor = conn.cursor()

# Create a table

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               department TEXT,
               salary REAL
               );
               ''')
#commit the changes
conn.commit()

#Inserting Data


# query = "INSERT INTO employees(name,department,salary) VALUES (?,?,?);"
# args_tuple = [
#     ('Alice', 'HR' , 65000.0),
#     ('Bob','Finance',72000.0),
#     ('John','IT',78000.0)
# ]
# cursor.executemany(query,args_tuple)

# conn.commit()

#Querying Data

cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()
# print(all_employees)

for employee in all_employees:
    print(employee)

print("\n\n\n")
#filtering data
query = '''SELECT * FROM employees where department=?'''
args_tuple = ('IT',)
cursor.execute(query,args_tuple)
it_employees = cursor.fetchone()
print(it_employees)

#update date

cursor.execute('''
               
UPDATE employees SET salary = ? where id = ?
''',(90000.0,1))

conn.commit()

cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()
# print(all_employees)

print("\n\n\n")
for employee in all_employees:
    print(employee)


#Delete a record 

cursor.execute('DELETE from employees where id =1;')
conn.commit()


cursor.execute("SELECT * FROM employees")
all_employees = cursor.fetchall()
# print(all_employees)

print("\n\n\n")
for employee in all_employees:
    print(employee)

cursor.close()
conn.close()

##Working with MYSQL

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="user@123",
    database="employee_db"
)


cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100) NOT NULL,
               department VARCHAR(100),
               salary Float
               );
               ''')
#commit the changes
conn.commit()

query = "INSERT INTO employees(name,department,salary) VALUES (%s,%s,%s);"
args_tuple = [
    ('Alice', 'HR' , 65000.0),
    ('Bob','Finance',72000.0),
    ('John','IT',78000.0)
]
cursor.executemany(query,tuple(args_tuple))

conn.commit()
cursor.close()
conn.close()