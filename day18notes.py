# Day 18 notes

import csv

# there is a csv module

filename = 'states_clean.csv'
with open(filename) as csvfile: #this opens the file and closes it
    reader = csv.reader(csvfile) # reader is a csv object
    next(reader) # skips first line
    for row in reader:
        print(row) # prints each row as a list


def get_population(state):
    with open(filename) as csvfile: 
        reader = csv.reader(csvfile) 
        next(reader) 
        for row in reader:
            if row[0] == state:
                return int(row[1])

print(get_population('Canada'))

url = 'cs1301.com/downloads/states_clean.csv'
def get_populous_states(N):
    with open(filename) as csvfile: 
        reader = csv.reader(csvfile) 
        next(reader)
        states = []
        for row in reader:
            state, population = row[0], int(row[1])
            states.append((state,population))
        sorted_states = sorted(states, key = lambda x: x[1], reverse = True)
        # reverse = True means descending
        print(sorted_states)
        return -1


# the urllib program allows you to acces websites via your program



















