# Day 20

# learn scope

# global variables are not in a function, local variables are in functions
    # printing a variable inside a function will print the local
    # printing a variable outside a function will print the global

# if you define a function as range (which is a predefined function), it will
    # rewrite the function becuase yours is higher precedence


a = 9

def func():
    # print(a) would cause an error
    a = 3 
    print(a) # prints local

func()
print(a) # prints global

# only use global variables when they are used in more than 1 function

###############################################################################

# def range(num):
    # print(num + 1)


# for count in range(10): # Error: NoneType object is not iterable
 #    print(count)

# it will think you are calling your own range function

num = 15

def myfunc2(n):
    print(n+1)
    num = 18
    print(num)

print(num)
myfunc2(num)
print(num)

# 15
# 16
# 18
# 15

###############################################################################

# Dictionaries

newdict = {}
anotherdict = {'joe':18,'tom':22}
anotherdict['sue'] = 84

print(anotherdict)

# order does not matter

# practice
# use a loop to create a dictionary where the keys are the numbers from 1 to 10
# the values are double the key

# dict should look like {1:2,2:4,3:6...10:20}

mydict = {}
for num in range(1,11):
    mydict[num] = 2 * num

print(mydict)


# show what the dictionary would be like after this loop

mynewdict = {}
for num in range(3):
    for num2 in range(4):
        mynewdict[num] = num2

print(mynewdict)

# this above does not work the same as the previous scenario























