# day 25 - more with the weather API
# also, the pprint function

# note about test 3 - handouts from this part of the course will be on the test
# not just book material

import requests
from pprint import *

myURL = "https://www.metaweather.com"

# to get the weather from this API

fullURL = myURL + "/api/location/2357024" # atlanta's woeid

r = requests.get(fullURL)
# printing r gives you the 200 thing (just a response code)

data = r.json() # gives you data
print(data)
pprint(data)

today = data['consolidated_weather'][0]
todaytemp = today['the_temp']
print(todaytemp)
todaytemp = todaytemp*9.0/5.0 +32

# what if you don't know the woeid? do a query

r = request.get(myURL + "/api/location/search/?query=paris")
citylist = r.json()
pariswoeid = citylist[0]['woeid']

# what would the high temperature be in Paris tomorrow?

r = requests.get(myURL + "/api/location/" + str(pariswoeid))
data = r.json()
tomorrow = data['consolidated_weather'][1] # 0 is today 1 is tomorrow
paris_max_tmrw = tomorrow['max_temp']
print(paris_max_tmrw)

# which city is colder today? Vancouver or Minneapolis?
r = requests.get(myURL + "/api/location/search/?query=minneapolis")
citylist = r.json()
minnwoeid = citylist[0]['woeid']

r = requests.get(myURL + "/api/location/search/?query=vancouver")
citylist = r.json()
vanwoeid = citylist[0]['woeid']

r = requests.get(myURL + '/api/location/' + str(minnwoeid))
data = r.json()
temp2 = data['consolidated_weather'][0]['max_temp']

if temp1 < temp2:
    print('Minneapolis is colder today')
else:
    print('Vancouver is colder today')










