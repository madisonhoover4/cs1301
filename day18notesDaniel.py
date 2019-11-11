import csv
import urllib.request
import urllib.parse

"""
PART 1. Reading and Writing Files
The file object provides a set of access methods to make our lives easier. We would see how to use read() and write() methods to read and write files.

Writing
    - The write() method writes any string to an open file.
    - Syntax: fileObject.write(string)
        * If mode is: 'w' -> creates a new file, starts from the top.
        * If mode is: 'a' -> if file exist, start from cursor (end), otherwise same as mode: 'w'
    - The write() method does not add a newline character ('\n') to the end of the string

Reading
    - The read() method reads a string from an open file.
    - Syntax: fileObject.read([count])
        * mode is: 'r'
    - Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.

"""

"""
PART 2. CSV Files

* DOWNLOAD EXAMPLE DATASET: cs1301.com/downloads/states_clean.csv

- Read a csv file and print every row:

filename = 'states_clean.csv'
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


- Write functions that does gets answers from data.

def get_population(state):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0]==state:
                return row[1]
print(get_population('Alabama'))

def get_populous_states(N):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        states = []
        for row in reader:
            state, population = row[0], int(row[1])
            states.append( (state,population) )
        return sorted(states, key = lambda x: x[1], reverse=True)[:N]

print(get_populous_states(10))
"""


""" PART 3. urllib
1. INTRO
The urllib module in Python 3 allows you access websites via your program.

This opens up so many doors for us developers!

urllib in Python 3 is slightly different than urllib2 in Python 2, but they are mostly the same. Through urllib, you can access websites, download data, parse data, modify your headers, and do any GET and POST requests you might need to do.

We just need to import urllib.requests. From there, we assign the opening of the url to a variable, where we can finally use a .read() command to read the data. The result is a massive mess, but we did indeed read the source code.


with urllib.request.urlopen('http://cs1301.com') as f:
    print(f.read().decode('utf-8'))

with urllib.request.urlopen('http://cs1301.com/downloads/RamblinWreck.txt') as f:
    print(f.read().decode('utf-8'))

"""


"""
~~~~~~~~~~~ EXTRA MATERIAL BELOW ~~~~~~~~~~~~~~
Some websites do not appreciate programs accessing their data and placing weight on their servers. When they find out that a program is visiting them, they may sometimes choose to block you out, or serve you different data that a regular user might see. This can be annoying at first, but can be overcome with some simple code.

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=hello')
    print(str(x.read()))
except Exception as e:
    print(str(e))

We overcome it by using some headers manipulations
try:
    url = 'https://www.google.com/search?q=hello'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using a browser.
    headers = {}
    headers['User-Agent'] = "Mozilla/4.0"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(str(respData))
except Exception as e:
    print(str(e))

 """
