# Day 24 - Using an API (not in the textbook and needed for the Lab 2)
# We will be using a handout posted in t-square

import requests

# API stands for Application Programming Interface
# Just a way for a website to share info with the public, usually includes...
# documentation
# there are many APIs available w massive amounts of data if you just know...
# how to access it (some requires an API key, but many don't or will give you...
# a key if you just ask)

# here's a list of API's that don't need any keys
# https://shkspr.mobi/blog/2016/05/easy-apis-without-authentication/

myURL = "https://www.metaweather.com"
fullURL = myURL + "/api/location/search/?query=atlanta"



r = requests.get(fullURL)
print(r) # prints out the response code (200 is good)
# to get the actual data...

data = r.json()
print(data)
# this one gives a list of data for this specific query aka atlanta


templateURL = myURL + "/api/location/search/?query="

citylist = ['atlanta','paris','amsterdam','boston']
for city in citylist:
    cityURL = templateURL + city
    r = requests.get(cityURL)
    data = r.json()
    print(data)

# search by latitude and longitude
lattlongURL = myURL + "/api/location/search/?lattlong=36,-122"

r = requests.get(lattlongURL)
data = r.json()
print(data)



















