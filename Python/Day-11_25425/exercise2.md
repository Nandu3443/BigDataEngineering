### 1. **Variables and Data Types**
**Exercise:**  
Create a program that calculates the total cost of items in a shopping cart.  
- Define variables for the price of three items (e.g., `item1_price`, `item2_price`, `item3_price`) and their quantities.  
- Calculate the total cost and print it.

**Example:**  
```python
item1_price = 10.5
item1_quantity = 2
# Define similar variables for item2 and item3
# Calculate total cost and print
```

---

### 2. **Type Casting**
**Exercise:**  
Write a program that asks the user for their age as a string, converts it to an integer, and calculates the year they were born. Assume the current year is 2025.

**Example:**  
```python
# Input: "25"
# Output: "You were born in 2000."
```

---

### 3. **Input/Output**
**Exercise:**  
Create a program that asks the user for their name and favorite color, then prints a personalized greeting.

**Example:**  
```python
# Input: "Alice", "blue"
# Output: "Hello Alice! Your favorite color is blue."
```

---

### 4. **String Operations and Formatting**
**Exercise:**  
Write a program that takes a sentence as input and performs the following:  
- Counts the number of words.  
- Converts the sentence to uppercase.  
- Replaces all spaces with underscores.

**Example:**  
```python
# Input: "Python is fun"
# Output: "Words: 3, Uppercase: PYTHON IS FUN, Modified: Python_is_fun"
```

---

### 5. **Conditional Statements**
**Exercise:**  
Create a program that determines if a person is eligible to vote.  
- Input: Age of the person.  
- Output: "Eligible to vote" if age is 18 or above, otherwise "Not eligible."

**Example:**  
```python
# Input: 20
# Output: "Eligible to vote"
```

---

### 6. **Loops**
**Exercise 1:**  
Write a program that prints all even numbers between 1 and 50 using a `for` loop.

**Exercise 2:**  
Create a program that keeps asking the user for a number until they enter a negative number. Use a `while` loop.

**Example:**  
```python
# Input: 5, 10, -1
# Output: "You entered a negative number. Exiting."
```

---

### 7. **Functions**
**Exercise 1:**  
Write a function `calculate_area` that takes the radius of a circle as input and returns its area. Use the formula `area = π * r^2`.

**Exercise 2:**  
Create a function `is_palindrome` that checks if a given string is a palindrome (reads the same backward as forward).

**Example:**  
```python
# Input: "radar"
# Output: True
```

---

### 8. **Combining Concepts**
**Exercise:**  
Create a program that simulates a simple ATM.  
- Ask the user for a PIN (use input).  
- If the PIN is correct, display a menu with options: Check Balance, Deposit, Withdraw, Exit.  
- Use functions for each operation and loops to keep the program running until the user chooses to exit.

**Example:**  
```python
# Input: "1234"
# Output: "Welcome! Choose an option: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit"
```

---

for the above topics i learnt in python provide me exercises to practice, considering all aspects form the questions on use-cases providing examples

GitHub Copilot: Okay, here are some Python exercises based on the topics you listed, designed around real-world use cases with examples:

---

### 1. **Variables and Data Types**
**Exercise:**
You are planning a road trip. Create a program to calculate the estimated fuel cost.
- Define variables for the distance of the trip (in kilometers, e.g., `distance_km`), the car's fuel efficiency (in kilometers per liter, e.g., `fuel_efficiency_kpl`), and the price of fuel per liter (e.g., `fuel_price_per_liter`).
- Calculate the total liters of fuel needed (`total_fuel_liters = distance_km / fuel_efficiency_kpl`).
- Calculate the total fuel cost (`total_cost = total_fuel_liters * fuel_price_per_liter`).
- Print the total fuel cost, formatted to two decimal places.

**Example:**
````python
distance_km = 500.0  # float
fuel_efficiency_kpl = 15.5 # float
fuel_price_per_liter = 1.75 # float

# Calculate total fuel needed
total_fuel_liters = distance_km / fuel_efficiency_kpl

# Calculate total cost
total_cost = total_fuel_liters * fuel_price_per_liter

