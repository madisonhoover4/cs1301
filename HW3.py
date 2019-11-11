#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
Introduction to Functions using Python.
"""
__author__ = "Madison Hoover"
""" I completed this homework using only this semester's course materials and TA helpdesk help. """


"""
Function name (1): countLetter
Parameters: string to iterated through (str), letter to count occurances of (str)
Return value: number of the given letter appears in the string (int)
Description:
Write a function that takes in two parameters, one being a string of any length, and the other being an individual letter to count the occurrences of.
1. Uppercase and lowercase letters should both be counted. If the letter does not appear in the sentence, return 0.
2. Must use a for-each loop.
"""

def countLetter(str, letter):
    occur = 0
    str = str.lower()
    for x in str:
        if x == letter:
            occur +=1
    return occur



"""
Function name (2): encryptMessage
Parameters: string to encrypt (str)
Return value: encrypted string (str)
Description:
You are working on a top secret project for which you have to encrypt words that come through. Write a function that takes in the word to be encrypted as a parameter and returns the encrypted word. The rules for encryption are as follows:
    1. “a” or “A” → “@”
    2. “s” or “S” → “$”
    3. “h” or “H” → “#”
    4. Numbers should not be included in the encrypted string
    5. “!” indicates to stop the encryption
"""

def encryptMessage(msg):
    newmsg = ""
    for letter in msg:
        if letter == "a" or letter == "A":
            newmsg += "@"
        elif letter == "s" or letter == "S":
            newmsg += "$"
        elif letter == "h" or letter == "H":
            newmsg += "#"
        elif letter in "1234567890":
            continue
        elif letter == "!":
            break
        else:
            newmsg += letter
    return newmsg



"""
Function name (3): encryptSentence
Parameters: sentence to encrypt (str)
Return value: encrypted sentence (str)
Description:
For the same top secret project, you are sometimes posed with the problem of encrypting sentences.
To encrypt a sentence, only words that begin with a capital letter should be encrypted.
You should call your encryptMessage() from above to encrypt words in the sentence.
"""
def encryptSentence(phrase):
    if phrase == "":
        return ""
    newsentence = ""
    s = phrase.split()
    for word in s:
        if word[0].isupper():
            newsentence += (encryptMessage(word) + " ")
        else:
            newsentence += word + " "
    a = newsentence
    return a[0:-1]



"""
Function name (4): stringPartition
Parameters: a word (str)
Return value: modified word (str)
Description:
Write a function that takes in a word as a parameter and returns a modified version of the word
in which all letters at an even index are in the first half of the string and all letters at
an odd index are in the second half of the string. The letter at index 0 should be the first letter in the modified word.
"""

def stringPartition(word):
    first = ""
    second = ""
    letter = 0
    while letter < len(word):
        if word[letter] == 0:
            first = first + word[letter]
            letter += 1
        elif letter % 2 == 0:
            first = first + word[letter]
            letter += 1
        elif letter % 2 != 0:
            second = second + word[letter]
            letter += 1
    return first + second



"""
Function name (5): sumEvens
Parameters: upper-bound for range (int)
Return value: sum of evens within the range 0 to upper-bound
Description:
1. Write a function that accepts an upper bound from a range from zero to that upper-bound. That upper bound is not included in the range.
2. After calculating the range, your function should sum up all even values within the range.
"""

def sumEvens(bound):
    total = 0
    for num in range(0,bound):
        if num % 2 == 0:
            total += num
            num +=1
    return total



"""
Function name (6): vowelsAndConsonants
Parameters: original word (str)
Return value: original word ordered by vowels and consonants
Description:
Write a function that takes a string as a parameter, and separates the vowels and consonants from one another.
1. It should return one string, consisting of the same letters of the original string, but with all of the vowels at the front of the string,
2. All of the consonants should be at the back of the string. Must iterate through the string.
Hints:
- String concatenation might help for this function.
"""

def vowelsAndConsonants(word):
    vowels = "aeiouAEIOU"
    firsthalf = ""
    secondhalf = ""
    for x in word:
        if x in vowels:
            firsthalf += x
        elif x not in vowels:
            secondhalf += x
    return firsthalf + secondhalf


