# Did you think the most complex way of using a random module in python is random sampling? This idea cannot be farther from the truth. It is also possible to create random stories and even beyond using the random module. 

# Here, the aim is to create a random story each time the user runs the program. The story will be the same always but with little variation with the input. This is a fun but exciting python project which will work wonders with beginners to gain confidence in python.

# In a nutshell, the program will ask users for inputs such as the name of a place, action, etc. and then build a story around the data.  



my_number_list = [5, 64, 48, 65, 43, 64, 87, 23, 65, 38, 9]

def random_number_1():

    with open ('random_number_1.txt', 'r') as reader:
        reader_1 = reader.readlines()  
        reader_1.remove(reader_1[0])
        random_number_1 = reader_1[0]

    with open('random_number_1.txt', 'w') as writer:
        for i in range(len(reader_1)):
            writer.writelines(reader_1[i])

    with open ('random_number_1.txt', 'a') as appender:
        appender.write(random_number_1)

    random_number_1 = int(random_number_1)%10

    return random_number_1




def random_number_2():

    with open ('random_number_2.txt', 'r') as reader:
        reader_1 = reader.readlines()  
        reader_1.remove(reader_1[0])
        random_number_2 = reader_1[0]

    with open('random_number_2.txt', 'w') as writer:
        for i in range(len(reader_1)):
            writer.writelines(reader_1[i])

    with open ('random_number_2.txt', 'a') as appender:
        appender.write(random_number_2)
   
    random_number_2 = int(random_number_2)%10

    return random_number_2


random_number = str(random_number_1())+ str(random_number_2())

# print(random_number)

import datetime

now = datetime.datetime.now()

print(now.microsecond//10000)



# download dictionary file