# Print the result
print(f"Estimated fuel cost for the trip: ${total_cost:.2f}")
# Expected Output: Estimated fuel cost for the trip: $56.45
````

---

### 2. **Type Casting**
**Exercise:**
Write a program that asks a user for the temperature in Celsius as input (which will be a string) and converts it to Fahrenheit.
- Get the temperature in Celsius using `input()`.
- Convert the input string to a floating-point number using `float()`.
- Apply the conversion formula: `Fahrenheit = (Celsius * 9/5) + 32`.
- Print the result in a user-friendly format.

**Example:**
````python
celsius_str = input("Enter temperature in Celsius: ")

# Convert string input to float
celsius_float = float(celsius_str)

# Calculate Fahrenheit
fahrenheit = (celsius_float * 9/5) + 32

# Print the result
print(f"{celsius_float}°C is equal to {fahrenheit}°F")

# Input: "25"
# Output: 25.0°C is equal to 77.0°F
````

---

### 3. **Input/Output**
**Exercise:**
Create a simple Mad Libs-style game.
- Ask the user to input various words: a noun, a verb, an adjective, and an adverb.
- Use these inputs to fill in the blanks in a pre-written story or sentence.
- Print the completed story.

**Example:**
````python
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(f"\n--- Your Story ---")
print(f"The {adjective} {noun} {verb} {adverb} down the street.")

# Input: "dog", "ran", "happy", "quickly"
# Output:
# --- Your Story ---
# The happy dog ran quickly down the street.
````

---

### 4. **String Operations and Formatting**
**Exercise:**
Write a program that takes a full name (e.g., "John Jacob Doe") as input and extracts the initials.
- Get the full name as input.
- Split the name into parts (first, middle, last) using `split()`.
- Get the first letter of each part.
- Join the initials together, perhaps with periods.
- Print the original name and the extracted initials.

**Example:**
````python
full_name = input("Enter your full name: ")

name_parts = full_name.split() # Splits the string into a list of words

initials = ""
for part in name_parts:
    initials += part[0].upper() + "." # Get first letter, uppercase it, add a period

print(f"Full Name: {full_name}")
print(f"Initials: {initials}")

# Input: "ada lovelace"
# Output:
# Full Name: ada lovelace
# Initials: A.L.
````

---

### 5. **Conditional Statements**
**Exercise:**
Create a program that suggests an activity based on the weather.
- Ask the user for the weather condition (e.g., "sunny", "rainy", "snowy").
- Use `if`, `elif`, and `else` to suggest an activity:
    - "sunny": "Go for a picnic or a walk."
    - "rainy": "Read a book or watch a movie."
    - "snowy": "Build a snowman or go skiing."
    - Otherwise: "Stay home and relax."
- Print the suggestion.

**Example:**
````python
weather = input("What's the weather like today? (sunny, rainy, snowy): ").lower() # Convert to lowercase

if weather == "sunny":
    suggestion = "Go for a picnic or a walk."
elif weather == "rainy":
    suggestion = "Read a book or watch a movie."
elif weather == "snowy":
    suggestion = "Build a snowman or go skiing."
else:
    suggestion = "Stay home and relax."

print(f"Suggestion: {suggestion}")

# Input: "Rainy"
# Output: Suggestion: Read a book or watch a movie.
````

---

### 6. **Loops**
**Exercise 1 (`for` loop):**
Write a program that calculates the factorial of a number entered by the user. The factorial of a non-negative integer `n`, denoted by `n!`, is the product of all positive integers less than or equal to `n`. (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120). Use a `for` loop.

**Example:**
````python
num_str = input("Enter a non-negative integer: ")
num = int(num_str)
factorial = 1

