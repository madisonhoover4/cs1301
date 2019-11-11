# Recitation 5

# only thing not in textbook that is on test is binary and hex

inventory = {"apples":430, "bananas":312, "pears":217}
del inventory["pears"]
# prints {"apples":430, "bananas":312}

# .keys(), .values() returns a list of the dictionaries keys, values
# .items() returns a list of dict's (key,value) tuple pairs

a = {"a":2,"b":1,"c":3}

for key in a.keys():
    a[key] = key*a[key]

    

alist = [1,2,3,4,5]
aDictionary = {}
num = 10
aDictionary["list"] = alist
aDictionary["number"] = num
aDictionary["bool"] = True
print(aDictionary)
alist[2] = "GT"
num = 11
del aDictionary["bool"]
print(aDictionary)

hours = {}
hours["c"] = 120
hours["C"] = 90
hours["B"] = 4
hours["J"] = 70
for x in hours:
    hours[x] += 30
for x in hours:
    print(hours[x])

def over21(alist):
    adict = {}
    for tup in alist:
        if tup[1] >= 21:
            adict[tup[0]] = tup[1]
    return adict
























