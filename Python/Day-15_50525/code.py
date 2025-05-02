## Reading text files
# file = open('file.txt','r')
# print(file.readlines())
# file.close()

# #iteration over file object
# with open('file.txt','r+') as file:
#     #helps to read line by line from file
#     for line in file:
#         print(line)
    
#     #to read data as list of strings
#     data = file.readlines()
#     print(data)

#     data = ["Hi, hello\n","how are you?\n"]

#     #to write line by line
#     file.write("hi hello")

#     #to write list of lines at one short
#     file.writelines(data)

# #create a file if not exists
# with open('new_file.txt','w') as file:
#     data = ["Hi, hello\n","how are you?\n"]
#     file.writelines(data)


# # Working with csv files

# # import csv 

# # with open('student_data.csv','r') as file:
# #     csv_reader = csv.reader(file)
# #     for row in csv_reader:
# #         print(row)

# # with open('student_data2.csv','w') as file:
# #     csv_writer = csv.writer(file)
# #     csv_writer.writerow(['Name','Age','City'])
# #     csv_writer.writerow(['John','25','New York'])

# #Working with Json

# #writing json

# import json
# data = {
#     'name':'John',
#     'age':30,
#     'city':'NewYork'
# }

# with open('output.json','w') as file:
#     json.dump(data,file,indent=4)

# with open('output.json','r') as file:
#     print(type(file.read()))
#     data = json.load(file)
#     print(data.get("name"))

## Working with paths using os lib
# import os
# current_dir = os.getcwd()
# print(current_dir)

# file = open('C:\\Users\\HCR867\\Documents\\MyGIT\\BigDataEngineering\\Python\\Day-15_50525\\file.txt')
# print(file.read())
# file.close()

# file_path = os.path.join(current_dir,'file.txt')
# print(file_path)

# print(os.path.exists(file_path))

# if os.path.exists(file_path):
#     print("file exists!..")

# # os.rename('file.txt','updated_file.txt')
# # os.remove('new_file.txt')

# # os.mkdir('files')
# os.makedirs('files/txt_files',exist_ok=True)

## Working with paths using path lib lib

from pathlib import Path
import os

#creates path object
data_dir = Path(os.getcwd())
file_path = data_dir/'file.txt' #path joining with / operator
print(file_path)

content = file_path.read_text()
print(content)

file_path.write_text('New content')

#properties of file

print(file_path.name)   # just the file name
print(file_path.suffix) # file extension
print(file_path.parent) # parent directory

#path operations

print("\n\n\n")
for file in Path(os.getcwd()).glob("*.txt"):
    print(file)

with open('teLfile.txt','r',encoding='utf-8') as file:
    print(file.read())