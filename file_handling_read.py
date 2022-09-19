# File Handeling in python, performing open, read or write amd close operations.

f = open('data_read.txt', 'r') # by default opens in read mode, if we don't mention

print(f.readline()) # print only 1 line
print(f.readline())
print(f.readline())

print(f.read()) #reads the whole file
print(f.read(10)) #reads only 10 characters
f.seek(12) #set the position of cursors at 12th position


for line in f:
    print(line)

f.close() # closing is compulsory

print('......Doosra method......')

# otherwise another method can be followed

with open('data.txt') as f:
    for line in f:
        print(line)  # closing is not required here, with will close automatically