# day 22 exam review

# Sample Exam Topics

# KNOW KNOW KNOW dictionaries
    # from a file, in a range, etc.
    # she likes when it uses more than one data structure

# files - reading and writing
    # if you open and close a file in for loop it will keep restarting the read
    # so you created an infinite loop

# strings
    # go back to chapter 8
    # split, strip, get rid of first or last character, concatonate, etc.
    # string functions are useful with files

# modules
    # random, math
    # know randrange
    # urllib.request
    # NOT time module
    # NOT csv
    # NOT turtle
    # know different types of importing

# immutable v. mutable
    # what does it mean for something like a dictionary key
    # what types of data can be a dictionary key
    # a list CAN'T be a dictionary key, even Nonetype could

# events
    # just know what an event is
    # doesn't involve coding
    # might have to say why you are saying .listen()
    # a listener is a program waiting for those events, otherwise won't do

# scope
    # tracing global and local variables and functions

# number system conversion
    # binary to hex
    # hex to decimal
    # first thing on the test

# --------------------------------------------------------------------------

# tracing sample

def traceMe(tupleList):
    total = 0
    for num2 in range(1,3):
        total += tupleList[num2][0]
    return total

print(traceMe([(3,2),(1,4),(8,9)]))

# returns 9


num = 3
num2 = 9
def myscope(num):
    num += 1
    print(num)
myscope(num2)
print(num)

# returns 10 ,3

# sample coding

# create a dictionary from the contents of a file
f = open("grades.csv","r")
lines = f.readlines()
f.close()

mydict = {}
for line in lines:
    piecelist = line.split(",")
    mydict[piecelist[0]] = float(piecelist[1].strip())

print(mydict)













    




