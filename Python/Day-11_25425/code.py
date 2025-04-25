print("Hello..")

is_licensed = True
is_aged = True
age = 18

#Logical and operator
if is_licensed and age>=18:
    print("You can drive..")
else:
    print("You are not allowed to drive..")


#Logical or operator
is_licensed = True
is_aged = False

if is_licensed or is_aged:
    print("you can drive")
else:
    print("You'r not allowed")

#Logical not operator

is_licensed = False
is_aged = True

if not is_licensed:
    print("You are not allowed to drive..")
else:
    print("You are allowed..")

# 100 times 
#looping over a range of numbers
for i in range(5):
    print(f"Hello welcome, How are you - {i}")
    print("------")

#loop over a string

value = "Python Programming"
for char in value:
    print(char)


#While Loop 
counter = 1
while counter <= 5:
    print(f"Hello welcome, How are you - {counter}")
    counter +=1 
    # counter = counter + 1

print("done with while loop...")

counter = 1
condition = True
while condition:
    print(f"#Hello welcome, How are you - {counter}")
    counter +=1
    if counter == 6:
        condition = False


#break 
# 0,1,2,3,4----10
for i in range(10):
    if i == 5:
        break  #stops at 5, printing only 0-4
    print(i)

print()
print()
#continue 

for i in range(5):
    if i % 2 ==0  :
        print("skipping the iteration")
        continue
    else:
        print(i)

result = 0
# for i in range(5):
#     user_input = int(input("enter a value:"))
#     result = result + user_input
#     # line 2
#     # line 3
#     # .
#     # line 59
#     # .
#     # .
#     # line 100

# print(result)


# for i in range(3):
#     user_input = int(input("enter a value:"))
#     result = result + user_input
#     # line 2
#     # line 3
#     # .
#     # line 59
#     # .
#     # .
#     # line 100


# print(result)

# def greet(name):
#     greetings = f'''
#                     This is a greeting from {name}, wish you all the best.. 
#     '''
#     return greetings

# for i in range(1):
#     user_input = input("Enter the name to greet:")
#     print(greet(user_input))

# print(greet("sai"))

# def addition(previous_value):
#     user_input = int(input("enter a value:"))
#     # line 2
#     # line 3
#     # .
#     # line 59
#     # .
#     # .
#     # line 100
#     return previous_value + user_input

# result = 0
# for i in range(5):
#     result = addition(result)

# print(f"the result is {result}")
    
# print(addition(19892))

# def greet2():
#     return "Hi hello, how are you.."

# print(greet2())

# print(addition()) # throws error

def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("sai"))
print(greet("sai","hola"))
# print(greet())


# No return --> None (implicitly)
def log_message(msg):
    print(f"LOG : {msg}")
    # return None

print(log_message("hello ...."))


#return a value

def sqaure(x):
   return x*x

print(sqaure(2))

#return multiple values

def get_dimensions():
    x = 200
    y = 100
    return x,y

width,height = get_dimensions() # unpack the tuple
print(f"width is {width}")
print(f"height is {height}")


# functional scope 

x = 10 # global scope
y = 30
def my_function():
    global y
    y = 5    #local variable
    a = 10
    print(x,y)
    return None

my_function() # 10 5
print(x)
print(y)  # Error : y is not defined in this scope
# print(a)  # error 

if True:
    z = 20
else:
    print("Nothing...")

print(z)