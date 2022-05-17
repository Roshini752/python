''' Import error '''
#import OS  #original module os
''' syntax error'''

#print ' hello world '   #missing paranthesis

#print("hello')  #unterminated string literal

# print("hello")  #inexpected indent

#a = "python  #unterminated string literal

 #class = 'python'   #never use keywords (invalid syntax)

'''logical error like mistakes with precedence'''
a = 7
b = 8
print(a+b/2) #11.0

print((a+b)/2)  #7.5
  
'''NameError'''
xyz =9
print(xyz)         #print(xy)   #NameError: name 'xy' is not defined. Did you mean: 'xyz'?


'''keyerror'''

d = {1:10,"r":'roshini',10:"rosh","r":27}
print(d[1])   #10

#print(d[2]) #KeyError: 2 here 2 is not present in the dictionary

'''indexError'''
d= [1,2,3,4]
print(d[2])  #3
#print(d[7])   #IndexError: list index out of range

'''zerodivision error'''
"""x = 2/0
print(x) #ZeroDivisionError: division by zero
x = 1/False   #ZeroDivisionError: division by zero """

'''ValueError'''
print(ord("a"))  #97
#print(ord(1))  #TypeError: ord() expected string of length 1, but# int found
#print(ord("abc"))  #TypeError: ord() expected a character, but string of length 3 found

x = int(2.0)
print(x)
#x = int('r')  #ValueError: invalid literal for int() with base 10: 'r'













