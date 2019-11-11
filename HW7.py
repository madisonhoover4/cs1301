#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW7 - Dictionaries - due Monday, Mar. 13, 2017
"""
__author__ = "MADISON HOOVER"
__collaboration__ = """ I WORKED ON THIS ASSIGNMENT ALONE USING ONLY THIS SEMESTER'S COURSE MATERIALS AND RESEARCH ON THE COLLECTIONS MODULE. """

"""
Function name: charCount
Parameters: a string
Returns: a dictionary

Description: Make a function called charCount that takes in a string as a parameter and returns a dictionary. The dictionary should have each character in the string as a key and the corresponding value should be the amount of occurrences of that character.

"""

from math import *
import collections

def charCount(string):
    mydict = {}
    for ch in string:
        if ch in mydict.keys():
            mydict[ch] += 1
        else:
            mydict[ch] = 1
    return mydict
        
# DONE

"""
Function name: shopping
Parameters: a dictionary {key is the name of an item (str): value is a tuple containing the item’s cost per unit (float) and how many of that item you want to buy (int)), a list of items that are on sale (str)
Returns: a dictionary {key is the <str> name of an item: value is <float> how much was actually paid for it}

Description: Write a function that takes in a dictionary in which every key is the name of an item, and every value is a tuple with how much the item costs per unit, and how many of the item you want to buy, as well as a list of things that qualify for the store’s 20% off sale. The function should return a dictionary in which every key is the name of an item you bought, and the value is the total amount you paid for that item (i.e. unit price * quantity * .8 if the item is on sale). The dictionary should also have a key-value pair where the key is “total” and the value is the grand total for all of the things you bought.

Notes:
- All prices in the returned dictionary should be rounded to 2 decimal points.
- You can assume that all the items in the list of items on sale will be lowercase. However, not all of the items in the original dictionary will be lowercase.
- You can assume that “total” will never be a key in the original dictionary.

"""
def shopping(adict, alist):
    newdict = {}
    finaldict = {}
    for val in alist:
        val.lower()
    for key in adict.keys():
        if key in alist or key.lower() in alist:
            adict[key] = (adict[key][0]*0.8, adict[key][1])
    for key in adict.keys():
        adict[key] = float("{0:.2f}".format(adict[key][0]*adict[key][1]))
    total = 0
    for val in adict.values():
        total += val
    adict["total"] = round(total,2)
    
    return adict

# DONE

"""
Function name: dictReplaceStr
Parameters: a string, a dictionary
Returns: a string

Description: Write a function that takes in a string and a dictionary. The key to dictionary will be a string and the value is another string. In the string, replace every word that is a key in the dictionary with the value that the key maps to and return that new string.

"""

def dictReplaceStr(astring, adict):
    for key in adict.keys():
        if key in astring:
            astring = astring.replace(key, adict[key])
    return astring

# DONE
    

"""
Function name: groupAge
Parameters: a dictionary {keys are strings: values are dictionaries with member names as keys and their ages as values}
Returns: a dictionary {keys are strings of the group: values are integers with group artists’ ages}

Description: Write a function that takes in a dictionary and returns a dictionary. The function will take in a dictionary where the key will be a string that represents the name of some group and the value will be another dictionary that has the members of the group as the key and their age as the value. The function should take this dictionary and make a new dictionary where the keys will be strings of the group name and the values will be the total of all band member’s ages.

"""
def groupAge(thedict):
    newdict = {}
    for key in thedict:
        total = 0
        for key2 in thedict[key]:
            total += thedict[key][key2]
        newdict[key] = total
    return newdict
    
# DONE

"""
Function name: statistics
Parameters: a list of numbers (ints or floats)
Returns: a dictionary {keys are strings: values are lists or numbers}

Description: Write a function that takes in a list of numbers and returns a dictionary with some basic statistical measures (see table below) about the data in the list.
"""

def statistics(numlist):
    adict = {}
    lowestnum = 1e10000
    for num in numlist:
        if num < lowestnum:
            lowestnum = num
    adict["min"] = round(lowestnum,3)
    
    maxnum = -1e100000
    for num1 in numlist:
        if num1 > maxnum:
            maxnum = num1
    adict["max"] = round(maxnum,3)
    
    summed = 0
    for num2 in numlist:
        summed += num2
    adict["sum"] = round(summed,3)
    
    adict["mean"] = round(summed/len(numlist),3)
    
    sortedlist = list(numlist)
    sortedlist.sort()
    
    if len(numlist)%2 == 0:
        median = round((sortedlist[int(len(numlist)/2-1)]+ sortedlist[int(len(numlist)/2)])/2,3)
    else:
        median = numlist[int((len(numlist)-1)/2)]
    adict["median"] = median

    lister = []
    listmode = []
    dictmode = {}
    for num in numlist:
        dictmode[num] = 0
    for num in numlist:
        if num in dictmode.keys():
            dictmode[num] += 1

    x = 0
    for key in dictmode:
        if dictmode[key] > x:
            x = dictmode[key]
    lister.append(x)
    for key in dictmode:
        if dictmode[key] == lister[0]:
            listmode.append(round(key,3))
    adict["mode"] = sorted(listmode)
    

    summed2 = 0
    for num5 in numlist:
        parts = (num5 - adict["mean"])**2
        summed2 += parts
    variance = round(summed2/len(numlist),3)
    adict["var"] = variance

    adict["sdev"] = round(sqrt(variance),3)
    
    return adict










