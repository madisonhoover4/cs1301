
# ints always round down
# but the rounding in a // action always moves left of the number line
    # which means 6 // 4 = 1 but -6 // 4 = -2
    # modulus % displays the remainder and has same precedence as M and D
    
# built in functions pow, max, and abs

##a	b	a and b
##False	False	False
##False	True	False
##True	False	False
##True	True	True

##a	b	a or b
##F	F	F
##F	T	T
##T	F	T
##T	T	T


# de Morgan's Laws
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

def daysofweek(num):
    while num <= 6 or num >= 0:
        if num == 0:
            return "Sunday"
        elif num == 1:
            return "Monday"
        elif num == 2:
            return "Tuesday"
        elif num == 3:
            return "Wednesday"
        elif num == 4:
            return "Thursday"
        elif num == 5:
            return "Friday"
        elif num == 6:
            return "Saturday"
        else:
            return "Invalid input"


# To get the last character in a word ...

fruit = "banana"
sz = len(fruit)
last = fruit[sz-1]

# or you can do fruit[-1] to get the last letter


#############################################################################
# Day 12 Class Review
# Exam is on Chapters 1-8 and 11

# types of errors:
    # 1. syntax - 2a = "hello"
    # 2. semantic - 2 + 2 = 22
    # 3. runtime "2" + 1

# int("2") = 2
# int(3.14) = 3
# int(-3.66) = -3
# int("23 dogs") = runtime ERROR

# variable rules
    # cannot start with number
    # case sensitive


# if you see a float in your operation, it will produce a float
# if you see integers, it will produce integers

# if you are given a function, at least write def hello_world(parm1,parm2)
    # and write return "hello" at the end or something


# PRINT vs RETURN

# print() ...
    # is a function
    # return value is none type
    # does not stop execution
    # can be used outside a function
    # print("hello") gets rid of quotations

    # a = print("hello")--> hello
    # print(a) --> None

# return ...
    # is a statement
    # is the return value of a function
    # stops immediately returns back to caller
    # only inside a function

def example():
    print("hello")
    return "bye"

# a = example() --> a = bye, but only prints "hello"

# print(a) --> bye


# if... boolean expression:

# elif... boolean expression:

# else:

# you can only have one if and one else

for x in range(len("Daniel")):
    print(x) # NO, will print vertically
    print("Daniel"[x]) # this print 012345


# continue says go to the next element in that interval

# range is range(start,end,steps); only one that is required, the end

# lists are mutable
# strings are immutable

############################################################################
# MONDAY NIGHT EXAM REVIEW SESSION

# regular division / always returns a float

# precedence order
    # not and or


# 1 % 13 = 1 and type is int

# strings
    # concatenation
    # multiplication
    # NO subtracting or dividing
    # indexing - aString[start:stop:step], you can do reverse if -step

# print("hi") -> hi
# return "hi" -> "hi"

# 'b' > 'a' is True, according to the ascii numbers, capitals come before
# 'A' < 'z' is True

# inputs come in as strings

def countUp(num1, num2):
    x = num1 + 1
    while x < num2:
        print(x)
        x += 1




def mysteryFunc(a, b):
    a = a+2
    b = a+2
    print(a)
    print(b)

a = 7
b = 9
x = mysteryFunc(b,a)
print(a)
print(b)
print(x)

# a function without a return value is NoneType!!
# as soon as you call a function, it will do its prints




def alternateCaps(phrase):
    newstr = ""
    x = 0
    while x < len(phrase):
        if x % 2 == 0:
            newstr+= phrase[x].upper()
            x += 1
        else:
            newstr+= phrase[x].lower()
            x += 1
    return newstr

print(alternateCaps("iloveamerica"))








        
