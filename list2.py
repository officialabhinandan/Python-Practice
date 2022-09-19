# list comprehension
# listname = [(expression) (for item in the list)  (if condition)]

a = [x for x in range(100)]
print(a)

a = [x for x in range(100) if x % 2 == 0]  # prints only even number within range
print(a)

a = [x for x in range(100) if x % 2 == 1]  # prints only odd number within range
print(a)

n = int(input("Enter a no\n"))
b = [n**i for i in range(10)]
print(b)
