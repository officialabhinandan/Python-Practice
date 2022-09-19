# Similar with set. Here everything stores in key:value pair.
# All the pairs are heterogenious in nature.
# Dictionaries are mutable.
# Repeatation of same keys are not allowed here, if repeated the value of previous one will be updated.


my_dic = {'Biden': 87, 'Modi':99, 'Putin': 67, 32: 23, 2:'Xinping', 'NK': 'Kim', 7: ['a', 'b', 'c']}
print(my_dic['Biden'])
print(my_dic[32])
print(my_dic[2])
print(my_dic['NK'])
print(my_dic[7])

my_dic['Truss'] = 49 #Adding new elememnts
print("After addition: ", my_dic)

my_dic['Putin'] = 71 #Updating older elements
print("After updation: ", my_dic)



sqr = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
for i in sqr:
    print("Key", i, ":", sqr[i])
