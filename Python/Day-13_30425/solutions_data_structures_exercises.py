"""
Python Data Structures Practice Exercises with Solutions
======================================================
"""

# ========== LIST, TUPLE, SET EXERCISES ==========

"""
Exercise 1: List Manipulation
----------------------------
Create a list of your favorite movies. Then write code to:
- Add a new movie to the end
- Insert a movie at the second position
- Remove the third movie
- Sort the list alphabetically
- Print only the first three movies
"""

# Solution
favorite_movies = ["The Shawshank Redemption", "Inception", "The Dark Knight", "Pulp Fiction"]

# Add a new movie to the end
favorite_movies.append("Interstellar")
print("After adding a movie:", favorite_movies)

# Insert a movie at the second position
favorite_movies.insert(1, "The Godfather")
print("After inserting a movie:", favorite_movies)

# Remove the third movie
favorite_movies.pop(2)  # or del favorite_movies[2]
print("After removing the third movie:", favorite_movies)

# Sort the list alphabetically
favorite_movies.sort()
print("Sorted list:", favorite_movies)

# Print only the first three movies
print("First three movies:", favorite_movies[:3])


"""
Exercise 2: Tuple Operations
---------------------------
Given the tuple of monthly expenses (1200, 900, 1500, 1100, 1800):
- Find the maximum and minimum expenses
- Calculate the average monthly expense
- Convert the tuple to a list, add a new expense, and convert back to a tuple
- Try to modify an element directly (notice what happens)
"""

# Solution
monthly_expenses = (1200, 900, 1500, 1100, 1800)

# Find max and min expenses
max_expense = max(monthly_expenses)
min_expense = min(monthly_expenses)
print(f"Maximum expense: ${max_expense}")
print(f"Minimum expense: ${min_expense}")

# Calculate average expense
average_expense = sum(monthly_expenses) / len(monthly_expenses)
print(f"Average monthly expense: ${average_expense:.2f}")

# Convert tuple to list, add expense, convert back to tuple
expenses_list = list(monthly_expenses)
expenses_list.append(1300)
monthly_expenses = tuple(expenses_list)
print("Updated expenses tuple:", monthly_expenses)

# Try to modify directly
try:
    monthly_expenses[0] = 1000  # This will raise a TypeError
except TypeError as e:
    print(f"Error when trying to modify a tuple directly: {e}")


"""
Exercise 3: Set Operations
-------------------------
Given two sets of student IDs, those who take Math: {101, 103, 105, 107, 109}
and those who take Science: {102, 103, 104, 105, 108}:
- Find students who take both subjects
- Find students who take Math but not Science
- Find students who take either Math or Science but not both
- Find all unique student IDs
"""

# Solution
math_students = {101, 103, 105, 107, 109}
science_students = {102, 103, 104, 105, 108}

# Students who take both subjects (intersection)
both_subjects = math_students.intersection(science_students)  # or math_students & science_students
print("Students taking both subjects:", both_subjects)

# Students who take Math but not Science (difference)
math_only = math_students.difference(science_students)  # or math_students - science_students
print("Students taking only Math:", math_only)

# Students who take either Math or Science but not both (symmetric difference)
either_but_not_both = math_students.symmetric_difference(science_students)  # or math_students ^ science_students
print("Students taking either Math or Science but not both:", either_but_not_both)

# All unique student IDs (union)
all_students = math_students.union(science_students)  # or math_students | science_students
print("All students:", all_students)


# ========== DICTIONARY EXERCISES ==========

"""
Exercise 4: Contact Manager
--------------------------
Create a dictionary representing a contact list with names as keys and phone numbers as values.
Write code to:
- Add a new contact
- Update an existing contact's number
- Delete a contact
- Print all contacts sorted by name
- Search for a specific contact
"""

# Solution
contacts = {
    "John": "555-1234",
    "Alice": "555-5678",
    "Bob": "555-8765",
    "Emma": "555-4321"
}

# Add a new contact
contacts["Michael"] = "555-9876"
print("After adding a new contact:", contacts)

# Update an existing contact's number
contacts["Alice"] = "555-1111"
print("After updating Alice's number:", contacts)

# Delete a contact
del contacts["Bob"]  # or contacts.pop("Bob")
print("After deleting Bob:", contacts)

