name = "John"
age = 25
pi = 3.14159
is_alive = True
paragrah = '''
                This is a sample paragraph to understand...
        '''

print(name)
print(age)
print(pi)
print(is_alive)
print(paragrah)


# String to number
print("String to Number")
age_str = "25"
print(type(age_str))
age_int = int(age_str)
print(type(age_int))


#Number to string
print("Number to string")
count = 42
print(type(count))
count = str(count)
print(type(count))

# Integer to float & vice versa

x = 10
x = float(x)
print(x)

y = 10.9 
y = int(y)
print(y)  # it truncates the decimal points, it doesn't round values


# Boolean

empty_to_false = ""
empty_to_false = bool(empty_to_false)
print(empty_to_false)

zero_to_false = bool(0)
print(zero_to_false)

strig_to_bool = bool("false")
print(strig_to_bool)