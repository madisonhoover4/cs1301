# Day 14 - modules

import math # module that gives you access to pi, sqrt
import turtle # turtle functions

# new one
import random # gives you access to random numbers
# there's another step
myrandom = random.Random() # creates a new random number generator
# you onlu need to do this once


for i in range(10):
    print(myrandom.randrange(1,6)) # prints a random number between 1 and 5
    
friendlist = ['joe', 'tom', 'ben', 'sue', 'mary', 'carl']

mypick = myrandom.randrange(0, len(friendlist))
print("My best friend today is",friendlist[mypick])

# create a favfood functions

favfoods = ['pizza', 'chicken sandwich', 'spaghetti', 'meatloaf', 'sushi']

# generate a tuple of a random friend and food

##friendnum = myrandom.randrange(len(friendlist))
##foodnum = myrandom.randrange(len(favfoods))
##mytup = (friendlist[friendnum],favfoods[foodnum])

##print(mytup)
# you can return two things from a function with a tuple

for count in range(7):
    friendnum = myrandom.randrange(len(friendlist))
    foodnum = myrandom.randrange(len(favfoods))
    mytup = (friendlist[friendnum],favfoods[foodnum])
    print(mytup)

# the loop above could possibly select the same food or friend multiple times
# if you don't want that to happen, you keep a list of ones already used

# try this... roll 2 dice continuously, generating a number sum of two dice
# do this until a seven has been rolled, then tell them you rolled lucky 7

sum = 0
while sum != 7:
    die1 = myrandom.randrange(1,7)
    die2 = myrandom.randrange(1,7)
    sum = die1 + die2
    print(sum)

print("You rolled lucky number 7!")


# OR

while True:
    diceroll = myrandom.randrange(2,13)
    print(diceroll)
    if diceroll == 7:
        print("You rolled lucky 7")
        break


print(myrandom.random()) # generates one random float between 0 and 1






















