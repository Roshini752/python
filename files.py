import os
import shutil
# Reading a file
'''file = open("file1.txt",'r')
print(file.read())  # it will give the whole content to read
file.close()

file = open("file1.txt",'r')
print(file.read(4))  # it will give the first 4 characters
file.close()

file = open("file1.txt",'r')
print(file.readline())  #it will read single line
file.close()

file = open("file1.txt",'r')
print(file.readline(2))  #it will read 2 characters
file.close()

file = open("file1.txt",'r')
print(file.readlines())  #it will read line by line line
file.close()'''

#write method
'''
file = open("file1.txt",'w')
file.write("test case\n")
file.write('adding another line')
print("file name :",file.name)
print("file mode :",file.mode)
file.close()

file = open("file1.txt",'r')
print(file.read())
file.close()

file = open("file1.txt",'a+')
file.write("\ntest \n")
file.write('line')
file.writelines("roshini"\
                "peyyala")
file.close()

file = open("file1.txt",'r')
print(file.read())
file.close()
'''
'''
#create new file
file = open("file2.txt",'x')
file.close()
'''
'''
#deleting a file
os.remove("file2.txt") # deleting- if we know  that this file is exist
'''
'''
if os.path.exists("file2.txt"):
    print("file exists")
    os.remove("file2.txt")
    
else:
    print("file not exists")


file = open('file1.txt','r+')
file.write("write + read")
file.close()
print("file closed or not :",file.closed)
'''
'''
file = open('file1.txt','b')
file.read()
file.close()
'''           
#tell() -> gives thecurrent position
'''
file = open("file1.txt",'r')
print(file.read(6))
print(file.read(6))
print(file.tell())
file.close()

'''
'''
file = open("file1.txt",'r')
print(file.read(6))
print(file.seek(0,1))
print(file.seek(0,0))
print(file.seek(0,2))
print("file size :",file.tell())
file.close()

'''
fd = open("fi.txt",'r')
#os.rename("fi.txt","file3.txt")

os.mkdir("new")
print(os.getcwd())
print(os.listdir())
shutil.rmtree("new")    
print(os.listdir())
fd.close()



















