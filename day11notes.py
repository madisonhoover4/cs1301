# Day 11 - more lists and strings

# test wednesday, review session Monday at 5
# more review in class Monday

import string # gives you access to useful string functions and constants

print(string.ascii_letters)

# you can use it in string.ascii_uppercase or lowercase too

name = "Falcons"
print(name.find("a")) # you put the string first before the .


print(name.replace('a','e'))

def myreplace(astring,oldletter,newletter):
    place = 0
    newstring = ''
    while place < len(astring):
        if astring[place] == oldletter:
            newstring += newletter
        else:
            newstring += astring[place]
        place += 1
    return newstring


def myreplace2(astring,oldletter,newletter):
    place = 0
    newstring = ''
    for place in range(len(astring)):
        if astring[place] == oldletter:
            newstring += newletter
        else:
            newstring += astring[place]
    return newstring

def myreplace2(astring,oldletter,newletter):
    place = 0
    newstring = ''
    for letter in astring:
        if letter == oldletter:
            newstring += newletter
        else:
            newstring += letter
    return newstring




print(myreplace("Falcons",'n','p')) # replace all the n's with p's

###########################################################################

# escape sequences

myname = "R\2\D\2" # prints R\D
print(myname)

## \n makes it go down to the new line - newline character

print("h\n\n\ng") # the length is 5

# if you actually want a \, you must type two

print("joe\\mary") # = joe\mary

############################################################################

# lists odds and ends - Append and Delete

list = [1,2,'a',3]

list.append('Falcons')
print(list)

# you cannot append something onto the end of the string

del list[1]
print(list)













