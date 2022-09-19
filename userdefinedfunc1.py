def average(a,b):
    return ((a+b)/2)

print(average(2,4))




def greet():
    print("Good morning")

greet()

def greet1(name, dish="sabji"): # default dish sabji, in case not pass as a parameter in func call
    print("Good morning", name)
    print("Please eat", dish)

greet1('Abhinandan', 'rice')
greet1('Raj', 'bread')
greet1('Rita')
# reet1(5.16)  # No data type limitations




