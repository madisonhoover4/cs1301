# day 23 - Try and Except

# an exception is another name for a runtime error
# you can handle these errors in your code

# before try... except review break and continue

for num in range(50):
    if num % 7 == 0:
        continue     # go back to start of loop
    if num % 25 == 0:
        break        # exits loop
    print(num)

print("Done!")

# try except uses break and continue to handle the possibilty of exceptions...
# occurring

age = 0
while age < 18:
    try:
        age = input('enter your age')
        age = int(age)
        if age < 18:
            print("no admittance")
    except:
        print("Your answer must be a positive integer")
        age = 0
print("welcome")


# very useful with files in case they are not there

try:
    myfile = open("gradesss.csv","r")
    data = myfile.read()
    print(data)
    myfile.close()

except:
    print("unable to find file")
    
# nonexistent items in a dictionary

mydict = {1:45,2:99}
try:
    print(mydict[8])
except:
    print("key not found in dictionary")


# finally is a way to end the try...except block and wrap things up
# finally code is executed whether the try or except block happened


myfile = open("grades.csv")
try:
    print(3/0)
except:
    print("exception occurred")

finally:
    myfile.close()

    

import random

total = 0
rand = random.Random()
for num in random.randrange(1,100):
    try:
        if num % 10 == 7:
            continue
        if num in [70,71,72,73,74,75,76,78,79]:
            break
        total += num
    except:
        total = 0
print(total)



