# Print all contacts sorted by name
print("Sorted contacts:")
for name in sorted(contacts.keys()):
    print(f"{name}: {contacts[name]}")

# Search for a specific contact
search_name = "John"
if search_name in contacts:
    print(f"Found {search_name}: {contacts[search_name]}")
else:
    print(f"{search_name} not found in contacts")


"""
Exercise 5: Frequency Counter
---------------------------
Write a function that takes a string and returns a dictionary with each character as a key
and its frequency as the value. Ignore spaces and make it case-insensitive.
"""

# Solution
def char_frequency(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Initialize empty dictionary
    freq_dict = {}
    
    # Count frequency of each character
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict

# Test the function
sample_text = "Hello World"
result = char_frequency(sample_text)
print(f"Character frequency in '{sample_text}':", result)


"""
Exercise 6: Nested Dictionaries
-----------------------------
Create a nested dictionary of students, where each student has a name, age, and a dictionary of subject grades.
Write code to:
- Add a new grade for an existing student
- Calculate each student's average grade
- Find the student with the highest grade in a specific subject
- Print a formatted report for each student
"""

# Solution
students = {
    "Alice": {
        "age": 20,
        "grades": {
            "Math": 85,
            "Science": 90,
            "History": 78
        }
    },
    "Bob": {
        "age": 22,
        "grades": {
            "Math": 92,
            "Science": 88,
            "History": 95
        }
    },
    "Charlie": {
        "age": 21,
        "grades": {
            "Math": 78,
            "Science": 85,
            "History": 80
        }
    }
}

# Add a new grade for an existing student
students["Alice"]["grades"]["English"] = 88
print("Alice's updated grades:", students["Alice"]["grades"])

# Calculate each student's average grade
print("\nAverage grades:")
for name, data in students.items():
    grades = data["grades"].values()
    avg_grade = sum(grades) / len(grades)
    print(f"{name}: {avg_grade:.2f}")

# Find the student with the highest grade in a specific subject
subject = "Math"
highest_grade = 0
best_student = ""

for name, data in students.items():
    if subject in data["grades"] and data["grades"][subject] > highest_grade:
        highest_grade = data["grades"][subject]
        best_student = name

print(f"\nStudent with highest {subject} grade: {best_student} ({highest_grade})")

# Print a formatted report for each student
print("\nStudent Reports:")
print("-" * 40)
for name, data in students.items():
    print(f"Name: {name}")
    print(f"Age: {data['age']}")
    print("Grades:")
    for subject, grade in data["grades"].items():
        print(f"  - {subject}: {grade}")
    print("-" * 40)


# ========== COMPREHENSION EXERCISES ==========

"""
Exercise 7: List Comprehension
----------------------------
Use list comprehensions to solve the following:
- Generate a list of squares for numbers 1 to 20
- Filter out all odd numbers from a list of integers
- Create a list of tuples containing numbers and their cubes for numbers 1 to 10
- Convert a string to a list of ASCII values for each character
"""

# Solution

# Generate a list of squares for numbers 1 to 20
squares = [n**2 for n in range(1, 21)]
print("Squares from 1 to 20:", squares)

# Filter out all odd numbers from a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers only:", even_numbers)

# Create a list of tuples containing numbers and their cubes for numbers 1 to 10
number_cubes = [(n, n**3) for n in range(1, 11)]
print("Numbers and their cubes:", number_cubes)

# Convert a string to a list of ASCII values for each character
text = "Python"
ascii_values = [ord(char) for char in text]
print(f"ASCII values for '{text}':", ascii_values)


"""
Exercise 8: Dictionary Comprehension
----------------------------------
Use dictionary comprehensions to:
- Create a dictionary mapping numbers 1-10 to their squares
- Invert a dictionary (swap keys and values)
- Create a dictionary filtering out items with values less than 10 from an existing dictionary
- Generate a word-length dictionary from a sentence
"""

# Solution

# Create a dictionary mapping numbers 1-10 to their squares
square_dict = {n: n**2 for n in range(1, 11)}
print("Number to square mapping:", square_dict)

# Invert a dictionary (swap keys and values)
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)

# Create a dictionary filtering out items with values less than 10 from an existing dictionary
scores = {"Alice": 15, "Bob": 8, "Charlie": 12, "David": 7}
high_scores = {name: score for name, score in scores.items() if score >= 10}
print("Scores:", scores)
print("High scores (>=10):", high_scores)

