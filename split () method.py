# split() method converts a string into a list ..then it will spereate the
# words with the specified in the split method

#for eg :

import random

string = "hello my name is prabal"
words= string.split(" ")

length =len(words)
x=random.randint(0, length-1)

print(words[x])
