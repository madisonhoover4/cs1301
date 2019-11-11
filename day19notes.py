# Day 19 - Dictionaries

# dictionaries are a new data type, key to value pairs

# the key must be unique, immutable, but the values don't have to be

# "123456" might lead to price $9.99 and "55555" leads to $9.99

# "903209318" is a list of ["Madison Hoover", 18, "IE"]

# to create a dictionary:
mydict = {}
mydict["joe"] = 19 # (whatever you want for key in the bracket, then = value)

for item in ["joe", "tom", "sarah"]:
    mydict[item] = 0 # this will go thru list and add each to dictionary
    # if joe already exists, it will replace joe with new value
    print(len(mydict))
    
# dictionaries are not kept stored in sequential order

prodCodes = {}
prodCodes['111'] = 99.99
prodCodes['223'] = 88.99
prodCodes['123'] = 99.99
prodCodes['111'] = 79.99 # the length is only 3 because 111 is reassigned
print(len(prodCodes))

codeslist = ['12','34','56']
costlist = [99.99,88.99,100.00]

# create a dict from the codeslist and costlist above
codedict = {}

for count in range(len(codeslist)):
    codedict[codeslist[count]] = costlist[count]

print(codedict)

# try this... create a dictionary called letterdict that keeps track of how...
# many times each letter has been used in a string of text

# step 1 - initialize all letters in the dictionary to 0

letterdict = {}
sentence = 'everybody wishes they could get into tech'
sentence = sentence.lower()

for letter in sentence:
    letterdict[letter] = 0

print(letterdict)

for letter in sentence:
    if letter in letterdict.keys():
        letterdict[letter] += 1

print(letterdict)

del letterdict['e'] # this is how you delete something
print(letterdict)


# print how many letters in the sentence occur more than 2 times

count = 0
for item in letterdict.values():
    if item > 2:
        count += 1

print(count) # you cannot go backwards by looking up values, only keys


# create a dict of names and ages of your 3 closest friends

# then write a for loop that will make all of them one year older

agedict = {"Rachel":18,"Leigh":19,"Carson":19}
for name in agedict.keys():
    agedict[name]+=1

print(agedict)
















