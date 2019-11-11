# Day 5 - conditionals, boolean variables
# chapters 5 and 6 guide the homework

def isiteven(num):
    if num % 2 == 0:
        return True
    else:
        return False

#testing
print(isiteven(3))

myvariable = isiteven(4)
print(myvariable)
print(type(myvariable))

# logical operators for conditional results

# < > <= >= != ==

def chooseCandy(choice):
    if choice == 1:
        return "Snickers"
    elif choice == 2:
        return "Mars bar"
    elif choice == 3:
        return "Twix"
    else:
        return "Skittles"

print(chooseCandy("one")) # not equal to int 1 so you get Skittles
chooseCandy(4)
chooseCandy(1)

#############################################################################

#write a fucntion that returns the number doubled if it is less than 10
# and returns the number tripled if it is 10 or more

def multiply(num):
    if num < 10:
        return num*2
    else:
        return num*3


print(multiply(8))

#############################################################################

# conditionals can become more complicated with and, or, and not

print(3>5) # prints out False (value: False, type: Boolean)
print(3>5 or 3<5) # prints out True
print(not 3>5) # True
print(3%2 == 0) #False

num1 = 3
num2 = 0
print(num1>num2 or num2>num1) #True
print(num1<num2 and num2>5) #False
print(num1%2 == 0 or num2%2 == 0) #True
print(not num1 == 3) #False
print(not(num1==3) and not(num1<4)) #False

#############################################################################

# Nested if statements

name = "Joe"
age = 18

if age>= 18:
    print("You can vote")
    if name == "Joe":
        print("You get two votes")
else:
    print("You cannot vote")

if age >= 18 and name == "Joe"
    print("You can vote")
    print("You get two votes")
elif age >= 18:
    print("You can vote")
else:
    print("You can vote")


# try this one...
# rewrite this with a nested if statement (do not use and)
num1 = 4
num2 = 4
if num1 == 3 and num2 == 4:
    print("hi")
elif num2 == 4:
    print("go away")
else:
    print("love")

# rewritten

if num2 == 4:
    if num1 == 3:
        print("hi")
    else:
        print("go away")

else:
    print("love")


    













