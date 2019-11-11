# Day 10 notes - Lists (chapter 11)

# a list is a equence of smaller pieces of data, not necessarily the same type

alist = [1, 0, "cat", [1,2], 1.3]

print(alist)
print(type(alist))
print(len(alist))

# list indexing

name = "john"
print(name[0])

# you can index a list the same way

print(alist[1])
print(type(alist[2]))

# in works well with lists
if 3 in alist:
    print ("great")


# looping through lists
for item in alist:
    print(item)
    if item == "cat":
        print('meow')

# differences between lists and strings
# both are compound data types
# + and * operators work on both

# strings are all characters, lists can be any type including compound types
# lists can contain other lists or other strings

# strings are immutable (cant be changed) - lists arae mutable

name = "joe"
name = "beth"

list = [1,2,3]
list[0] = 99
print(list)

name = "gatech"
# you can't name[0] = "G"

# try this... loop through a string changing the letter e to a * when you come to it
word = "To hell with Georgia"

newword = ""
for letter in word:
    if letter == "e":
        newword += "*"
    else:
        newword += letter
word = newword # after the loo

print(word)

# what if you knew the e was at position 4
# word[4] = "*"
word = word[0:4] + "*" + word[5:] # or you can do [5:len(word)] but defaults

# or

mylist = ["t","o","","h","e","l","l"]

mylist[4] = "*"
print(mylist)


#examples of + and *

list1 = [1,2,"c"]
list2 = [3,"b",1.2]

list3 = list1+list2
print(list3)

list4 = list1 * 5
print(list4)


# try this... loop through a list of integers using a while loop that prints out...
# all the items in a list, but stops when the item in the list is > 9
# (not printing that one out)

newlist = [1,9,7,12,14,3]

for num in newlist:
    if num <=9:
        print(num)
    else:
        break


# or
num = 0
while newlist[num] <= 9:
    print(newlist[num])
    num+=1


# nested list example
nestedlist = [[1,2,3],[4,5,6]]

for minilist in nestedlist:
    for item in minilist:
        print(item)






