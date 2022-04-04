

"""
y = [1,2,3,4,5,6,7,8,9]

a = (x*2 for x in y)
# generator expression
print(a) # it will print the genarator object

print(list(a)) # it print the newly generated list

'''-------------------------------------------------'''
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

'''--------------------------------------------'''

def gener(n):
    for i in range(n):
        yield i
print("--------------------------")

for i in gener(5):
    print(i)

'''--------------------------------------------'''
def genera(n):
    for i in range(n):
        yield i

print("--------------------------")
x = genera(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


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


def div(a,b):
    print(a/b)

div(2,4)  # 0.5

div(4,2)  # 2.0



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

#-----------------------------------------------------------------------#

from array import *

array_num = array('i',[1,3,5,7,9])
array_num.typecode

print(array_num)
print(i)
















































