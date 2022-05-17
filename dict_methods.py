d = {1:"hini",2:"ros"}
print(d)
d.clear()   # it will clear the elements in dictionary
print(d)

d = {1:"hini",2:"ros"}

dt = d.copy()
print("d is " ,d)
print('dt is ',dt)
dt[3]= 4
#d[3] = 4
print("d is " ,d)
print('dt is ',dt)

x = dict.fromkeys(d)  # it copies the keys to new dict by defalut values are None
print("x is ",x)
print("d is ",d)


x = dict.fromkeys(d,6) # here values for keys are 6
print("x is ",x)
print("d is ",d)

x = d.get(2)   # it returns the value for key 
print(x)

x = d.get(3) #if key doesnt exist returns none
print("get is",x)

x=d.items()  #it will return the key-value pairs in (key,value) format
print("dict items are",x)

x = d.keys() #it will return all the keys
print('keys are :',x)

 
x = d.pop(2)   # it will delete the key and return corresponding value
print("pop is ",x)
d[3]=4
d[5]="r"
d[0] ="o"
print(d)
print("popitem is ",d.popitem()) # it will delete the last key-value pair


x = d.setdefault(9,8) # it will the corresponding value 
print(x) #8
print(d) #if key-value didnt present in the dict then it add that key-value pair

x = {5:4,'r':'o',2:'p'}
d.update(x)  # x ele are also  added  to d 
print("updated d is " ,d)

print("values are " ,d.values())





