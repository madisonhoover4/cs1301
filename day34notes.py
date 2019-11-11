# day 34 notes - more recursion

# recursively sum up the numbers between 1 and the parameter and return the...
# result

def sumup(num):
    if num ==1:
        return num
    else:
        return num + sumup(num-1)

print(sumup(100)) # returns 5050
print(sumup(3)) # returns 6

# in recursion, python uses a stack to store its current state
# can't finish until reaches base case

# try this, write a function recpyramid that prints a pyramid made of asterisks
# the first line has the parameter number of asterisks
# each following line is one less, until you get one asterisk

def recpyramid(num):
    if num == 1:
        print("*")
    else:
        print("*"*num)
        recpyramid(num-1) # prints * from num to 1

# in tail recursion, the action happens on the way back out, seen below

def recpyramid2(num):
    if num == 1:
        print("*")
    else:
        recpyramid2(num-1) #prints opposite of recpyramid (1 to num)
        print("*"*num)

# print out number from 1 to parameter in order recursively

def recprint(num):
    if num == 1:
        print(num)
    else:
        recprint(num-1)
        print(num)

recprint(25)


def sumupmystery(num,num2):
    if num == num2:
        return 0
    else:
        return num2 - sumupmystery(num +1, num2)
    
print(sumupmystery(3,8))

# write sumtwo a recursive func that sums up all even numbers
# assume parameter is even number > 2

def sumtwo(num):
    if num == 2:
        return 2
    else:
        return num + sumtwo(num -2) # if these swapped, wouldn't change anything


print(sumtwo(6))


















