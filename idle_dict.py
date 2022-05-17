'''Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.'''
s ={}

type(s)
<class 'dict'>
# s ={} empty dictioanry
# for list we work with individual elements
# for dict we work with key : value pairs
d = {100:20}
print(d)
{100: 20}
d = {10:'roshini','rosh':27}
print(d)
{10: 'roshini', 'rosh': 27}
d = {}
d[100]='roshini'
d[2] ="peyyala"
print(d)
{100: 'roshini', 2: 'peyyala'}
d[100] = 'rosh'
print(d)
{100: 'rosh', 2: 'peyyala'}
d[3] = 'rosh'
print(d)
{100: 'rosh', 2: 'peyyala', 3: 'rosh'}
 # same keys are negleted
 
# the same key will be updated with new value
# the same values with different keys are allowed
#nested dictionary
d = {1:2,"r":'roshini',"ro":27,27:{1:2,4:'april,12:'dec}}
SyntaxError: expression expected after dictionary key and ':'
d = {1:2,"r":'roshini',"ro":27,3:{1:2,4:'april,12:'dec}}
SyntaxError: expression expected after dictionary key and ':'
d = {1:2,"r":'roshini',"ro":27,27:{1:2,4:'april,12:'dec'}}
                                   
SyntaxError: unterminated string literal (detected at line 1)
d = {1:2,"r":'roshini',"ro":27,27:{1:2,4:'april',12:'dec'}}
                                   
print(d)
                                   
{1: 2, 'r': 'roshini', 'ro': 27, 27: {1: 2, 4: 'april', 12: 'dec'}}
print(d[2])
                                   
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(d[2])
KeyError: 2
print(d{2})
                                   
SyntaxError: invalid syntax
d = {(1,2,3):'tuple'}
                                   
print(d)
                                   
{(1, 2, 3): 'tuple'}
d = {[1,2,3]:'list'}
                                   
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d = {[1,2,3]:'list'}
TypeError: unhashable type: 'list'
# dictionaries doesnt have mutable ele
                                   
d = {(1,2,3):'tuple'}
                                   
d[2]="feb"
                                   
print(d)
                                   
{(1, 2, 3): 'tuple', 2: 'feb'}
d[2] = "febr"
                                   
print(d)
                                   
{(1, 2, 3): 'tuple', 2: 'febr'}
