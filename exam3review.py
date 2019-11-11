# Exam 3 Review

# TRY AND EXCEPT

# some good exceptions-
    # division by zero
    # operations on incompatible types
    # accessing a list item, dict value, or object attribute that doesn't exist
    # using an identifier that has not been defined
    # trying to access a file that doesn't exist

#----------------------------------------------------------------------------

# API - Application Programming Interface

# some entity develops this and us, as a user, we can interact with their code
# we can write code, without having to know how theirs works
# used to present information to other developers or process data
# they are useful bc their code can stay private, while we are still able to...
# extract data from Applications that are already made for us

# ex. Uber uses Google Maps' API
# we build off of another application

# the request module is simpler than urllib
# get data from the web using apis/json (be able to explain this!)
    # we send a request, then we are returned a JSON object
    # they will turn that object into a dictionary
    # requests.get() makes a call to the api and gets info you want at the url..
    # you pass in, returns a STRING
    # .json() puts that info in a form we can understand & manipulate in python
    # type of value you did JSON to will be dictionary

#-----------------------------------------------------------------------------

# Big - O
# relationship b/w how much data you have and time it takes

# constant
# logarithmic
# log linear
# linear.....

# Linear Search - O(n)
    # not as efficient, unsorted or sorted lists

# Binary Search - O(logn)
    # efficient, must be sorted list
    # if list is even, searches one with lower index


# Bubble sort(On^2)
# Insertion sort O(n^2)
# Selection sort O(n^2)
# Merge sort O(nlogn)
# Quick sort O(nlogn)


#---------------------------------------------------------------------------

# OOP - Object Oriented Programming

# Classes and objects
    # the definition of the idea we are coding, it's the blueprint
        # attributes - fields of data
        # methods - functions that an instance of the class can perform

    # object - instance of class

    # init is a constructor
    # self must be put in params for all methods
    




















