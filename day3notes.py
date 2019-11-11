# day 3 - modulus, functions, input statement
# homework will be on chapters one through four, try it this weekend

# division is complicated in python - because there are two division operators
#       /     and      //

print(3/5) 
# This gives 0.6

print(3//5)
# This is integer division so it tells you how many whole number values of 5...
### go into 3, which is 0
##
### another operator % is the modulus operator, which gives you the remainder
##
##print(12%5) # how many are left over when 5 is divided into 12?
### 2 times with two leftover
##
###On a mini quiz, it'll say, what would be the result of these?
##10//5 # = 2
##4%2 # = 0
##5%2 # = 1
##100//9 # = 11
##
###-----------------------------------------------------

#input statements allow your user to enter a number

print("enter your name") # then do the input statement
#or easier...
name = input("What is your name?")
print(name * 2) # it displays MadisonMadison
print((name + " ") *2) # it displays Madison Madison

#what if you want numbers?
age = input("How old are you?")
print(age)
print(type(age)) # but it says my 18 is a string, not an integer
#input statements always give a string unless you convert to int or float

age = float(age) # this converts the string to a float
# but it will be a runtime error if you try and convert words in your input to...
# a float or integer

print(age + 1)

#-----------------------------------------------------

##numbusses = input("How many can fit on each bus?")
##numstudents = input("How many students are there?")
##numbusses = int(numbusses)
##numstudents = int(numstudents)
##
### how many mini busses are needed?
##print("You will need to order this many busses:")
##print(numstudents // numbusses)
##
##print("You will have this many students who have to walk")
##print(numstudents % numbusses) # aka how many are in the remainder?

#------------------------------------------------------
##try this... have the user enter his/her age
# tell them how old they will be in 10 years

age = input("How old are you?")
age = int(age)

newage = age + 10
print("In ten years, you will be", newage)

#-------------------------------------------------------
##
###function: a block of code associated with a name
##
##def sayHello():
##    print("Hello World!")
##    print("You look beautiful today!")
##
##
##sayHello() # if you don't write this out, the fuction won't get called
##sayHello()
##sayHello()
##
##
##def sayGoodbye():
##    print("So long cruel world!")
##
##sayGoodbye() # functions are performed in the order you call them, not in...
### the order they are defined






