### day 7 - more loops
##
### runnning counts and totals
##
### running count - add 1 each time an element is found
##count = 0
##for letter in "I love CS1301, it is my favorite class":
##    if letter == ' ':
##        print(letter)
##        count += 1
##print("There were", count, "occurences.") # if this statement was in line with..
### if, then it would print there were 0, 0, 0, 1, 2, 3, ...
##
##################################################################################
##
### running sums
### instead of adding 1 each time, add the element itself
##
##
### if a number is even, add it to a running total
### a.k.a. sum up all the even numbers between 0 and 999
##
##sum = 0
##for num in range(1000): # really this is 0-999
##    if num%2==0:
##        sum = sum + num
##
##print("The sum of the even numbers is", sum)
##
##
### have a user enter a number repeatedly until the total of all the numbers is..
### greater than 100
##
##
##total = 0
##
##while total <= 100:
##    number = int(input("Enter a number"))
##    total = total + number
##print("total is", total)


# print out how many vowels are in the string phrase
# phrase = "i love the atlanta falcons and hope they win the superbowl"

phrase = "i love the atlanta falcons and hope they win the superbowl"
phrase = phrase.lower()
count = 0
for ch in phrase:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count+=1
print(count)

# "A" != "a"


phrase = phrase.lower() # converts a phrase to lowercase


# try this... write a function that takes as input a phrase and counts how...
# many letters are in the phrase up until the point at which a blank occcurs

def countFirstWord(phrase):
    count = 0
    for letter in phrase:
        if letter == ' ':
            return count
        else:
            count += 1



print(countFirstWord('I love Computers') # should print out 1
print(countFirstWord('Atlanta rocks') # should print out 7

      






