names = ['Shyam\n', 'Jodhu\n', 'Modhu\n']

with open('data_write1.txt', 'w') as f: #creates new file and writes there
    f.write('Abhinandan\n')
    f.writelines(names)

# this write method creates a new file in the memory and starts writing
# if files is already present, it wipes out the old data and start writing again 
# to overcome this, we use append mode

with open('data_write2.txt', 'a') as f: #creates new file and writes there
    f.write('Abhinandan\n')
    f.writelines(names)
