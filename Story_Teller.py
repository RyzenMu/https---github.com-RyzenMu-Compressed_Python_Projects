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

print(random_number)

import datetime
import random

now = datetime.datetime.now()

print(now.microsecond//10000)



# download dictionary file

import pandas as pd
def panda5():
    dictonary_file = pd.read_csv('dictionary.csv')

    words_column = dictonary_file['words']

    print(words_column)


    grammar_column = dictonary_file['grammar']

    print(grammar_column)

    meaning_column = dictonary_file["Meaning"]

    print(meaning_column)

    for i in range(len(words_column)):
        print('{} -- {}'.format(words_column[i], meaning_column[i]))



#reading csv file from import csv module
import csv
def csv6():
    with open('dictionary.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

import csv
def csv7():
    with open('dictionary.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)




#turn ascii value to alphabets

for i in range(65, 90):
    ascii = chr(i)
    print(ascii, end='')
print()

for i in range(97, 122):
    ascii = chr(i)
    print(ascii, end='')
print()


#convert alphabets into words of 5 letters of your choice using permutation and combination

large_alphabet = chr(random.randint(65, 90))
print(large_alphabet)

small_alphabets = ''
for i in range(4):
    small_alphabets += chr(random.randint(97, 122))

print(small_alphabets)

#create a set of 50 words and narrate a story using verbs and adjectives
for i in range(50):
    large_alphabet = chr(random.randint(65, 90))
    small_alphabets = ''
    for i in range(4):
        small_alphabets += chr(random.randint(97, 122))
    new_word = large_alphabet+small_alphabets
    print(new_word)
    dictonary_file = pd.read_csv('dictionary.csv')
    words_column = dictonary_file['words']
    words = [word for word in words_column]
    if new_word in words:
        print("new word : " , new_word)
else:
        print('No match found')

#match the generated words with dictionary words

#print the matched results


#end





