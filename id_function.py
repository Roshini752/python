Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
id(1)
2131433292016
a = 10
id(a)
2131433292304
a = a+2
id(a)
2131433292368
id('python')
2131469601840
str1 = 'roshini'
str2 = 'peyyala'
id(str1)
2131470170480
str1 = str1 + str2
id(str1)
2131469708784
a = (1,2,3)
id(a)
2131470271168
a[3] = 4
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[3] = 4
TypeError: 'tuple' object does not support item assignment
a[1] = a[1] + 2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[1] = a[1] + 2
TypeError: 'tuple' object does not support item assignment
a.append = 4
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append = 4
AttributeError: 'tuple' object has no attribute 'append'
a = [1,2,3]
id(a)
2131470171904
a[1] = 3
print(a)
[1, 3, 3]
id(a)
2131470171904
# here list is a mutable -> here we changed the a value but didnt changes its id
# but in strings whenever we changed the string id also changed -> immutable
