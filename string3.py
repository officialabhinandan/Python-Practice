#string slicing
str = "abcdefg"

print(str[1:3])
print(str[1:])
print(str[:4])
print(str[3:])
print(str[0:5:2]) # print 0th to 4th index with freq 2
print(str[::-1])  # reverse of str using negative indexing
print(str[0:5:-1], "Blank space") # print nothing as direction is given backward while traversing forward
print(str[-1:0:1], "Blank space") # # print nothing as direction is given forward while traversing backward
print("Printed blank space for line 9 and 10")


