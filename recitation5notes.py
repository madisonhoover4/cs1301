# Recitation 5

alist = [1,2,3]

# if you want to clone alist...

blist = alist[:] # this indexes the entire list

alist.append(7)
print(alist)

# alias is a nickname for a list, 2 name references for same thing

clist = alist
clist.append(54) # appends to both clist and alist


# IMPORTANT
# changing a nested in list in a clone changes both the clone and the original


mylist = ["hey",True,[1,2,3]]
yourlist = mylist[:] # that's a clone
yourlist[2][1] = 11 # this changes mylist
yourlist[2] = False # this does not change mylist
print(mylist)


# Opening Files

# you can open files for reading "r" (the default), writing "w", appending "a"

# when you open the file for writing, it deletes all text, so to add use append

# how to get info from a file:
    # read - string with the whole file
    # readline - the first line in the file as a string, keep track of which line ur on
    # readlines - list with every line in file as an element

# with readline, once it reads a line, moves to the next one for reading

# if you print your second call of readline(), it will print with a line break too




















