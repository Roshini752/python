'''
s = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
count = 0
for i in s:
    print(count,i)
    count = count + 1

s = "a"
print(dir(s))
'''
'''
#characteristics of string
print("\ncharacteristics of string\n")
a = 'strings are immutable'
print (a)
#a = 'strings 'are' immutable'  #invalid syntax,perhaps you forgot a comma
#print (a)
a = "strings 'are' immutable"
print (a)
a = 'strings "are" immutable'
print (a)

#escape sequence
print("\nescape sequence\n")
msg = '\'strings are immutable\''  # \' will give the single quotes to the required string
print(msg)

msg = '\"strings are immutable\"'  # \" will give the double quotes to the required string
print(msg)

msg = 'strings\nare\nimmutable'
print (msg)
msg = 'strings\tare\timmutable'
print (msg)

msg = 'strings\\immutable'
print(msg)

#format specifiers
print("\nformat specifiers\n")

a= 12.000
print(a)
print("int of a is : %d"%a)
print("float of a is :%f"%a)
print("float value : %0.2f"%a)
a='cats'
b='dogs'
print("I love %s and %s" %(a,b))
c = 3
d =4
print("there are %d %s and %d %s"%(c,a,d,b))

#indexing

print("\nindexing\n")
s = "python"
print(s)
c=0
for i in s:
    print("str[%d] : %c "%(c,i))
    c = c+1
print("s[0] = ",s[0])
print("s[1] = ",s[1])
print("s[2] = ",s[2])
print("s[3] = ",s[3])
print("s[4] = ",s[4])
print("s[5] = ",s[5])
print("s[-1] = ",s[-1])
print("s[-2] = ",s[-2])
print("s[-3] = ",s[-3])
print("s[-4] = ",s[-4])
print("s[-5] = ",s[-5])
print("s[-6] = ",s[-6])



#slicing

print("\nslicing\n")

s = "string"
print(s)
print(s[1:4])
print(s[1])
print(s[4:])
print(s[-5:-2])
print(s[:4])
print(s[5:2:-1])
print(s[2:5:2])

#built in functions

print("\nbuilt in functions\n")

s=s.capitalize()
print("capitalize() : ",s)

a=s.center(7,'*') #if we give width < string len it will return only string 
print("center() : ",a)

a = 'sstring'
b = 'ẞtring'
if a.casefold()== b.casefold():
    print("the strings are equal")
else:
   print("the strings are not equal")

c=b.casefold()
print("casefold() : ",c)

s = "infosys is in India"
ss = "i"
count = s.count(ss,0,9)
print("count is",count)

res = s.endswith("India")
print("endswith() : ",res)

a = "hello ẞworld"
print("expandtabs() : ",a.expandtabs(8))  #vinay is  a goob  boy
#vinay is a  goob  boy   vinay   is  a   goob    boy
a = 'ẞ'
res=a.encode()
print(res)
#res="\xe1\xba\x9e"
print(res.decode())
print(res)

print(s.find("i s")) #8
print(s.find(" i ",))#-1

a="hi {b},welcom to {}".format("all",b="python")
print(a)

print(s.index("is")) # returns position if sub str is found else it will through error

str = "roshini"
print(str.isalnum()) #it will true for numbers and alphabets false for special characters

print(str.isalpha()) #it returns true if all the characters in string are alphabets
str = "1230"
print(str.isdecimal()) #it return true if all the numbers are decimals
#str = "1"
print(str.isdigit())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print("Is digit()",a.isdigit())


print("Is digit()",b.isdigit())



print("Is decimal()",a.isdecimal())


print("Is decimal",b.isdecimal())
'''
str="_P7YTHON" 
print(str.isidentifier()) #it will consider string as a identifier and it will chceck whether it valid or not

print(str.islower())
print(str.isupper())
str ="5"
print(str.isnumeric())
str1 ="\n is \n printable"
print(str1.isprintable())
str2 = "New 2Line"
print(str2.isprintable()) 
str3 = "\t \n "
print(str3.isprintable())
print(str3.isspace())
print(str2.istitle())# Title Cased-True
print(str2.isupper())
print(str2.lower())
print(str2.upper())
print(str2.swapcase())
print("join() : ",str.join(str2))

print("ljust() : ",str2.ljust(15,"*"))
print("rjust() : ",str2.rjust(15,"*"))
a = "   lstrip"
print(a)
#print("lstrip() :",a.lstrip())
print(a.lstrip('p'))
txt = ",,,,,ssaaww...w..bananaw....wwww"

x = txt.lstrip(",.asw")

print(x)

y = txt.rstrip(",.asw")

print(y)

x = txt.strip(",.asw")

print(x)







