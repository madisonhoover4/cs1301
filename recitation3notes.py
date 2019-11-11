# range, for and while loops, breaks, cont.

# range(start, stop, step)
# it will range from the start to one before the stop
# range(0, 10) has the default step of always 1
# range(0, 10, -1) will range from 10 -> 1

range(8, 0, -2) # 8, 6, 4, 2
# doing range(8, 0, 2) will not do anything


########################################################################
"""
You use loops when you iterate something multiple times. When you know the
number of times an action is to be repeated, use a for loop. If you don't,
use a while loop.
"""

for letter in "python":
    print(letter) # will print python's letter each on it's own line

# for loops are sometimes called for each loops
# adding a "/n" prints a new line?

for num in range(2, 10, 2): # first determine your range to be 2, 4, 6, 8
    print(num*2)
    
    
# while loops are a number based on something that changes (input)
# every for loop can be written as a while loop but not vice versa

# while (): whatever is inside the parenthesis is a boolean
# below it you put changes to your booleans
# while True: would print forever

def range2(start, stop, step):
    while(start < stop):
        print(start)
        start = start + step

range2(2, 10, 2)


def game():
    userInput = input("Do you want to continue?")
    while (userInput == "yes"):
        print("You are continuing.")
        userInput = ("Do you want to continue?")

for x in range(6): # the range of 6 is 0, 1, 2, 3, 4, 5
    print(x)

x = 0
while x<6:
    print(x)
    x += 1
    
# tell the while loop to start at a number and use the < to stop it

##########################################################################

for letter in "python":
    if letter == "t":
        continue # when you do this, it's skips the below statement & restarts 
    print(letter)

for letter in "python":
    if letter == "t":
        break # the loop will stop forever when it reaches t
    print(letter)
# anything indented to the right of "for" or "while" will be broken out of


def findEs(str): # never put quotes in a parameter, it is made for variables
    numE= 0
    for letter in str:
        if letter == "e":
            numE= numE+1
    return print(numE)

findEs("eeeeeeee")



