"""
Function name: guessNumber
Parameters: final answer (int)
Return value: number of guesses the user took (int)
Description:
Write a function that takes an integer value in and asks the user to try to guess this answer. When the user guesses the correct value, print a congratulatory statement and tell them how many guesses it took. If the user inputs “quit” (exactly the string quit, don’t worry about edge cases like ‘QUIT’), your code should end, and print the correct answer. The integer returned if the user quits should be -1. You must use a while-loop.

Here are some test cases to show you how the function should work:

    >>> a = guessNumber(5)
    >>> “What is your guess?” —›  2
    >>> “Wrong answer, try again” —›  4
>>> “Wrong answer, try again” —›  5
      >>> “Correct! It took you 3 tries.”
_____________________________________
>>> print(a)
      >>> 3

    >>> a = guessNumber(5)
    >>> “What is your guess?” —›  2
    >>> “Wrong answer, try again” —›  4
>>> “Wrong answer, try again” —›  quit
      >>> “The correct answer was 5.”
_____________________________________
>>> print(a)
      >>> -1


"""

def guessNumber(final):
    x = 0
    guess = input("What is your guess?")
    final=str(final)
    correct = False
    while x is not correct:
        if guess == final:
            x += 1
            print("Correct! It took you " +str(x)+ " tries.")
            correct = True
            return x
        elif guess == "quit":
            print("The correct answer was " +str(final)+ ".")
            x = -1
            return x
            break
        elif guess != final:
            guess = input("Wrong answer, try again.")
            x += 1

"""
Function name (8): diamond
Parameters: a number 2-9 specifying half the width of the diamond (int)
Return value: N/A
Description:
Write a function that takes in a number specifying half the width of the diamond as a parameter and prints a diamond of those specifications.
Make sure the diamond prints in the correct format as shown in the example below. Do not hardcode this. You must use a for-loop.
"""

def diamond(num):
    for i in range(1,num+1, 1):
        width = 2*num
        num_spaces = width - (2*i)
        spaces = int((num_spaces) / 2)*" "
        print(spaces + 2*i*str(i) + spaces)
        i += 1
    for i in range(num, 0, -1):
        width = 2*num
        num_spaces = width - (2*i)
        spaces = int((num_spaces) / 2)*" "
        print(spaces + 2*i*str(i) + spaces)
        i += 1


"""
Function name (9): countDivisibility
Parameters: lower-bound value (int), upper-bound value (int)
Return value: N/A
Description:
1. Write a function that takes two parameters as the lower and upper bound of a range of intervals.The upper bound is not inclusive.
2. Within this range, your code should count the number of values that are either only divisible by 3, only divisible by 5, or divisible by both 3 and 5.
Each value can only satisfy one circumstance. For example, 15 can only be counted towards being divisible by both 3 and 5.
3. Your code should then print the counts of divisibilities in an informative way.

"""

def countDivisibility(lowerb, upperb):
    by3 = 0
    by5 = 0
    byboth = 0
    for num in range(lowerb, upperb):
        if num % 5 == 0 and num % 3 == 0:
            byboth += 1
        elif num % 5 == 0:
            by5 += 1
        elif num % 3 == 0:
            by3 += 1
    print(str(by3) + " number(s) divisible by three, " +str(by5) + " number(s) divisible by five, " +str(byboth)+ " number(s) divisible by both")



"""
Function name (10): multiTable
Parameters: number to make the multiplication table for (int)
Return value: N/A
Description:
Write a function that takes in a number as a parameter and prints the multiplication table for that number.
The table should be printed in an easy to read format.
The first row and column should display the numbers from 1 – number specified.
The top left corner of the table should remain blank as shown in the example below.
Do not hard code this. You must use a for-loop.
"""

def multiTable(num):
    print("\t", end="")
    for y in range(1, num+1, 1):
        print(str(y) + "\t", end = "")
    print()
    for x in range(1, num+1, 1):
        print(str(x) + "\t", end="")
        for y in range(1, num+1, 1):
            print(x*y, "\t", end="")
        print()






    
