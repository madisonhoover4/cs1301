#! /usr/bin/python3
import requests
import json
from pprint import pprint

MAIN_URL = "https://www.metaweather.com"

"""
# ################### #
#   Location Search   #
# ################### #
Docs:
    https://www.metaweather.com/api/#locationsearch
URL:
    /api/location/search/?query=(query) or
    /api/location/search/?lattlong=(latt),(long)

Arguments:
    Either query or lattlong need to be present.
    query
        Text to search for.
    lattlong
        Coordinates to search for locations near. Comma separated lattitude and longitude e.g. "36.96,-122.02".
Examples:
    * /api/location/search/?query=san
    * /api/location/search/?query=london
    * /api/location/search/?lattlong=36.96,-122.02
    * /api/location/search/?lattlong=50.068,-5.316
"""
location_search_url = "/api/location/search/"

"""
# ############## #
#    Location    #
# ############## #
Docs:
    https://www.metaweather.com/api/#location
URL:
    /api/location/(woeid)/
Arguments:
    woeid
        Where On Earth ID. Docs.
Examples:
    * /api/location/44418/ - London
    * /api/location/2487956/ - San Francisco
"""
location_url = "/api/location/{}/"
"""
# ############### #
#  Location Day   #
# ############### #
Docs:
    https://www.metaweather.com/api/#locationday
URL:
    /api/location/(woeid)/(date)/
Arguments:
    woeid
        Where On Earth ID. Docs.
    date
        Date in the format yyyy/mm/dd. Most location have data from early 2013 to 5-10 days in the future.
Examples:
    * /api/location/44418/2013/4/27/ - London on a 27th Apr 2013
    * /api/location/2487956/2013/4/30/ - San Francisco on 30th April 2013
"""
location_day_url = "/api/location/{}/{}/"


"""
Where to find WOEID (Where On Earth ID)?
    http://woeid.rosselliot.co.nz/
"""
LOCATIONS = {
    'Atlanta':'2357024',
    'London':'44418',
    'New York':'2459115',
    'San Francisco':'2487956',
    'Los Angeles': '2442047'
    }

def get_5_day_forecast(woeid):
    """ gets a dictionary of the weather for today and the next 5 days

        key: date [year-month-yeah] (i.e. 2017-03-14)
        value: a tuple of (max_temp, min_temp, state)
    """
    r = requests.get(MAIN_URL+location_url.format(woeid))
    r.raise_for_status()
    data = r.json()
    # uncomment the next line to see how a JSON object looks like #
    # pprint(data)
    days = {}
    for day in data['consolidated_weather']:
        date = str(day['applicable_date'])
        max_temp = int(day['max_temp'])
        min_temp = int(day['min_temp'])
        state = str(day['weather_state_name'])
        days[date] = (max_temp, min_temp, state)
    return days

def get_current_weather(woeid):
    """ Get the current weather in Celsius """
    r = requests.get(MAIN_URL+location_url.format(woeid))
    r.raise_for_status()
    data = r.json()
    # uncomment the next line to see how a JSON object looks like #
    # pprint(data)
    today = data['consolidated_weather'][0]
    return today['the_temp']

def search(s):
    """ Perform a search query on s """
    query = {'query':s}
    r = requests.get(MAIN_URL+location_search_url,params=query)
    r.raise_for_status()
    data = r.json()
    return data

if __name__ == '__main__':
    # PART 1. Play with 5 day forecast
    try:
        woeid = LOCATIONS['San Francisco']
        forecast = get_5_day_forecast(woeid)
    except requests.HTTPError as e:
        print("Error while getting 5 day forecast!\nMake sure you have a valid woeid")
        print(e)
    else:
        """ The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement. """
        print("This is your forecast for today and the next 5 days:")
        for day in forecast:
            h,l,state = forecast[day]
            print("Day: {} - {} ({},{})".format(day, state,l,h))

    print("-"*70)
    # PART 2. Play with getting current weather
    try:
        woeid = LOCATIONS['Atlanta']
        current = get_current_weather(woeid)
    except requests.HTTPError as e:
        print("Error while getting current weather!\nMake sure you have a valid woeid")
        print(e)
    else:
        print("The current weather is: {}".format(current))
    print("-"*70)
    # PART 3. Play with getting search results
    try:
        query = "San"
        results = search(query)
    except requests.HTTPError as e:
        print(e)
    else:
        if len(results) != 0:
            print("These are all the results I was able to find for {}:".format(query))
            for result in results:
                title = result['title']
                print(title)
                print('\tLocation Type = {}'.format(result['location_type']))
                print('\twoeid = {}'.format(result['woeid']))
                print('\tLattitude and Longitude = {}'.format(result['latt_long']))
        else:
            print("Unable to get any results for {}".format(query))
