def sum_of_list(a):
    print('Calculating.......')
    return sum(a)

marks =[5,4,12,63,74,108]

print(" The sum of the given marks are: ", sum_of_list(marks))


def greetings(names):
    for i in names:
        print("Hello", i)

names = ['Abhi', 'Kobi', 'Chobi'] 
greetings(names)    