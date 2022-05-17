Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = {}
type(a)
<class 'dict'>
a = {0}
type(a)
<class 'set'>
a = set()
type(a)
<class 'set'>
bool(a)
False
a = set(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a = set(0)
TypeError: 'int' object is not iterable
bool(a)
False
a = {0}
bool(a)
True
a = {}
bool(a)
False
x ={1,2.4,"hello",None}
type(x)
<class 'set'>
x = {1,2,(3,4,5),"rosh"}
x = {1,2,[3,4,5],"rosh"}
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = {1,2,[3,4,5],"rosh"}
TypeError: unhashable type: 'list'
"rosh" in x
True
"ro" in x
False
x | y
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x | y
NameError: name 'y' is not defined
y = {1}
x|y
{1, 2, (3, 4, 5), 'rosh'}
y = {89}
x|y
{1, 2, (3, 4, 5), 'rosh', 89}
x & y
set()
y ={1,3,4}
x & y
{1}
x - y
{2, (3, 4, 5), 'rosh'}
x ^ y
{2, 3, 4, 'rosh', (3, 4, 5)}
x<=y
False
x >=y
False
x |= y
print(x)
{1, 2, (3, 4, 5), 3, 4, 'rosh'}
x &= y
print(x)
{1, 3, 4}
x-=y
print(x)
set()
x ^= y
print(x)
{1, 3, 4}
