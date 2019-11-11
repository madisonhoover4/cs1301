"""
Georgia Institute of Technology - CS1301
Introduction to Fruitful Functions and Conditionals using Python.
"""
__author__ = "Madison Hoover"
""" I, Madison Hoover, worked alone on this assignment only using this semester's course materials """

"""
Function name: isSummerCrop
Parameters: crop (string)
Return value: True or False Boolean
Description:
Write a function that determines whether or not the parameter crop is in season.
Refer to the table in the PDF to see which crops are in season during the summer.
Return True if it is, False otherwise.
"""

def isSummerCrop(crop):
    if crop == "avocado":
        return True
    elif crop == "watermelon":
        return True
    elif crop == "plum":
        return True
    else:
        return False
    
"""
Function name: isWinterCrop
Parameters: crop (string)
Return value: True or False Boolean
Description:
Write a function that determines whether or not the parameter crop is in season.
Refer to the table in the PDF to see which crops are in season during the winter.
Return True if it is, False otherwise.
"""

def isWinterCrop(crop):
    if crop == "avocado":
        return True
    elif crop == "pumpkin":
        return True
    elif crop == "lemon":
        return True
    else:
        return False

"""
Function name: isFallCrop
Parameters: crop (string)
Return value: True or False Boolean
Description:
Write a function that determines whether or not the parameter crop is in season.
Refer to the table in the PDF to see which crops are in season during the fall.
Return True if it is, False otherwise.
"""

def isFallCrop(crop):
    if crop == "lettuce":
        return True
    elif crop == "pumpkin":
        return True
    elif crop == "ginger":
        return True
    else:
        return False

"""
Function name: isSpringCrop
Parameters: crop (string)
Return value: True or False Boolean
Description:
Write a function that determines whether or not the parameter crop is in season.
Refer to the table in the PDF to see which crops are in season during the spring.
Return True if it is, False otherwise.
"""

def isSpringCrop(crop):
    if crop == "avocado":
        return True
    elif crop == "lettuce":
        return True
    elif crop == "lemon":
        return True
    else:
        return False

"""
Function name: marketPlace
Parameters: crop (string)
Return value: int, 0 â€“ 4 inclusive
Description:
Write a function that determines how many seasons the parameter crop is in
season for by calling the four functions you wrote above. Return an int that
represents that number. This return value should be 0, 1, 2, 3, or 4.
Test Cases (not an exhaustive list):
marketPlace(â€œavocadoâ€) --> 3
marketPlace(â€œgingerâ€) --> 1
marketPlace(â€œapplesâ€) --> 0
"""

def marketPlace(crop):
    num = 0
    if isWinterCrop(crop) == True:
        num += 1
    if isSpringCrop(crop) ==True:
        num += 1
    if isSummerCrop(crop) == True:
        num += 1
    if isFallCrop(crop) == True:
        num += 1
    return num



"""
Function name: findMovie
Parameters: studio (string), director (string)
Return value: string representing the name of a movie
Description:
Write a function called findMovie where the first parameter is studio and the
second parameter is director, and returns a string representing the matching
movie. The table in the PDF shows which movie to return based on the studio and
the director.
Test Cases (not an exhaustive list):
findMovie(â€œWarner Brosâ€, â€œScorseseâ€) --> â€˜The Departedâ€™
findMovie(â€œUniversalâ€, â€œScorseseâ€) --> None

"""

def findMovie(studio, director):
    if studio == "Warner Bros":
        if director == "Spielberg":
            return "Ready Player One"
        elif director == "Scorsese":
            return "The Departed"
        elif director == "Villeneuve":
            return "Prisoners"
    elif studio == "Universal":
        if director == "Spielberg":
            return "Jaws"
    elif studio == "Paramount":
        if director == "Spielberg":
            return "Saving Private Ryan"
        elif director == "Scorsese":
            return "Hugo"
        elif director == "Villeneuve":
            return "Arrival"
    else:
        return None
    



"""
Function name: watchMovie
Parameters: rating (int), time (int)
Return value: boolean representing whether or not to watch the movie
Description:
Write a function called watchMovie where the first parameter is rating and the
second parameter is time, and returns a boolean about whether or not to watch a
movie. Return True if you are to watch a movie and False if you are to not watch
a movie.
You will not watch the movie if either of the following are true:
â€¢	The rating is less than 60
â€¢	The rating is less than 80 and greater than or equal to 60, and the time is
        either less than 105 or greater than 140
You will watch the movie if either of the following are true:
â€¢	The rating is less than 80 and greater than or equal to 60, and the time is
        greater than or equal to 105 and less than or equal to 140 minutes
â€¢	The rating is greater than or equal to 80
Test Cases (not an exhaustive list):
watchMovie(45, 115) â†’ False
watchMovie(60, 105) â†’ True
watchMovie(80, 200) â†’ True
watchMovie(75, 90) â†’ False
watchMovie(95, 90) â†’ True
"""

def watchMovie(rating, time):
    if rating < 60:
        return False
    elif rating >= 80:
        return True
    elif rating >= 60 and rating < 80:
        if time < 105 or time > 140:
            return False
        else:
            return True


"""
Function name: is_even
Parameters: number (int)
Return value: True or False (bool)
Description:
Write a function calledÂ is_evenÂ that takes an integer as an argument and returns
TrueÂ if the argument is anÂ even numberÂ andÂ FalseÂ if it isÂ odd.
"""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

"""
Function name: is_odd
Parameters: number (int)
Return value: True or False (bool)
Description:
Write a functionÂ called is_oddÂ that takes an integer as an argument and returns
TrueÂ if the argument is an odd number and False if it is even.
"""

def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

"""
Function name: is_factor
Parameters: factor(int), number (int)
Return value: True or False (bool)
Description:
Write a functionÂ called is_factorÂ where the first parameter factor is an integer
and the second parameter number is an integer. Your function should return True
if the first argument (factor) is a factor of the second argument (number).
Test Cases (not an exhaustive list):
is_factor(3, 12)  True
is_factor(5, 12)  False
is_factor(25, 15)  False
"""

def is_factor(factor, number):
    if number % factor == 0:
         return True
    else:
        return False

"""
Function name: is_multiple
Parameters: multiple(int), number (int)
Return value: True or False (bool)
Description:
Write a functionÂ called is_multipleÂ where the first parameter multiple is an
integer and the second parameter number is an integer. Your function should
return True if the first argument (multiple) is a multiple of the second
argument (number).
Test Cases (not an exhaustive list):
is_multiple(12, 3)  True
is_multiple(12, 5)  False
is_multiple(12, 12)  True
"""

def is_multiple(multiple, number):
    if multiple % number == 0:
        return True
    else:
        return False
    