# Generate a word-length dictionary from a sentence
sentence = "Python is a powerful programming language"
word_lengths = {word: len(word) for word in sentence.split()}
print("Word lengths:", word_lengths)


"""
Exercise 9: Combined Data Structures
----------------------------------
Given a list of dictionaries representing products with 'name', 'price', and 'category' keys:
- Use a list comprehension to filter products by category
- Use a dictionary comprehension to create a price lookup by product name
- Create a dictionary with categories as keys and lists of product names as values
- Find the average price per category using comprehensions and dictionaries
"""

# Solution
products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Headphones", "price": 150, "category": "Electronics"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Coffee Mug", "price": 12, "category": "Kitchen"},
    {"name": "Novel", "price": 20, "category": "Books"},
    {"name": "Keyboard", "price": 80, "category": "Electronics"}
]

# Filter products by category
electronics = [product for product in products if product["category"] == "Electronics"]
print("\nElectronics products:", electronics)

# Create a price lookup by product name
price_lookup = {product["name"]: product["price"] for product in products}
print("\nPrice lookup dictionary:", price_lookup)

# Create a dictionary with categories as keys and lists of product names as values
products_by_category = {}
for product in products:
    category = product["category"]
    if category in products_by_category:
        products_by_category[category].append(product["name"])
    else:
        products_by_category[category] = [product["name"]]
        
print("\nProducts by category:", products_by_category)

# Using comprehension (alternative approach)
category_names = {}
for product in products:
    category_names.setdefault(product["category"], []).append(product["name"])
print("\nProducts by category (alt method):", category_names)

# Find the average price per category
category_prices = {}
for product in products:
    category = product["category"]
    if category in category_prices:
        category_prices[category].append(product["price"])
    else:
        category_prices[category] = [product["price"]]

avg_price_by_category = {category: sum(prices)/len(prices) 
                        for category, prices in category_prices.items()}
print("\nAverage price by category:", avg_price_by_category)


"""
Exercise 10: Data Transformation Challenge
----------------------------------------
Given raw data about employees, use a combination of data structures and comprehensions to transform it into a structured format:
- Parse a CSV-like string into a list of employee dictionaries
- Group employees by department
- Calculate average salary by department
- Find the highest-paid employee in each department
"""

# Solution
# Raw CSV-like data (name, age, department, salary)
raw_data = """
John,28,Engineering,85000
Alice,32,Marketing,78000
Bob,35,Engineering,92000
Emma,27,HR,67000
Michael,41,Marketing,110000
Lisa,34,HR,72000
David,38,Engineering,115000
"""

# Parse the data into a list of dictionaries
lines = [line.strip() for line in raw_data.strip().split('\n')]
employees = []

for line in lines:
    name, age, department, salary = line.split(',')
    employees.append({
        'name': name,
        'age': int(age),
        'department': department,
        'salary': int(salary)
    })

print("\nEmployee data:")
for emp in employees:
    print(emp)

# Group employees by department
employees_by_dept = {}
for emp in employees:
    dept = emp['department']
    if dept in employees_by_dept:
        employees_by_dept[dept].append(emp)
    else:
        employees_by_dept[dept] = [emp]

print("\nEmployees grouped by department:")
for dept, emps in employees_by_dept.items():
    print(f"{dept}: {[emp['name'] for emp in emps]}")

# Calculate average salary by department
avg_salary_by_dept = {}
for dept, emps in employees_by_dept.items():
    total_salary = sum(emp['salary'] for emp in emps)
    avg_salary_by_dept[dept] = total_salary / len(emps)

print("\nAverage salary by department:")
for dept, avg_salary in avg_salary_by_dept.items():
    print(f"{dept}: ${avg_salary:.2f}")

# Find the highest-paid employee in each department
highest_paid_by_dept = {}
for dept, emps in employees_by_dept.items():
    highest_paid = max(emps, key=lambda emp: emp['salary'])
    highest_paid_by_dept[dept] = {
        'name': highest_paid['name'],
        'salary': highest_paid['salary']
    }

print("\nHighest-paid employee by department:")
for dept, emp_info in highest_paid_by_dept.items():
    print(f"{dept}: {emp_info['name']} (${emp_info['salary']})")
