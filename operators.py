#operators

#arithmatic operators

'''
x= 10 + 10.5
print(x)
#x=x + 'a'
#print(x)   # we cant add num and str



a= 5+3-2+4-1*2+2*3/2 
print(a)

print('a'+'b')
print('10'+'20')
print(5/2)
print(5//2)
print(25/6)
print(25%6)
print(-25%-7)


print(10**4, 10*4 , "a"*4)
'''

#Relational Operators

'''
print(5>3)
print(5<3)
print(5!=5.0)  #5.0 type cast to 5 (float to integer)
print(5==5.0)
print(3>=3.0)
print(3<=3.0)

print(None == False)
print(1.00 == 1.00000)
'''

#assignment operators

'''
x = 10
print(x)
x = 15
print(x)

x += 5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=5
print(x)
x%=5
print(x)

x//=5
print(x)

#x**=5
#print(x)

#x&=5
#print(x)

#x|=5
#print(x)

#x^=5
#print(x)

#x<<=5
#print(x)

#x>>=5
#print(x)
'''

#logical operators
'''
a=10  #0000 1010
b=4   #0000 0100
x=4
print(b and a)#if both are true it will return second operand else returns 0-'False'
print(b or a)#If any ne true then it will return true value

print(1 and 1)

c=b or a
print(c)

c= not x #if x is true value c will return false and vise versa
print(c)
'''

#bit-wise operators
'''
a=10 #0000 1010
b=4  #0000 0100

print(a & b)#0000 0000
print(a | b)#0000 1110
print(a ^ b)#0000 1110

print(~a)#-(n+1)
print(a>>2)#0000 0010
print(a<<2)#0010 1000
'''
#membership operators
# it will  return true or false

string = "Roshini"
print('K' in string)
print("sh" in string)

for i in range(5):
    print(i)

s="R"

if s in string:
    print(s,"is present in the string",string)
else:
    print("Not present")



s = "r"
if s not in string:
    print("Not present")
else:
    print(s,"is present in the string",string)

