s ={'roshini',27,8.27,23.5}
a = frozenset(s)   # which is immutable 
print(type(s))
print(type(a))
y = {5}
#fs.update(y) #no update is there as frozen set is immutable
print(a)

b = a.copy()
print(b)

c = b.difference(a) # b-a
print(c)

d = a.intersection(b) # it will return the common ele
print(d)

d =a.isdisjoint(b)
print(a)
print(d)  # it will return whether two sets have intersection or not
print(b)

d = a.issubset(b)
print(d)
a = {4,5}
d = a.issubset(b)
print(d)
d = a.issuperset(b)
print(d)

d = a.symmetric_difference(b) #it will return the elements which are not same
print(a)
print(d)
print(b)

d = a.union(b) #it will return the similar values 
print(d)

a =frozenset({1,2,3,4})
b =frozenset({0,1,2,3})
c =frozenset({0,0,0,0})
print(type(a),type(b),type(c))
print("all-a:",all(a))
print("all-b:",all(b))
print("all-c:",all(c))
print("any-a:",any(a))
print("any-b:",any(b))
print("any-c:",any(c))
x=enumerate(a)
print(x)
for i in x:
    print(i)
print('len ',len(a))
print('list ',list(a))
print("max ",max(a))
print("min ",min(a))
print("sum ",sum(a))










