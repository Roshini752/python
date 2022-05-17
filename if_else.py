
#simple if

n = 10
if n % 2 == 0:
   print("n is an even number")

#if_else
n = 5
if n % 2 == 0:
   print("n is even")
else:
   print("n is odd")

#nested_if

a = 5
b = 10
c = 15
if a > b:
   if a > c:
      print("a value is big")
   else:
       print("c value is big")
elif b > c:
    print("b value is big")
else:
     print("c is big")

#if_elif_else

x = 15
y = 12
if x == y:
   print("Both are Equal")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")
