# Day 8 Notes ... more iteration, break.. continue
#start reading chapter 8

# loop through a word

count= 0
for letter in "yellow jackets":
    if letter in "aeiouAEIOU":   # not in ____ is also an option
        count += 1
print(count)
        

# what if you want to keep the vowels in a string?

newstring = "" # the empty string
for letter in "yellow jackets":
    if letter in "AEIOUaeiou":
        newstring += letter    # add the letter to your new string

print(newstring)


# write a function that removes all the values from an input phrase
# return the phrase without any vowels




def devoweler(phrase):
    newphrase = ""
    for letter in phrase:
        if letter not in "AEIOUaeiou":
            newphrase = newphrase + letter
    return newphrase # if this was indented under the if it will return ""

result = devoweler("I am Madison Hoover")
print(result)

#############################################################################

for num in range(10):
    print(num)
    if num == 7:
        break  # exits the loop, prints 0 through 7
    print(num)
print("done")

# very useful for bad input from the user

# have a user enter a letter and add it on to a string when the user enters a .
# stop the loop and tell them their string, don't add the .string

newstring = ""
while True:
    letter = input("Enter a character: (enter a period when done)")
    if letter = ".":
        break
    newstring += letter
print(newstring)


# continue = restart loop




