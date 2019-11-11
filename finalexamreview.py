# Things I need to go over

# Big O
# Recursion
# Binary Hex and Decimal
# Files
# Clones and Aliases
# Sorts
# Requests Module and JSON Formatting





""" Things to Remember:
- You can add lists
- Try/Except fucntions do not return none
- Writing to a file automatically adds a newline character after your line

"""

# Big O
"""
# theoretical measure of the execution of an algorithm, usually time or ...
memory needed given the problem size n, which is usually number of items

# constant
# logarithmic
# log linear
# linear.....

# Linear Search - O(n)
    # not as efficient, unsorted or sorted lists

# Binary Search - O(logn)
    # efficient, must be sorted list
    # if list is even, searches one with lower index


# Bubble sort(On^2)
# Insertion sort O(n^2)
# Selection sort O(n^2)
# Merge sort O(nlogn)
# Quick sort O(nlogn)

"""



# Request Module and JSON Formatting
"""
# the request module is simpler than urllib
# get data from the web using apis/json (be able to explain this!)
    # we send a request, then we are returned a JSON object
    # they will turn that object into a dictionary
    # requests.get() makes a call to the api and gets info you want at the url..
    # you pass in, returns a STRING
    # .json() puts that info in a form we can understand & manipulate in python
    # type of value you did JSON to will be dictionary

"""

# Recursion

def rec1(alist):
    if ( len(alist) == 0 ):
        return 0
    else:
        first = alist[0]
        alist = alist[1:]
        return rec1( alist) + first
    
print(rec1([1,2,3]))

def rec2(alist):
    if ( len(alist) == 0 ):
        print(0)
    else:
        first = alist[0]
        print(first)
        alist = alist[1:]
        rec2( alist)
        
rec2([1,2,3])

def bunnies(numbun):
    if numbun == 0:
        return 0
    else:
        return 2 + bunnies(numbun-1)


# FINAL REVIEW SESSION 1

"""
Enumerating a list returns [ (index, item) ]
Slicing [start:stop:step] ***stops one before the stop
Indexing at [-1] gives you the last item

Packing a tuple aTup = (name, age, school)
Unpacking a tuple (name, age, school) = aTup
Swapping a tuple (a,b) = (b,a)

Aliases change an object, clones do not
Clone by copying items from one mutable data type variable to another
Make an alias by assigning one variable to another variable
When you have a clone (copy) of a list, nested lists will still be changed

Print adds its own newline character!
    -printing from a line in readlines will print a blank line


aList = None
eList = ["jack", "kate", "sawyer", "Vincent"]
bList = [2, 8, 14, 16, 23, 42, ["Ben","walt"]]
cList = ['hello','shannon','walt']
dList = ['four', 8, 14, 16, 23, 42, ["Ben","walt"], 'hello','shannon','walt']
WRONG ABOUT:
    -if you have a = 2 and make a list including a, changing a won't change list
    

Error Practice:
1. runtime
2. syntax
3. runtime
4. runtime
5. syntax
6. runtime
7. semantic
ALL CORRECT BABY

Expression and Result Practice:
None, NoneType
5, int
2, int
"2.142", string
"AAAb", string
0.0, float
5, int
Error
9.0, float
None, NoneType
True, bool
3, int
Error, error
Error, error
WRONG ABOUT:
    -"{:.3f}".format() returns a string
    -int("astring") is an error
    -Booleans work from left to right unless parentheses are given
    - 2 % 4 is 2, if number doesn't go in, answer is just first num

Conditional practice:
Elena loves memes!
2.0
here!
4
6
True
WRONG ABOUT:
    -any division returns a float

Loop Practice:
a)
x = "cs 1301 is the best"
ch = 3
while ch < 7:
    print(x[ch])
    ch += 1

b)
i = 4
for num in range(4, 24, 4):
    print(num)
WE LIT FAM

Tracing Practice:
1
2
a
1
2
a
ALL RIGHT YEAH

File I/O Practice:
"r"
readlines()
"w"
lines
" : ", 0
" : ", [1]
int(age)
str(name + "\n")
close()
close()
WRONG ABOUT:
    -make sure to change your string to ints
    -add newline characters you betch! (write won't do it for you)

Random Practice:
integer = r.randrange(2,11,2)
integer = r.randrange(10,31,10)
for num in range(10):
    print(r.randrange(1,1301))
HMMM:
    -is my second answer the same as r.randrange(1,4)*10

QUESTION 1:
a) pizza [7,5,7]
b) error - list index out of range
c) error - tuple does not support operand "+"
d) False
e) [[90,80,70],"z"]
f) error = nothing
CORRECT TILL DEATH

QUESTION 2:
one, read(), newline, empty string, close, readlines(), "f.txt", "a"
"""
# Code Writing 1:

def encode(aStr):
    if len(aStr)%2 != 0:
        for ch in aStr:
            if ch in "aeiou":
                aStr.replace(ch,"*")
    else:
        aStr = aStr[int(len(aStr)/2):]+aStr[:int(len(aStr)/2)]
        aStr[0].upper()
    return aStr


# RECURSION
print("stop") 

def rec(n):
    if n < 4:
        return 2
    print(n)
    value = rec(n-1) + rec(n-2)
    return value

rec(6)
# 6 5 4 














