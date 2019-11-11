/#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW5 - Tuples and Modules - due Feb. 23, 2017
"""
__author__ = "Madison Hoover"
__collaboration__ = """ I worked on this assignment alone using only this semester's course materials. """

"""
Question #1: (10pts)
Function name: complex_calculator
Parameters: a string and a list
Return value: An int, a float, or None

Description: Write a function that takes two arguments. The first argument will be a name (string). The second argument will be a list of numbers. The name will decide what function from the math module will be used. Refer to the table below to decide which name will correspond to which math function. If the name passed into the function is not one in the table, return None. The list of numbers contains the arguments to be used for the math function. However, some of these math functions take only 1 parameter and others take 2. Assume that if the math function needs one parameter, the list will be of length one, and if the math function needs two parameters the list will be of length two.
"""

import math
def complex_calculator(name, alist):
    if name == "ceil" or name == "CEIL":
        return math.ceil(alist[0])
    elif name == "fabs" or name == "FABS":
        return math.fabs(alist[0])
    elif name == "gcd" or name == "GCD":
        return math.gcd(alist[0], alist[1])
    elif name == "pow" or name == "POW":
        return math.pow(alist[0], alist[1])
    elif name == "hypot" or name == "HYPOT":
        return math.hypot(alist[0], alist[1])
    else:
        return None

# DONE
        
    
"""
Question #2: (10pts)
Function name: extract_information
Parameters:  A string
Return value: A tuple of length 3

Description: Write a function that takes in a string containing information about a person. You may assume that the string will always be formatted in this way: â€œNAME: AGE, SCHOOLâ€. Return a tuple in the format (NAME (string), AGE (int), SCHOOL (string)).
"""

def extract_information(astring):
    list1 = astring.split(": ")
    list2 = list1[1].split(", ")
    name = list1[0]
    age = int(list2[0])
    school = list2[1]
    return (name, age, school)

# DONE

"""
Question #3: (10pts)
Function name: create_addressbook
Parameters:  A list of strings
Return value: A list of tuples

Write a function that takes in a list of strings. The list can be empty, in which case return an empty list. Each string contains information about a person. You may assume that the string will always be formatted in this way: â€œNAME: AGE, SCHOOLâ€. Call the extract_information function to convert each string to a tuple. Add the tuples into a list. However, the tuples in the new list should be formatted (SCHOOL (string), NAME (string), AGE (int)). If there are two people with the same name, only the most recent information (the information last in the list) should be added. Return the list.
"""

def create_addressbook(alist):
    if alist == []:
        return []
    namelist = []
    for x in alist:
        name, age, school = extract_information(x)
        y = school, name, age
        for i in namelist:
            if i[1] == name:
                namelist.remove(i)
                break
        namelist.append(y)
    return namelist
        
# DONE




"""
Question #4: (20pts)
Function name: get_averages
Parameters: A list of tuples
Return value: A list of tuples

Description: Write a function that takes a list of tuples. The tuples in the list contains integers and floats. The list and tuples could be of any length (it can be empty). For each tuple, find the average of all the numbers and multiply each entry of the tuple by that average (each entry should be at max 2 decimal places). Return the new list of tuples.
"""



def get_averages(alist):
    returnList = []
    for tup in alist:
        total = 0
        newtup = ()
        if tup == ():
            newtup = ()
        else:
            for value in tup:
                total += value
            avg = total / len(tup)
            for value2 in tup:
                temp = value2*avg
                temp = round(temp,2)
                newtup += (temp,)
        returnList.append(newtup)
    return returnList

# DONE

"""
Question #5: (25pts)
Function name: party_time
Parameters: A list of tuples, an int
Return value: A tuple

Description: Write a function that takes in a list of tuples and an integer representing the max amount of people allowed in the party (size of the returned tuple). Each tuple with be comprised of a name of a person (string) and the priority status of that person (int) (status will be between 1 and 10, inclusively). You can assume a person with a priority status of 1 will be allowed in the party before someone of the priority status of 5. If more than one person has the same priority status, then you should give priority to the person who appears first in the list. When crafting the returned tuple, make sure to place the people in the tuple in order of priority.  Return the tuple of guest names.
"""


def party_time(guests, maxppl):
    namelist = []
    finallist = ()
    for num in range(1,11):
        for tup in guests:
            if tup[1] == num:
                namelist.append(tup[0])
                del tup
    if len(namelist) < maxppl:
        return tuple(namelist)
    x = 0
    while x < maxppl:
        finallist += (namelist[x],)
        x += 1
    return finallist

# DONE       

"""
Question #6: (25pts)
Function name: ocd
Parameters:  A list of 3 tuples
Return value: A list of 3 tuples

Description: Write a function that takes in a list of 3 tuples. The tuples could be of any length (however, assume it will not be empty). The tuples will contain ints and floats. Make a new list of three tuples. The tuples should be the same lengths as the ones passed in. However, the content should be sorted in ascending order. In other words, sort the contents of the list while keeping the lengths of all the tuples the same. Return the list.
"""

def ocd(tuplist):
    newlist = []
    for num in range(0, len(tuplist)):
        for num2 in range(0, len(tuplist[num])):
            newlist.append(tuplist[num][num2])
    newlist.sort()
    counter = 0
    finallist = []
    for i in range(len(tuplist)):
        newtuplist = []
        for j in range(len(tuplist[i])):
            newtuplist.append(newlist[counter])
            counter += 1
        finallist.append(tuple(newtuplist))
    return finallist

# DONE






