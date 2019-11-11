# Last Day Notes

# aliases v. clones

num = 22 # this is not an object, just an integer (called a primitive)
mylist = [1,2,3,4] # this is an object

num2 = num # makes a copy and stores it in num2

mylist2 = mylist # makes an alias (a pointer to the same area of memory)

mylist2[1] = 99
num2 = 44

print(num) # num is still 22
print(mylist) # this is changed when you change mylist2

# try this... create a dictionary from a list of words and numbers w word...
# as a key and num as a value

fr = open('words.txt','r')
stuff = fr.read()
mylist = stuff.split('\n')
fr.close()


mylist = ['joe',22,'fred',25,'martha',33,'tom',18]

mydict = {}
for num in range(len(mylist)-1):
    if num%2 == 0:
        mydict[mylist[num]] = mylist[num + 1]

print(mydict)