if num < 0:
   print("Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   # Use range from 1 up to and including num
   for i in range(1, num + 1):
       factorial = factorial * i
   print(f"The factorial of {num} is {factorial}")

# Input: "5"
# Output: The factorial of 5 is 120
````

**Exercise 2 (`while` loop, `break`):**
Create a simple number guessing game.
- Generate a secret number (or just hardcode one for simplicity, e.g., `secret_number = 7`).
- Use a `while True` loop to repeatedly ask the user to guess the number.
- Inside the loop, get the user's guess (convert to `int`).
- Use `if`/`elif`/`else` to check if the guess is too high, too low, or correct.
- If correct, print a success message and use `break` to exit the loop.
- If incorrect, provide a hint ("Too high" or "Too low").

**Example:**
````python
secret_number = 7
print("Guess the secret number (between 1 and 10)")

while True:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number}.")
        break # Exit the loop
    elif guess < secret_number:
        print("Too low. Try again.")
    else: # guess > secret_number
        print("Too high. Try again.")

# Input sequence: 5, 9, 7
# Output sequence:
# Guess the secret number (between 1 and 10)
# Enter your guess: 5
# Too low. Try again.
# Enter your guess: 9
# Too high. Try again.
# Enter your guess: 7
# Congratulations! You guessed the number 7.
````

---

### 7. **Functions**
**Exercise 1 (Definition, Arguments, Return):**
Write a function `calculate_discount` that takes the original price and a discount percentage as input.
- The function should calculate the discounted price.
- The function should return the final price after applying the discount.
- Call the function with sample values and print the result.

**Example:**
````python
import math # Needed for rounding if desired, but not strictly required

def calculate_discount(original_price, discount_percent):
  """Calculates the price after applying a discount."""
  if not (0 <= discount_percent <= 100):
      return "Invalid discount percentage. Must be between 0 and 100."
  discount_amount = original_price * (discount_percent / 100)
  final_price = original_price - discount_amount
  return final_price

# Example usage
price = 150.0
discount = 20.0 # 20% discount
final_price = calculate_discount(price, discount)

if isinstance(final_price, str): # Check if function returned an error message
    print(final_price)
else:
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {discount}%")
    print(f"Final Price: ${final_price:.2f}")

# Output:
# Original Price: $150.00
# Discount: 20.0%
# Final Price: $120.00
````

**Exercise 2 (Function for Logic):**
Create a function `is_prime` that takes an integer as input and returns `True` if the number is a prime number (greater than 1 and only divisible by 1 and itself), and `False` otherwise.

**Example:**
````python
import math

def is_prime(number):
  """Checks if a number is prime."""
  if number <= 1:
    return False # Numbers less than or equal to 1 are not prime
  if number <= 3:
    return True # 2 and 3 are prime
  if number % 2 == 0 or number % 3 == 0:
    return False # Eliminate multiples of 2 and 3 quickly

  # Check potential factors from 5 up to sqrt(number)
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6 # Check factors 6k ± 1
  return True

# Example usage
num1 = 29
num2 = 15

print(f"Is {num1} prime? {is_prime(num1)}")
print(f"Is {num2} prime? {is_prime(num2)}")

# Output:
# Is 29 prime? True
# Is 15 prime? False
````

---

### 8. **Combining Concepts**
**Exercise:**
Create a simple command-line calculator.
- Use a `while True` loop to keep the calculator running.
- Inside the loop, prompt the user to enter an operation (`+`, `-`, `*`, `/`) or `quit` to exit.
- If the user enters `quit`, `break` the loop.
- If the user enters a valid operation:
    - Prompt for two numbers (use `input` and `float` for type casting).
    - Define separate functions for `add`, `subtract`, `multiply`, and `divide`.
    - Use `if`/`elif`/`else` to call the appropriate function based on the chosen operation.
    - Handle potential errors like division by zero within the `divide` function.
    - Print the result.
- If the user enters an invalid operation, print an error message.

**Example Interaction:**
````
Enter operation (+, -, *, /) or 'quit': +
Enter first number: 10
Enter second number: 5
Result: 15.0
Enter operation (+, -, *, /) or 'quit': /
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero.
Enter operation (+, -, *, /) or 'quit': *
Enter first number: 3.5
Enter second number: 2
Result: 7.0
Enter operation (+, -, *, /) or 'quit': quit
Calculator exiting.
````

*(Self-contained code for the calculator is omitted here for brevity, but it would involve defining the functions `add(a, b)`, `subtract(a, b)`, etc., and structuring the `while` loop with `input` and `if`/`elif`/`else` as described).*

---