# Day 35 Notes - more complicated recursion

def mystery1(n):
    if n == 0:
        return 1
    else:
        return n * mystery(n-1)

# this is a factorial function

def mystery2(n):
    if n == 1:
        return 3
    else:
        return msytery2(n-1) + 3

def mystery3(n, unchangingnum):
    if n == 1:
        return unchangingnum
    else:
        return mystery3(n-1, unchangingnum) + unchangingnum

print(mystery3(4,3))

# a parameter can be a list

# find the sum of the items in a list using recursion

def listsum(alist):
    if len(alist) == 0:
        return 0
    else:
        return alist[0] + listsum(alist[1:])
    
print(listsum([2,4,1,1]))


def mystery(num): 
    if num==3: 
        return 3 
    else: 
        return 1 + mystery(num-1) + 1 

print(mystery(6))

def mystery(num): 
    if num==0: 
        return 10 
    else: 
        return mystery(num-1) -1 

print(mystery(4)) 

#------------------------------------

import turtle

t1 = turtle.Turtle()
wn = turtle.Screen()

def drawSpiral(t,linelength):
    if linelength <= 0:
        wn.bye()
    else:
        t.forward(linelength)
        t.right(90)
        drawSpiral(t,linelength - 5)

# drawSpiral(t1,200)

# try this, make the spiral start small and stop at size 100


def drawSpiralbig(t,linelength):
    if linelength >= 100:
        wn.bye()
    else:
        t.forward(linelength)
        t.right(90)
        drawSpiralbig(t,linelength + 5)

drawSpiral(t1,200)

# write a function that prints out '*" patter the number of times indicated...
# by the paraneter until 1

def recprint(n):
    




recprint(5)












