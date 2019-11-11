# day 6 - finish conditionals, start loops, range function


# and is higher precendence than or in if statements

num = 5
if num > 3 and num < 4 or num == 7:
    print("hello")


########################################################################

# next topic while loops, read chapter 3 with turtles to understand better


# if you need to repeat something many times it needs to be indented inside a loop
# 2 kinds of loops - while loops and for loops

num = 5
while num == 5:
    print("Hello")
    num = 23
print("done")


# it goes back and it checks to see if num still = 5 and prints over and over

# while loops have to have a way to stop

num = 1
while num <= 10:
    print(num)
    num = num + 1 # don't forget this!!
print(num) # this changes the fina value to 11


age = int(input("How old are you?"))
while age < 21:
    print("Have a soft drink sir")
    age = int(input("How old are you?")) # it will keep asking how old until...
          # you are over 21 years old



# write a loop that will cont. to ask a person to enter a value until they ...
# enter the number 7

number = int(input("Enter a number"))
while num != 7:
    num = int(input("Enter a number"))

########################################################################
# for loop


print(range(4)) # generates the numbers 0, 1, 2, 3 but prints "range(0, 4)"

for num in range(4): # python assumes you are starting at 0
    print(num) # this prints 0, 1, 2, 3 on its own line

for num in range(1, 4):
    print(num) # prints out 1, 2, 3 because it always stops before the end

for num in range(0,52): # prints odds 1 to 51
    if (num%2==1):
        print(num)

# write a for and while loop that prints out the even numbers from 5 to 10
# output should be 6, 8, 10

for num in range(5,11):
    if num%2==0:
        print(num)


num = 5
while num <= 10:
    if num%2==0:
        print(num)
    num = num + 1 # shortcut to num = num + 1 can be written as num+=1



# fun use of for loops

for letter in "Madison": # loops thru letter of a word
    print(letter * 10)
print(letter)



