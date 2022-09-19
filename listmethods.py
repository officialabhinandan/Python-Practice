a = [1,2,3,4]
print(a)

# APPEND METHOD
a.append(5)  #Adds a new element at the end
print(a)

# INSERT METHOD, syntax-> insert(position, element)
a.insert(1, 1.5) #Inserts an element in the given position 
print(a)

a.insert(3, "Abhi")
print(a)

# SORT METHOD, can sort only numbers or only alphabets at a time
b = [5,8,3,7,0,9,4]
b.sort()
print(b)

c = ['Abhi', 'Chobi', 'Kobi', 'Robi', 'Nobi']
c.sort()
print(c)

d = [5,8,7,6,4,3,7,6,0]

# POP METHOD, removes the particular element from the list

d.pop(3)
print(d)

# CLEAR METHOD, makes the whole list empty but still present in the memory

e = [1,2,6,9]
print("e list before clear:", e)
e.clear()
print("e list after clear:", e)

# REVERSE METHOD, reverses a list
c.reverse()
print("c after reversal:", c)

# INDEX METHOD, finds the index of an element
print(b.index(0))

# COUNT METHOD, counts freq of an element
print(a.count(2))
print(b.count(8))
print(c.count('Kobi'))
print(d.count(7))



