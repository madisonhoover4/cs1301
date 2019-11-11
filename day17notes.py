# Day 17 - CSV files

# csv stands for comma separated values

myfile = open("city_crime.csv","r")
linelist = myfile.readlines()
print(linelist)
myfile.close()

# everything is now stored in linelist

# print out the rate for all the cities in the file

for count in range(1, len(linelist)): # from 1 because you don't want header
    line = linelist[count]
    pieces = line.split(",")
    print(pieces[3]) # the type is a string!!

# try this... change the loop to sum up the crime, print total

total = 0
for count in range(1, len(linelist)):
    line = linelist[count]
    pieces = line.split(",")
    rate = float(pieces[3])
    total += rate
print(total)

# try to print out the city with the highest rate of crime
highestsofar = 0
citywithhighest = ""
for count in range(1, len(linelist)):
    line = linelist[count]
    pieces = line.split(",")
    rate = float(pieces[3])
    if rate > highestsofar:
        highestsofar = rate
        citywithhighest = pieces[2]
print(citywithhighest)


# crime_data.csv

# print out all the the council districts
myfile = open("crime_datat.csv","r")
linelist = myfile.readlines()
myfile.close()

##for count in range(1, len(linelist)):
##    line = linelist[count]
##    pieces = line.split(",")
##    print(pieces[1])

# change the code above to print only districts with bicycle theft

##for count in range(1, len(linelist)):
##    line = linelist[count]
##    pieces = line.split(",")
##    if "BICYCLE" in pieces[2]:
##        print(pieces[1])




















