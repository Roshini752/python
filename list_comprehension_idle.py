Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
Traceback (most recent call last):
  File "C:/Python310/python_program/list_comprehension.py", line 6, in <module>
    newlist.append(x)
NameError: name 'newlist' is not defined. Did you mean: 'new_list'?

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 'mango']

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 0]

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 0]
Traceback (most recent call last):
  File "C:/Python310/python_program/list_comprehension.py", line 34, in <module>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 34, in <listcomp>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 33, in list_fruits
    return fruit if fruit != apple else 0
NameError: name 'apple' is not defined. Did you mean: 'tuple'?

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 0]
Traceback (most recent call last):
  File "C:/Python310/python_program/list_comprehension.py", line 37, in <module>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 37, in <listcomp>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 33, in list_fruits
    if fruit != apple :
NameError: name 'apple' is not defined. Did you mean: 'tuple'?

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 0]
Traceback (most recent call last):
  File "C:/Python310/python_program/list_comprehension.py", line 37, in <module>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 37, in <listcomp>
    newlist =[list_fruits(x) for x in fruits]
  File "C:/Python310/python_program/list_comprehension.py", line 33, in list_fruits
    if(fruit != apple) :
NameError: name 'apple' is not defined. Did you mean: 'tuple'?

========== RESTART: C:/Python310/python_program/list_comprehension.py ==========
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['banana', 'cherry', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'kiwi', 'mango']
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'banana', 'cherry', 'kiwi', 0]
[0, 'banana', 'cherry', 'kiwi', 'mango']
