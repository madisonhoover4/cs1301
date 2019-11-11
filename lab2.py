#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
Lab2 - API and Requests module - due Thursday, Mar. 30, 2017
"""
import requests
import time
from collections import Counter

__author__ = "MADISON HOOVER"
__collaboration__ = """ I worked on this assignment alone using only this semester's course materials. """

"""
Get an account from themoviedb.org. Go to this link and create an account: https://www.themoviedb.org/?_dc=1489731496

assign your API key to the variable below
"""
API_KEY = "852a00b89a5132fece98911b4c1a1fcf"
base_url = "https://api.themoviedb.org/3/movie/"

"""
Function name: getMovieTitle
Parameters: an int representing the ID of a movie
Returns: a string representing the original title of the movie

Description: Write a function that takes in the ID of a movie, makes an API call, and returns the <str> original title of the movie related to the ID passed in.

"""

def getMovieTitle(movieId):
    fullURL = base_url + str(movieId) + "?api_key=" + API_KEY
    r = requests.get(fullURL)
    movieinfo = r.json()
    try:
        name = movieinfo['original_title']
        return name
    except:
        return None
    
# DONE2

"""
Function name: getTopTenMovies
Parameters: **No parameters**
Returns: a list containing the original titles of the top ten rated movies

Description: Write a function that makes an API call, and returns the <str> original title of the top ten rated movies.

"""

def getTopTenMovies():
    fullURL = base_url + "top_rated" + "?api_key=" + API_KEY
    r = requests.get(fullURL)
    toprated = r.json()
    print(toprated)
    list1 = []
    for num in range(0,9):
        list1.append(str(toprated['results'][num]['original_title']))
    return list1

# DONE2 


"""
Function name: getTopMoviesInRange
Parameters: an int representing the startYear (inclusive) of the range, an int representing the endYear (exclusive) of the range
Returns: a list containing the original titles of the top three rated movies that were released between the two years passed in.

Description: Write a function that takes in a two ints representing the start (inclusive) and the end (exclusive) of a period of time, and returns the top three rated movies that were released within the period of time specified by the parameters.
             To get the top rated movies, make an API call similar to the one you did for getTopTenMovies. Then, you should go through the movies, and append the first three movies that have a releasedDate between the specified time period.

            Notes:
             Since the movie API has tons of movies in their Database, they have an optional parameter called page for their GetTopRated endpoint. If you make the API call without specifying a value for the page parameter, it will be 1 by default, giving you the first couple of top rated movies.
             The movies are splitted into different "pages" (basically, into different JSONs) because having all the movies in a single endpoint would return a really heavy JSON.
             For this function, the problem you could face is that probably the top three movies that were released in a specific time range won't be in the first page.
             Hence, after you iterate through all the movies in the json returned by the endpoint with page 1, if you haven't found the top three movies, you will have to make an API call to get the top rated movies in page 2, and iterate through those movies.
             It is also probable that the top three movies in the specified time period aren't in the second page, so you will have to make an API call to get the movies in the next page, and so on until you find them.
             The iteration and the API calls to the next pages are given to you in the base code. Consequently, you just have to write the code to iterate through the movies for a single endpoint and append the movies that fall within the time period.
"""

# ################################ #
# TODO: Function 3:  getTopMoviesInRange #
# ################################ #
def getTopMoviesInRange(startYear, endYear):
    parameters = {"api_key": API_KEY}
    topRatedUrl = "top_rated"
    response = requests.get(base_url + topRatedUrl, params=parameters)
    jsonData = response.json()
    jsonMovieList = jsonData["results"]
    
    topList = []
    page = 1
    while len(topList) < 3 and page < jsonData["total_pages"]:
        '''TODO: Complete the function to find the top three rated movies in the time range specified by the parameters
        '''
        for movie in jsonMovieList:
            a = movie['release_date']
            year = a.split('-')[0]
            year = int(year)
            if year in range(startYear, endYear) and len(topList)<3:
                topList.append(movie['original_title'])
        
            
        page += 1
        parameters["page"] = page
        response = requests.get(base_url + topRatedUrl, params=parameters)
        jsonData = response.json()
        jsonMovieList = jsonData["results"]
        time.sleep(0.3)
    return topList

# DONE2

"""
Function name: getMoviesByGenre
Parameters: a list of movie Ids <ints>, and a genre <str>
Returns: a list containing the original title <str> of the movies passed in that belong to this genre

Description: Write a function that takes in a list of movie Ids and a genre. Make API calls to get information of each movie in the list by using its Id, and append the original title of the movie it belongs to the genre passed in.

"""
# ########################## #
# TODO: Function 4: getMoviesByGenre #
# ########################## #
def getMoviesByGenre(movieIdList, genre):
    newlist = []
    for name in movieIdList:
        fullURL = base_url + str(name) + "?api_key=" + API_KEY
        r = requests.get(fullURL)
        movieinfo = r.json()
        for dict in movieinfo['genres']:
            if dict['name'] == genre:
                newlist.append(str(movieinfo['original_title']))
    return newlist

# DONE2
# should I add try except for these too?


"""
Function name: mapProductionCompaniesToMovies
Parameters: a list of movie Ids <ints>, and a list of production companies <strings>
Returns: a dictionary {keys are strings: values are lists of strings }

Description: Write a function that takes in a list of movie Ids and a list of production companies. Each movie has a list companies that were involved in their production. Your task is to create a dictionary were the keys are the production companies in the list passed in, and the values are lists containing the original titles of the movies that were produced by the corresponding company./
"""

# ############################ #
# TODO: Function 5: mapProductionCompaniesToMovies #
# ############################ #
def mapProductionCompaniesToMovies(movieIdList, companyList):
    finaldict = {}
    for company in companyList:
        movielist = []
        for movieId in movieIdList:
            fullURL = base_url + str(movieId) + "?api_key=" + API_KEY
            r = requests.get(fullURL)
            movieinfo = r.json()
            companylist = movieinfo['production_companies']
            for num in range(0,len(companylist)):
                if companylist[num]['name'] == company:
                    movielist.append(movieinfo['original_title'])
        finaldict[str(company)] = movielist
    return finaldict

# DONE2
#should I add try except for this too?














        
