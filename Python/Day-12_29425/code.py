# Lists

# my_lists = [1,2,3,4,5]
# empty_list = []
# mixed_list = [1,"hello",3.14,True]
# nested_list = [1,[2,3],4]
# student_name = ["alex","bob","charlie"]

# #Opeartions
# # 1.Accessing Elements
# first_item = my_lists[0]
# last_item = my_lists[-1]
# print(last_item)

# #slicing 

# sub_list = my_lists[1:4]

# #Adding elements

# my_lists.append(6)
# my_lists.insert(0,0)
# my_lists.insert(3,-3)
# print(my_lists)

# my_lists[4] = 100
# print(my_lists)


# #Removing elements
# my_lists.remove(100)
# # my_lists.remove(9) #throws exception
# print(my_lists)
# my_lists.pop()
# my_lists.pop()
# print(my_lists)
# removed_value = my_lists.pop(3)
# print(my_lists)
# print(removed_value)

# #finding elements 

# index = my_lists.index(4)
# print(index)
# my_lists.append(2)
# print(my_lists)
# print(my_lists.count(4))

# # List Operations
# length = len(my_lists)
# my_lists.append(3)
# print(my_lists)
# my_lists.sort()
# print(my_lists)
# my_lists.reverse()
# print(my_lists)

# other_list = [7,8,9]
# my_lists.extend(other_list)
# # my_lists = my_lists + other_list
# print(my_lists)


# ##tuple 

# my_tuple = (1,2,3,3,4,5)
# print(my_tuple)
# empty_tuple = ()
# single_item_tuple =  (1,) #tuple([1])
# print(single_item_tuple)
# a = [1,2,3,4,5]

# tuple_from_list = tuple(a) # tuple([1,2,3,4,5])
# print(tuple_from_list)

# #key operations

# #Access elements (zero-indexed)

# first_item = my_tuple[0]
# last_item = my_tuple[-1]

# #Slicing
# sub_tuple = my_tuple[1:4]

# #find elements
# print(my_tuple)
# index = my_tuple.index(3) #returns index of first-occurence value
# print(index)
# count = my_tuple.count(3)

# #operations
# length = len(my_tuple)
# combined = my_tuple + (6,7,8) # tuple concatenation
# print(combined)

# #modify and recreate
# tuple_list = list(my_tuple)
# print(tuple_list)
# tuple_list[3] = 100
# my_tuple = tuple(tuple_list)
# print(my_tuple)

##Sets

my_set = {1,2,3,4,5}
empty_set = {}
set_from_list = set([1,2,3,4,5])

#Key operations

#adding element
my_set.add(5)
my_set.add(6)
print(my_set)

my_set.update([7,8,9])
print(my_set)

#Acccesing Directly not possible, sol : using loop
# my_set[0]

#removing elements

my_set.remove(3) #keyError if not found
my_set.discard(10)
my_set.pop() #removes and returns the element
print(my_set)
my_set.clear()
print(my_set)

#Set operations

a = {1,2,3,4}
b = {3,4,5,6}

union  = a.union(b) # a | b
print(union)
intersection = a.intersection(b) # a & b
print(intersection)

difference  = a.difference(b) # a-b
difference = b - a
print(difference)

symmetric_diff = a.symmetric_difference(b) # a^b
print(symmetric_diff)

# Member testing

my_set = {1,2,3,4,5}
is_in = 6 in my_set
print(is_in)
