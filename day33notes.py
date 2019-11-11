# day 33 - recursion - chapter 18

# interactivepython.org has a good explanation of recursion

# recursion works by reducing the prblem into smaller pieces over and over
# until you get to a piece that you already know the answer to
# it does this by calling itself

def countdown(num):    # print all the numbers from num to 1 then print blastoff
    if num ==0:
        print("Blastoff!")
    else:
        print(num)
        countdown(num-1)

countdown(5)
        
    
# 3 requirements for recursion
# 1) the function must include a call to itself
# 2) the function must have a base case (a way to stop)
# 3) the function call must be approaching the base case every time

# try this....print the even numbers from the its even parameter to 2 using recursion

##def printevens(num):
##    if num == 2:
##        print (2)
##    else:
##        print(num)
##        printevens(num - 2)
##
##
##printevens(100)


# try this one....
# print out the numbers from 1 to 100 in forward order this time!

def printnums(num):
    if num > 100:
        pass
    else:
        print(num)
        printnums(num+1)

printnums(1)


# what would this do?  infinite cursion
##def rec1(num):
##    if num > 0:
##        print(num)
##        rec1(num)
##
##rec1(100)


def rec2(num):
    if num > 0:
        print(num)
        rec2(num + 1)

 # rec2(100) this is an infinite loop


# recursion can return a value



