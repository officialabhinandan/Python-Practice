a = input('Enter first no ')
print(type(a))
# Always returns value in String
b = int(input('Enter second no '))
print(type(b))
# After typecasting to integer, now it retuens Integer
c = int(input('Enter third no '))

result1 = b*c
print(result1)

result2 = a*b
print(result2)

# Gives wrong answer, can't perform multiplication with string
