student = ['Ram', "Shyam", 'Jodu', "Modhu"]

print(student[0])
print(student[1])
print(student[2])
print(student[3])

print(student[-1])
print(student[-2])
print(student[-3])
print(student[-4])

#slicing a list
print(student[-1:0:-1])
print(student[0:3:2])
print(student[::-1])
print(student[0:2])

student[1] = "Payel" # As lists are mutable
print(student)  

del student[2] # Deletes 2nd element
print(student)

# del student #deletes the whole string
# print(student)