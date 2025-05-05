import math
result = math.sqrt(16)
print(result)

from random import randint,choice
number = randint(1,10)
print(number)
print(randint(1,10))
print(randint(1,10))
item = choice(['apple','orange','banana'])
print(choice(['apple','orange','banana']))
print(choice(['apple','orange','banana']))
print(choice(['apple','orange','banana']))

import my_utils
print(my_utils.greet("Alice"))
print(my_utils.PI)
print(my_utils.sqaure(4))


#import specific items
from my_utils import greet,PI
from my_utils import *
print(greet("bob"))
print(PI)
print(sqaure(5))

import sys

# print(sys.path)

sys.path.append('C:\\Users\\HCR867\\Desktop')
from utils2 import welcome,PI
print(welcome("Thank you"))
print(PI)

from common.utils import *
print(double(2))
print(PI_alter)

import pandas as pd