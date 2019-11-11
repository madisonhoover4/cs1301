alist = ['cat','bird','dog','house','tree']
for (num,val) in enumerate(alist):
    if (val=='dog'):
        print(num)
    if (num==1):
        print(val)

# if you try to print enumerate(alist) it will just give you <enumerate object>


def mysteryb(aList, num):
    aboolean = False
    i = 0
    while (not aboolean):
        if aList[i] == num:
            aboolean = True
        print(aList[i], aboolean)
        i = i + 1
    
        
bList = [67, 29, 29, 52, 87, 32, 97, 59, 61, 37]
print(mysteryb(bList, 87))


# prints...
'''
67 False
29 False
29 False
52 False
87 True
None
'''
# Since you are printing a func w no return, you return None!

def character_count(string):
    adict = {}
    
    for key in adict:
        for letter in string:
            if letter != key:
                adict[letter] = 1
            else:
                adict[letter] += 1
    return adict































