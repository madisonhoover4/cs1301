# Day 21 - more dictionary practice

# know when to use a string, list, tuple, or a dictionary

# be able to trace dictionary code

d = {"apples":15,"bananas":35,"grapes":12}

print(d["bananas"]+len(d.keys()))

# dictionaries are a good way to store sparce matrices

# if stored in a list of lists, most entires are 0 aka waste of space

values = {('A',2):15,('D',5):25,('C',2):42,("G",7):9}
print(values[('A',2)])

if ('A',2) in values.keys():
    print(values[('A',2)])
else:
    print(0)


# creating a dictionary from a file
f = open('gtsong.txt','r')
data = f.read()
f.close()



# create a dictionary of the letters from "gtsong.txt" and their occurrence

mydict = {}
for letter in data:
    letter = letter.lower()
    if letter in mydict.keys():
        mydict[letter] +=1 # add one to dictionary entry
    else:
        mydict[letter] = 1 # adds this letter to the dictionary

print(mydict)

# which letters in gt fight song occur ten or more times? don't count punctuation

count = 0
mylist = []
for key in mydict:
    if key in "abcdefghijklmnopqrstuvwxyz":
        if mydict[key] >= 10:
            count += 1
            mylist.append(key)

print(count)
print(mylist)


f2 = open('aliceinwonderland.txt','r')
data = f2.read()
wordlist = data.split()
f2.close()

mydict2 = {}
for word in wordlist:
    word = word.lower()
    if word in mydict2.keys():
        mydict2[word] += 1
    else:
        mydict2[word] = 1

highest_so_far = 0

for value in mydict2.values():
    if value > highest_so_far:
        highest_so_far = value


        

























