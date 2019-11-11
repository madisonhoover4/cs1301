# Day 32 - exam 3 review

# Handouts 1 (API) and 2 (Big-O) will be covered
# Chapters 14, 15, 16, 19, and 21
# List algorithms, enumerate, OOP, try...except...finally

# MOST IMPORTANT IS OOP

# be able to create and use classes...
# determine big O of code...
# recognize all the sorts we covered (minus quick)
# use enumerate in chap. 14
# assign a default value to a parameter

#---------------------------------------------------------------------------

# enumerate - gives you indices and values in an iterable data structure

mylist = ['a', 'b', 'c']
for item in enumerate(mylist):
    print(item)

myname = "Madison"
for mytup in enumerate(myname):
    print(mytup[1], 'is at position', mytup[0])


#---------------------------------------------------------------------------

# default parameter - sets a parameter if none is given instead of error

def myfunc(num = 0):
    print(num)

#----------------------------------------------------------------------------

# big O of code

total = 0
for num in range(5):
    for num in range(4):
        total +=1

# This is O(1), nothing changes if input gets bigger

alist = [0,1,2,3,4]
for num in range(len(alist)):
    for num in range(len(alist)):
        print(num)

# This is O(n^2) because changes based on list size
# If they are different listss, must be O(a*b)
# If length of alist is 1/2 length of blist it is still O(n^2) even though...
# it is twice as fast

n = 2
for num in range(n):
    index = n
    while index > 0:
        print(index)
        index = index // 2

# This is nlogn (if it 1000, you only run it 10 times)
# it would be only logn if there was no first line

#----------------------------------------------------------------------------
        
# class

# try this... create a rectangle class that contains 2 attributes: len and width
# it also has three methods: a constructor, area, and an __eq__ method that...
# returns true if 2 rectangles have same length and width
# and a method that tells ur class to print out the area when you attempt...
# to print the rectangle

class Rectangle:

    def __init__(self, length=100, width=100): # set default parameters
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
        

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width
    

    def __str__(self):
        return str(self.area())

r1 = Rectangle(100,50)
print(r1)
r2 = Rectangle(200,100)
print(r1 == r2)
r3 = Rectangle(200, 100)
print(r2 == r3)

# write the code necessary to generate a list of 100 rectangles, all 100 x 100

rectanglelist = []
for num in range(100):
    rectanglelist.append(Rectangle(100,100))

print(rectanglelist[0])

# ask the user to enter two numbers and create a rectangle of that size

width1 = int(input("Width?"))
length1 = int(input("Length?"))

r4 = Rectangle(width1,length1)














