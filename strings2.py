
a = "python is fun"
print(a.partition('is'))
print(a.partition('not'))

a = "python is fun and it is easy"
print(a.partition('is'))

a = "python is fun"
print("\n",a.rpartition('is'))
print(a.rpartition('not'))

a = "sing- sing sing- sing"
print(a.rpartition('is'))

print(a.replace("sing","song",1))

print("find():",a.find('i'))

print("rfind() :",a.rfind('i',3,9)) #it will check from the right side

print("rindex() : ",a.rindex('sin',3,9))

print("split() : ",a.split(" ",2))

print("rsplit() : ",a.rsplit("-",1))

study = "pen\nbook\npencil\n"
print("splitlines() : ",study.splitlines())
study = "pen book pencil"
print("splitlines() : ",study.splitlines())

print("startswith() : ",a.startswith('sing'))

print("startswith() : ",study.startswith('book'))

print("title() : ",a.title())
fill = "new story"
print("zfill() : ",fill.zfill(10))
c = "ẞ"
b = "b"
print("isascii() : ",c.isascii())
print("isascii() : ",b.isascii())
print("removesuffix() : ",a.removesuffix("si"))
print("a.removeprefix() : ",a.removeprefix("ing"))

txt = "hi this is"
x = "is"
y = "am"
mytable=txt.maketrans(x,y)
print("maketrans() : ",mytable)
print("translate() : ",txt.translate(mytable))
val = "all"
b="python"
a="hi {0},welcom to {1}".format(val,b)
print(a)
a={'x':4,'y':5}
print('{y} {x}'.format_map(a))
