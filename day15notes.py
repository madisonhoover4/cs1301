# Day 15 - turtle events

# review modules first

import turtle
import random

# instead of importing the way above.. you can

##from turtle import * # the star means everything and all
##from random import * # it makes a difference in terms of how you use them

# if you import the new way, you use them this way

##myrand = Random()
##print(randrange(1,3)) # you don't need to say random. anymore
##
##myturtle = Turtle()

##############################################################################
# TURTLE EVENTS
# an event is when something occurs such as a keypress or mouseclick event

turtle.setup(600,400)
wn = turtle.Screen()
wn.bgcolor("light blue")
tess = turtle.Turtle()
tess.speed(10)
myrand = random.Random() # create a random number generator

# keypress handlers (functions to handle keypress events)
def moveforward():
    tess.forward(30)    

def turnleft():
    tess.left(30)

def turnright():
    tess.right(30)

shapes = ["circle", "triangle", "turtle", "arrow"]

def costume():
    num = myrand.randrange(len(shapes))
    tess.shape(shapes[num])
    tess.shapesize(random.random() * 5)

def teleport():
    tess.penup()
    tess.goto(random.randrange(-300,300),random.randrange(-200,200))

# connects the keypresses to the keypress handlers we defined

wn.onkey(moveforward, "Up") # up arrow
wn.onkey(turnright, "r")
wn.onkey(turnleft,"l")

wn.onkey(teleport, "Escape") # move to a random location on the screen
wn.onkey(costume, "c") # change what the turtle looks like to a circle twice as big



# at the end of your program needs...
wn.listen()


# change the costume function to make the turtle change to randomly chosen shape
# and a randomly chosen size

# the shape needs to be either circle,triangle, turtle, arrow
# the size can be any floating point number between 0 and 2







