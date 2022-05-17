import os

# Reading a file
file = open("file1.txt",'r')
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
file.close()

#write method

file = open("file1.txt",'w')
file.write("test case\n")
file.write('adding another line')
file.close()

file = open("file1.txt",'r')
print(file.read())
file.close()

file = open("file1.txt",'a')
file.write("test case\n")
file.write('adding another line')
file.close()
'''
#create new file
file = open("file2.txt",'x')
file.close()
'''
'''
#deleting a file
os.remove("file2.txt") # deleting- if we know  that this file is exist
'''

if os.path.exists("file2.txt"):
    print("file exists")
    os.remove("file2.txt")
    
else:
    print("file not exists")
    




















