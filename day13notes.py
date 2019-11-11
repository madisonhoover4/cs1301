# Day 13 - turtles and tuples

import turtle # this is a module

##wn = turtle.Screen()
##wn.colormode(255)
##alex = turtle.Turtle()
##alex.pencolor('blue')
##alex.goto(100,100)
##joe = turtle.Turtle()
##joe.pencolor('green')
##joe.goto(50,50)
##sue = turtle.Turtle()
##sue.pencolor('pink')
##sue.goto(200,200)
##
##turtlelist = [alex,joe,sue]
##
##for t in turtlelist:
##    t.forward(100)
##    t.right(90)
##    
### make 15 anonymous turtles
##
##tlist = []
##for num in range(15):
##    t = turtle.Turtle()
##    tlist.append(t)
##
##print(tlist)


# try this
# given a list of collors
colorlist = ['blue', 'red', 'yellow', 'pink', 'green', 'purple', 'gray', 'black', 'orange']
# create 5 turtles using a loop and set each to one of colors from colorlist

##tlist = []
##for num in range(len(colorlist)):
##    t = turtle.Turtle()
##    t.goto(num*3,num*6)
##    t.pencolor(colorlist[num])
##    tlist.append(t)
##
### change the loop above so that the 5 turtles move one at a time...
### odd numbered turtles turn 90 degrees left before moving 100
### even numbered turtles turn 90 degrees right before moving 100
##
##
##for num in range(len(tlist)):
##    t = tlist[num]
##    if num % 2 == 0:
##        t.right(90)
##    else:
##        t.left(90)
##    t.formward(100)


###############################################################################

# a tuple is a new compound data structure
# similar to a list in that it can store mixed data types
# similar to a string in that it is immutable

mytup = ('physics','10am','2300',3)

print(mytup[0]) # they can be indexed
# you can add and multiply tuples, BUT NOT APPENDED

mytup = mytup *2
print(mytup)


# tuples can contain 0 items, denoted by ()

# tuples can contain 1 item
mytup1 = ('joe',) # won't work without the comma

# can include other tuples, strings, lists, etc.

mybigtup = ((1,2), [1,2,3], "cat")

# length of mybigtup = 3

tuplist = [(1,2,3), (4,5,6), (7,8,9)]

# print out first item
for item in tuplist:
    print(item[0])

# print out last item
for item in tuplist:
    print(item[-1]) # or print(item[len(item)-1])


# what are tuples used for?
# if  you want it to be immutable

student1 = ('john',22,4.0)
student2 = ('mary',21,4.0)
student3 = ('john',22,2.1)

people = [student1,student2,student3]

print(type(student1))

# create a new turtle and set it to a random color from colorlist
    
import random
myrandom = random.Random()

wn = turtle.Screen()
wn.colormode(255)
madison = turtle.Turtle()
colornum = myrandom.randrange(0,9)
madison.pencolor = colorlist[colornum]

madison.goto(100,100)







    
