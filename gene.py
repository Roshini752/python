

"""
y = [1,2,3,4,5,6,7,8,9]

a = (x*2 for x in y)
# generator expression
print(a) # it will print the genarator object

print(list(a)) # it print the newly generated list
"""
'''-------------------------------------------------'''
"""
def gen():
    print("1st yield")
    yield 1
    print("2nd yield")
    yield 2
    print("3rd yield")
    yield 3
print("---------------")
for i in gen():
    print(i)
x = gen()

print("------------------")
print(next(x))
print(next(x))
print(next(x))
"""
'''--------------------------------------------'''
"""
def gener(n):
    for i in range(n):
        yield i


for i in gener(5):
    print(i)

'''--------------------------------------------'''
"""
"""
def genera(n):
    for i in range(n):
        yield i


x = genera(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
"""
"""
print("--------------------------")
#---------------------------------------------------------------------#

#ITERATOR#

nums = [1,2,3,4]

it = iter(nums)

print(it.__next__())
print(it.__next__())
"""
#-----------------------------------------------------------------------#

#DECORATOR#

"""
def div(a,b):
    print(a/b)

div(2,4)  # 0.5

div(4,2)  # 2.0
"""

"""
def div(a,b):
    print(a/b)
def dec_div(func):
    def inn(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inn
div1 = dec_div(div)
div1(2,4)
"""
#-----------------------------------------------------------------------#

from array import *

a= array('i',[1,3,5,7,9])
#array_num.typecode

print(a)
print(a[0])
print(a[3])
a[3] = 8
print(a[3])
a[2:5]=array('i',[6,8,10])
print(list(a))



"""
numbers = [1,3,9]
value = numbers.__iter__()
item1 = value.__next__()
print(item1)
item2 = value.__next__()
print(item2)
item3 = value.__next__()
print(item3)
"""
"""
num_list = [1,4,9]
iter_obj = iter(num_list)
while(True):
    try:
        ele = next(iter_obj)
        print(ele)
    except StopIteration:
        break
        """
"""
def even_generator(maxm):
    n=2
    while n<= maxm:
        yield n
        n += 2
numbers = even_generator(4)
print(next(numbers))
print(next(numbers))
print(next(numbers))"""

'''
def printer():
    print("Hello world")
def display_info(func):
    def inner():
        print('executing',func.__name__,'function')
        func()
        print('finished execution')
    return inner
Decorated_func = display_info(printer)
Decorated_func()
'''
"""
def dec_div(func):
    def inn(a , b):
        if a<b:
            a,b=b,a
        return func(a , b)
    return inn
@dec_div
def div(a , b):
    print(a/b)
div(4,2)
#div1 = dec_div(div)
#div1(2,4)
"""
"""
def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner
def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner
@star
@percent
def printer(msg):
    print(msg.center(30))

printer("decorators are wonderful")

import array as arr
number = arr.array('i',[1,2,3,4,5])
del number[2]
		# removing 3rd ele
print(number)
del number
		# deleting entire array
print(number)



import pickle

# Python object
my_list = [11, 'Python', b'Love Python']

# Pickling
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

print("Pickling completed!")

"""
"""
import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
   """
import pickle
EmpID = {1:"Zack",2:"53050",3:"IT",4:"38"}
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()

import pickle
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)

import pickle
pickle_off = open("EmpID.pickle", 'rb')
EmpID = pickle.load(pickle_off)
print(EmpID)

#{1: 'Zack', 2: '53050', 3: 'IT', 4: '38'}











































