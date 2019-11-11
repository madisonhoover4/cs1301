# day 9 Strings (Chapter 8 in the book)
# a string is our first compound data type
# a compound data type is a data type made up of other data items

# a string is made of individuaal characters that are indexed

word = 'Jackets'
# word[0] is just the J as a string

# len(word) is 7, indexed 0 through 6

name = 'spongebob'
print(name[1]) # will print out the p
print(len(name)) # 9
# print(name[len(name)]) will create a runtime error

# this is the slow way to get the first three letters of the name
      
print(name[0] + name[1] + name[2])

# or use slicing to make it easier
print(name[0:3])

# or use slicing to make it easier

print(name[0:3]) # spo
print(name[1:4]) # pon
print(name[1:len(name)-1]) # pongebo

# looping through a string using indicies

# loop through a string to find a particular character

def find1(astr,ch):
    for letter in astr:
        if letter == ch:
            return True
    return False            # after the loop

print(find1('cat', 'a')) # finds a in cat

# to find place, do a new function

def findPlace(astr,ch):
    place = 0
    for letter in astr:
        if letter == ch:
            return place
        else:
            place += 1
    return -1           # after the loop

def findPlace2(astr,ch):
    place = 0
    while place < len(astr):
        if ch == astr[place]:
            return place
        else:
            place += 1
    return -1           # after the loop


def findPlace2(astr,ch):
    place = len(astr) // 2
    while place < len(astr):
        if ch == astr[place]:
            return place
        else:
            place += 1
    return -1           # after the loop

# loop through a string printing out only the off indexed letters in a string

name = "spongebob"

for index in range(1,len(name),2): # 0 to 8, because spongebob is 9 letters
# it will do it in steps of 2

    
