# Did you think the most complex way of using a random module in python is random sampling? This idea cannot be farther from the truth. It is also possible to create random stories and even beyond using the random module. 

# Here, the aim is to create a random story each time the user runs the program. The story will be the same always but with little variation with the input. This is a fun but exciting python project which will work wonders with beginners to gain confidence in python.

# In a nutshell, the program will ask users for inputs such as the name of a place, action, etc. and then build a story around the data.  



my_number_list = [5, 64, 48, 65, 43, 64, 87, 23, 65, 38, 9]

with open ('random_number.txt', 'r') as reader:
    reader_1 = reader.readlines()  
    reader_1.remove(reader_1[0])
    random_number = reader_1[0]
    with open('random_number.txt', 'w') as writer:
        for i in range(len(reader_1)):
            writer.writelines(reader_1[i])


print(random_number)
