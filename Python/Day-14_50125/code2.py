# a = 10
# b = int(input("Enter b value:"))
# #Simple Try-Except Block
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero try with > 0")

# print("code execution is done..")


# # Multiple Except Blocks

# try:
#     value = int(input("enter a number"))
#     result = 10/value
#     print(result)
# except ValueError:
#     print("Invalid input- not a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero try with > 0")

# # (Grouped Exceptions)

# try:
#     value = int(input("enter a number"))
#     result = 10/value
#     print(result)
# except (ValueError,ZeroDivisionError):
#     print("invalid operation..")

# #Catchig any exception

# try:
#     #this line throws error
#     result = 10/0
# except Exception as e:
#     print(f"An an error occured:{e}")


# # Else Clause 
# #  else block runs only if no exceptions occur in try block
# try:
#     value = int(input("Enter a number:"))
# except ValueError:
#     print("Invalid input")
# else:
#     print(f"You entered {value} correctly")

# print("code execution completed..")


# #Finally clause
# # this will always executes regardless of whether an exception occured

# try:
#     a = 1
#     result = 10/a
# except ZeroDivisionError:
#     print("cannot divide with zero..")
# else:
#     print("no exception happened")
# finally:
#     print("Executed finally block..")


#Raising Exception 

def validate_age(age):
    if age<0:
        raise ValueError("Age cannot be negative..")
    if age>120:
        raise ValueError("Age is too high..")
    return age

# int("abc")
validate_age(-10)

## Using Custom Exceptions