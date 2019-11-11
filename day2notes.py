#Day 2 - Variables and Expressions
# finish chapters 3 and 4 by Friday

# a variable is an identifier (a name) that points to a value

myname = "Madison"
mynumber = 27

# Rules to variable naming: a variable can only be made up of letters,
# numbers, and an underscore _
# a variable must start with a letter
# variables are case-sensitive
# do meaningful variable names

num1 = 3
Num1 = 4
# these are two different variables, so just stick to lowercase
# 3number as a variable would break the syntax rules

# variables keep their value until you change it to something else
print(myname)

# I can change its value

myname = "Ms. Madison"
print(myname)

# it will print both names

num1 = 10
num2 = 20
print(num1 + num2)
# even though I defined num1 as 3 earlier in my code, it will use my most
# recent assignment of num1

# a runtime error would be if you divided by zero or said something undefined
# ex. of a syntax error: using & instead of + for addition
# ex. of a syntac error: forgetting a parentheses in print(   )


# variables have data types associated with them based upon the value they store

num3 = 25.2
# 25.2 is a floating point number
print(num3)
print(type(num3))

# an integer, denoted by int, is a different class (no decimal)

num1 = 5
num2 = 6
result = num1/num2

print(result)
print(type(result))
print(type(num1))
# num1 is an integer, num 2 is an integer, but result is a float

# python follows normal rules for order of operations (PEMDAS)
# () then ** then / * than + -

myname = "Queen"
mynum = 27
# result = myname + mynum

# cannot print(result) becuase you can't add two different types RUNTIME ERROR
print(type(myname))
print(type(mynum))

mynum = "33" # makes mynum a string
print(type(mynum))
result = myname + mynum
print(result) # it prints Queen33



