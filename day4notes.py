# Day 4 - advanced function calls
# read book chapters 4 and 6 this week

def children():
    num = int(input("How many children do you want to have one day?"))
    numgirls = num//2
    numboys = num - numgirls
    print("Hopefully you will have",numgirls,"girls and",numboys,"boys.")

#children()

# pass input to the function using an input parameter
def children(num):
    numgirls = num//2
    numboys = num - numgirls
    print("Hopefully you will have",numgirls,"girls and",numboys,"boys.")


children(5)
# this just shows the print statement immediately without the input stop each time

# replace printed output with a return statement
# each function can only return one value
def girlchildren(num):
    numgirls = num//2
    return numgirls

def boychildren(num):
    numboys = num//2
    return numboys

myanswer = girlchildren(5) # this doesn't print anything, just computes it
print(myanswer)

########################################################################

# write a function called orderbuses that takes as it input parameters the...
# number of students and returns how many minibuses to order - assume that...
# 10 students can fit on a minibus
# always add an extra bus so no one ever has to walk

def orderbuses(numstudents):
    numbuses = numstudents // 10
    remainder = numstudents % 10
    if remainder > 0:
        numbuses = numbuses + 1
    return numbuses

orderbuses(11)
orderbuses(333)
orderbuses(3)
# these won't print out anything unless you print them

# try this one
# write a function that takes a number and returns the number doubled
# test your function using this function call

def doubleme(num):
    return (num * 2)

print(doubleme(3))

#########################################################################

# functions with if statements

# write a function that takes two parameters and returns the word "Awesome"...
# if the numbers are the same number - does not print anything out
# if the numbers are different, the function returns the word "Mismatch"
# call the function match

def match (num1, num2):
    if num1 == num2:          # use == to test for equality
        return "Awesome"
    else:
        return "Mismatch"

myresult = match(3,3)
yourresult = match(3,4)
print(myresult)
print(yourresult)

# write a function called doubleme that takes a string (someone's name)...
# and returns a string that is their name twice

def doubleme (name):
    name = name*2
    return name

print(doubleme("Madison"))

# write a function that takes two numbers and returns the word "Awesome"...
# if the first one is evenly divisible by the second number
# return the word "Lame" if that is not the case

def divide (num1, num2):
    if (num1 % num2) == 0:
        return "Awesome"
    else:
        return "Lame"


print(divide(6,3))
print(divide(7,3))




