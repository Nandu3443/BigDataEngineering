#dictionaries

# my_dict = {
#     "name":"John",
#     "age": 30,
#     "city" : "New York"
# }

# empty_dict = {} # dict()

# data = [("name","John"),("age",30),("city","Newyork")]

# dict_with_tuples = dict(data)

# print(dict_with_tuples)

# dict_with_constructor = dict(name="John",age=30)
# print(dict_with_constructor)

# #Key Operations

# #access elements

# name = my_dict["name"]     # raised KeyError if not found
# age = my_dict.get("age",0) # returns default if not found
# print(name,age)

# #Adding / Modifying elements

# my_dict["email"] = "john@email.com"
# print(my_dict)
# my_dict["age"] = 31
# print(my_dict)

# updated_dict = {
#     "name":"John Klan",
#     "age": 29,
#     "city" : "Dallas",
#     "phno":"1312312312"
# }

# my_dict.update(updated_dict)
# print(my_dict)

# #Remove elements

# del my_dict["city"] #Removes key-value pair (KeyError if not found)
# print(my_dict)

# popped_value = my_dict.pop("age")  #removes and returns value
# print(popped_value)

# print(my_dict.popitem())
# print(my_dict.popitem())
# print(my_dict.popitem()) # keyError if no items present
# print(my_dict)


# my_dict = {
#     "name":"John",
#     "age": 30,
#     "city" : "New York"
# }


# #Dictionary methods

# keys = my_dict.keys() #returns dict_keys type
# print(type(keys))

# values = my_dict.values() #returns dict_values
# print(values)

# items = my_dict.items()  #dict_items 
# print(items)


# #Membership testing

# has_key = "last_name" in my_dict
# print(has_key)
# if has_key:
#     del my_dict["last_name"]

# #collection of dictionaries

# stutent_1 = {
#     "name":"John",
#     "age": 19,
#     "city" : "New York"
# }

# stutent_2 = {
#     "name":"Bob",
#     "age": 19,
#     "city" : "New York"
# }

# list_of_students = []
# list_of_students.append(stutent_1)
# list_of_students.append(stutent_2)
# print(list_of_students)



# list_of_students = [
#     {
#     "name":"John",
#     "age": 19,
#     "city" : "New York"
#     },
#     {
#     "name":"Bob",
#     "age": 19,
#     "city" : "New York"
#     }
# ]

# print("\n\n\n")
# for item in list_of_students:
#     if item["name"] == "John":
#         item["age"] = 20

# print(list_of_students)

# print("\n\n\n")


# # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
# for  key,value in stutent_1.items():
#     print(key,value)

# # Not allowed to manipulate data while looping
# stutent_1_copy = stutent_1.copy()
# for ele in stutent_1_copy:
#     if stutent_1_copy[ele] == "John":
#         stutent_1["email"] = "john@email.com"

# print(stutent_1)

##List Comprehensions

# data = [1,2,3,4,5]

# #simple list comprehension
# incremented_list = [x*2 for x in data]
# print(incremented_list)

# squares = [ x**2 for x in range(10)]
# print(squares)

# #with conditional

# even_squares = [x**2 for x in range(10) if x%2==0]
# print(even_squares)

# # with if-else

# parity = ["even" if x%2==0 else "odd" for x in data]
# print(parity)

# nested_data = [["john","klan"],[22,33],["new york","new york"]]

# flattened = [ item for sublist in nested_data for item in sublist  ]
# print(flattened)

# for sublist in nested_data:
#     for item in sublist:
#         print(item)

# #set comprehensions

# unique_sqaures = { x**2 for x in range(-5,5)}
# print(unique_sqaures)

# #dictionary comprehensions

# sqaure_dict = { x:x**2 for x in range(5)}
# print(sqaure_dict)

# # with conditional

# even_sqaure_dict = { x:x**2 for x in range(5) if x%2==0}
# print(even_sqaure_dict)

# #creating dictionary from  two lists

# names = ["Alice","bob","Charlies"]
# ages = [25,30,35]


# person_data  = {name:age for name,age in zip(names,ages) }
# print(person_data)

# person_data = {}
# for i in range(len(names)):
#     person_data[names[i]] = ages[i]

# print(person_data)

## Functional Programming

def add(a,b):
    return a+b

print(add(1,2))

#lambda function to add two numbers

add = lambda a,b: a+b
print(add(1,2))

#lambda function for squaring a number

square = lambda x: x**2
print(square(2))

# Map function

numbers = [1,2,3,4]
def double(x):
    return x*2

doubled = map(double,numbers)
print(list(doubled))

squared = map(lambda x:x**2,numbers)
print(list(squared))

## Filter function


def is_odd(x):
    return x%2!=0

odd_numers = filter(is_odd,numbers)
print(list(odd_numers))

even_numbers = filter(lambda x:x%2==0,numbers)
print(list(even_numbers))

list_of_students = [
    {
    "name":"John",
    "age": 19,
    "city" : "New York"
    },
    {
    "name":"Bob",
    "age": 16,
    "city" : "New York"
    }
]


filter_students = list(filter(lambda data:data.get("age",0)>18,list_of_students))
print(filter_students)