#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW4 - Lists - due Feb. 13, 2017
"""
__author__ = "Madison Hoover"
__collaboration__ = """ I worked on this assignment alone using only this semester's course materials """

"""
Function name: replaceStr
Parameters: original string (str), string to replace (str), replacement string (str)
Return value: new string (str)
Description:
Write a function that takes three strings.
The first string will be the original message.
The second string will be another string that may or may
not be present in the original string. If the second string is
present in the original string, replace all instances of that string with the third
string passed in as a parameter. Return the new string.

Do not use .replace(). You are, in essence, implementing the .replace() method yourself.

"""

def replaceStr(orig,replace,new):
    list1 = orig.split(" ")
    final = ""
    x = 0
    while x < len(list1):
        if list1[x] == replace:
            final += new + ' '
            x += 1
        else:
            final += list1[x] + ' '
            x += 1
        
    return final[0:-1]

"""
Function Name: breakEven
Parameters: A string (can be random letters, one word, or a sentence)
and an int of either 1 or 2 (if it’s 1 return the 1st half, if it’s 2, return the 2nd half)
Return value: A string that contains either the front or back half of the string
Description:
Write a function that divides a string into two halves.
If the length is even, the front and back halves are the same length.
If the length is odd, the extra character goes in the front half.
If the string is of length 1, the letter goes to the front half
and the back half remains empty. Return either the front or back half of the string if the second
parameter is 1 or 2, respectively.

"""

def breakEven(string, num):
    final = ""
    for x in range(len(string)-1):
        if len(string) == 1 and num ==2:
            return ""
        if num == 1:
            if len(string) % 2 == 0:
                final += string[0:len(string)//2]
                return final
            else:
                final += string[0:len(string)//2+1]
                return final
        elif num == 2:
            if len(string) % 2 == 0:
                final += string[len(string)//2:len(string)]
                return final
            else:
                final += string[len(string)//2:len(string)+1]
                return final


"""
Function Name: stickTogether
Parameters: A list of arbitrary elements
Return value: A string that is the concatenation of all string elements in the list.
Note that non-string elements should be skipped, including nested lists.
Description:
Write a function called stickTogether that accepts a list as a parameter.
It should return a string that is the concatenation of all string elements in the list.
Note that non-string elements should be skipped, including nested lists.

"""

def stickTogether(items):
    result = ""
    for x in items:
        if type(x) == str:
            result += x
    return result

"""
Function Name: addNums
Parameters: A list of floats and/or integers. The list may be empty.
Return Value: The modified list.
Description:
Define a function that adds each item in a list of numbers (either floats or ints)
with the next element. If an item is the last element in the list, the item should be added with itself.
The function should return the modified list.
"""
def addNums(elements):
    newlist = []
    num = 0
    for num in range(0, len(elements)-1):
        a = elements[num] + elements[num+1]
        newlist.append(a)

    if elements == []:
        newlist = []
    else:
        b = 2*elements[len(elements)-1]
        newlist.append(b)
    return newlist


"""
Function Name: mergeAdjacent
Parameters: A list of ints
Return value: A list where all adjacent equal elements (same number next to each other) have been reduced to a single element.
Description:
Write a function called mergeAdjacent that accepts a list of ints as a parameter.
If the adjacent ints are equal, merge the two equals into one int of the same value.
Return a new list that has no duplicate adjacent ints.
"""


def mergeAdjacent(nums):
    finallist = []
    num = 0
    if nums == []:
        return []
    while num < len(nums):
        if len(nums) == 1:
            return nums
        if nums[num] == nums[-1]:
            if nums[num] != nums[num-1]:
                finallist.append(nums[num])
        elif nums[num] != nums[num + 1]:
            finallist.append(nums[num])
        num += 1
    if finallist == []:
        finallist.append(nums[0])
        return finallist
    else:
        return finallist


"""
Function name: findAgents
Parameters: a nested list of regions; each region is a list of names; the names are strings
Return value: a list of all the first names that occur more than once in a region
Description:
Write a function that returns a list of all the first names that occur more than once in a given region (represented by a nested list).
(See test cases for more explaination)

"""



def findAgents(regions):
    newlist = []
    for region in regions:
        firstNames = []
        for name in region:
            a = name.split()
            first = a[0]
            last = a[1]
            if first in firstNames and first not in newlist:
                newlist.append(first)
            firstNames.append(first)
            
    return newlist         



"""
Function name: bestAthlete
Parameters: a nested list; each list will contain three values; the first value will be the string name of a sport, the second value will be the amount of points a player has scored in the sport, and the third parameter will be the name of a person who has played this sport
Return value: a string representation of the player with the high score,
the sport that is being examined and the player’s score
Description:
You are helping a recruiter find an athlete for the last position open on a sports team.
Return a string that tells the recruiter the name of the most promising candidate
(the athlete who has scored the most amount of points), the sport the candidate plays, and the number of points that this player has scored.
If two players are tied for the highest score, your function should return the player that the recruiter encounters first (the player tha
appears first in the list). If there are athletes of different sports within the list return None as you can’t compare one sport with another.

"""


def bestAthlete(nestlist):
    if nestlist == []:
        return None
    score = nestlist[0][1]
    sport = nestlist[0][0]
    name = nestlist[0][2]
    for stats in nestlist:
        if stats[0] != sport:
            return None
        if stats[1] > score:
            score = stats[1]
            name = stats[2]
    bestone = str(name) + ", " + str(sport) + ", " + str(score)
        
    return bestone































    
