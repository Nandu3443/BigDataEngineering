# name = "Sai Nandyala"
# user_input = input("Enter your name:")
# print(user_input)
# age = int(input("Enter your age:"))
# print(type(age))

# print("Hello welcome")

# # Multiple items
# print("hello",user_input, "you are",age,"years old")

# # formatting with f-strings  (3.6+) .format()

# print(f"Hello {user_input}, you are {age} years old..")


# #customize seperators and ending
# print("apple","banana","cherry")
# print("apple","banana","cherry",sep=", ")
# print("apple","banana","cherry",end=" ")
# print("mango")


# text = "Python"
# # forward indexing
# first = text[0]
# print(first)
# # backword indexing
# print(text[-1])

# text2 = ""
# print(len(text))
# # print(text[0]) throws index out of range error

# text = "Python programming"
# slice1 =text[0:6]

# print(slice1)

# slice2 = text[7:]
# slice2 = text[7:14]
# print(slice2)

# #stepper -> using each 2nd character
# slice3 = text[0::2]
# print(slice3)

# reversed = text[::-1]
# print(reversed)

# #common string methods
# text = " Hello, World!,Hello   "
# length = len(text)
# print(length)

# upper = text.upper()
# lower = text.lower()

# print(upper,lower,sep="\n")

# stripped = text.strip()
# print(len(stripped))

# replaced = text.replace("Hello","Hi")
# print(replaced)

# found = text.find("World") #9
# found = text.find("xyz") #-1 i.e not present
# print(found)

# splitted_text = text.split(",")
# print(splitted_text)


# #String concatenation
# greeting = "Hello" + " " + "there !" #"Hello there!"

# name = "sai"
# age="25"
# gender="male"
# print("Hello" + " " + "there !")
# print(name+" "+age+" "+gender)


# repeated = "sai"*30  # saisaisai
# print(repeated)



#Conditional Satements

age = 16

if age >= 18:
    print("You are allowed to apply license..")
else:
    print("You are not allowed...")


grade = 95


if grade >= 90:
    print("A - Excellent")
    print("Good Perfomance")
elif grade >= 80:
    print("B - Good")
elif grade >= 70:
    print("C - Satisfactory")
elif grade >= 45:
    print("D - Need Improvement")
else:
    print("F - Failed")

if grade>90:
    print("@A - Excellent")