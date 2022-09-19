s = "abhinandan"

# some in-built methods in string

print("s.isalpha: ", s.isalpha())
print("s.isdigit: ", s.isdigit())
print("s.islower: ", s.islower())
print("s.isupper: ", s.isupper())

print("s.lower: ", s.lower())
print("s.upper: ", s.upper())

o = "    abhi    "

print(o.lstrip())
print(o.rstrip())

my_str = o.upper()
print(my_str) # prints a totally new string

print(o) # o remains same bcz strings are immutable
