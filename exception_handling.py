import os
'''
try:
    x = int(input("enter a value: "))
    print("Try block : number is ",x/0)
except:
    print("Except block : Invalid input,enter numbers only")
'''
'''
try:
    x = int(input("enter a value: "))
    y = int(input("enter a value: "))
    print("Try block : number is ",x/y)
except Exception as arg:
    #print("divide by zero exception is raised")
    print(arg)
except ValueError:
    print("Except block : Invalid input,enter numbers only")
'''

'''
try:
    x = int(input("enter a value: "))
    print("Try block : number is ",x)
except:
    print("Except block : Invalid input,enter numbers only")
else:
    print('no exception')
'''
'''
try:
    '''x = str(input("enter a value: "))
    print("Try block : number is ",x)'''
    x = 10
    y = 0
    z = x/y
except Exception as arg:
    print(arg)
    
finally:
    print(" entered value is : ")
'''
'''except:
    print("Except block : Invalid input,enter numbers only")'''


try:
    x = int(input("enter a value: "))
    y = int(input("enter the y value : "))
    try:
        print("second try block is : ","div is", x/y)
    except Exception as arg :
        print(arg)
except:
    print("entered values are not integers")
finally:
    print("entered values are :",x,y)
    
'''
try:
    y=10
    x = int(input("enter a value: "))
    assert x<10,'age limit should be less than 10'
    print("x is eligible")
    try:
        print("second try block is : ","div is", x/0)
    except Exception as arg :
        print("Exception Error : ",arg)
except Exception as arg:
    print("error : ",arg)
finally:
    print("entered values are :",y)
'''    
'''    
except AssertionError:
    print("x is not Eligible")
'''
'''
except:
    print("invalid input")
'''
'''finally:
    print("...")'''
'''
try:
    x = int(input("enter x value :" ))
    print(x/0)
except Exception as arg:
    print("Exception values are : ",arg)
'''
    
    
    






    






    
