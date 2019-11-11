# Day 16 - File I/O

# open a file for readings - runtime error if it cannot find the file

myfile = open("limerick.txt","r")


for count in range(5):
    line = myfile.readline() # read one line
    print(line)
    print(len(line))

myfile.close()

# read - reads the whole file into a huge string, including line breaks though
myfile2 = open("limerick.txt","r")
mystring = myfile2.read()
print(mystring)
myfile2.close()


# readlines - reads all the lines from a file into a list of strings
myfile = open("limerick.txt","r")
mylist = myfile.readlines()
print(mylist)
myfile.close()

# challenge: print out how many total characters including invisible characters...
# are in the file uglyduck.txt

myfile = open("uglyduck.txt","r")
mystring = myfile.read()
print(len(mystring))
myfile.close()

# how many capital letters are in the file uglyduck.txt 

import string
myfile = open("uglyduck.txt","r")
mystring = myfile.read()
capitals = ""
for letter in mystring:
    if letter in string.ascii_uppercase:
        capitals += letter

print(len(capitals))



# writing to a file
myfile = open("mynewfile.txt","w") # if there isn't a file with this name it...
# will make one
myfile.write("line number 1") # if you don't do \n then it won't line break
myfile.write("line number 2")
myfile.close()

# end of period challenge
# create a file called favorites and list your 3 favorite foods

# then open file and print true if the food pizza was in the list

myfile = open("favorites.txt","w")
myfile.write("pasta\n")
myfile.write("pesto\n")
myfile.write("shrimp")
myfile.close()

myfile = open("favorites.txt","r")
mystring = myfile.read()
























