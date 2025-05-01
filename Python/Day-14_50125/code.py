my_list = [1,2,3]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #Raises StopIteration exception


# auto-handled in loop cause it checks each iteration whether 
# next element is present if not it stops
my_list = [1,2,3]
iterator = iter(my_list)
# for x in my_list:
for x in range(len(my_list)):
    value = next(iterator)
    #data manipulation


##generators
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print("\n\n\n")
print(next(gen))
print(next(gen))
print(next(gen))

def my_generator2():
    for i in range(100):
        yield i

gen2 = my_generator2()

for i in range(100):
    print(next(gen2))

def with_generator():
    result = []
    for i in range(100):
        result.append(i)
    return result 

data = with_generator()
for i in data:
    print(i)

numbers = [1,2,3,4,5]

def double(nums):
    # for i in nums:
    for i in range(len(nums)):
        yield nums[i] *2 

doubled = double(numbers)

for result in doubled:
    print(result)


#real world use case for Data Engineering
#helps us to process a file with million of lines