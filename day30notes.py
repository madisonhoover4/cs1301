# Day 30 - more practice with classes and objects
# special method __str__

class Pet:

    def __init__(self, aname, akind): # whatever your going to intialize goes after self
        self.name = aname
        self.kind = akind

    def speak(self):
        if self.kind == "dog":
            print("woof woof")
        else:
            print("meow")

    def areFriends(self, other):
        if self.kind == other.kind:
            return True
        else:
            return False

    def __str__(self):
        return "A " + self.kind + " named " + self.name




# outside of the class

beauty = Pet("Beauty","cat")
beauty.speak()
print(beauty.name)
print(beauty.kind)


# try this... create a dog named Smutty and make him speak

smutty = Pet("Smutty","dog")
smutty.speak()

print(beauty.areFriends(smutty)) # you don't need self again

if not beauty.areFriends(smutty):
    for num in range(3):
        beauty.speak()
        smutty.speak()

# create a bird class that contains 2 attributes, type and its bird call
# the bird is able to talk (write a talk method that prints its call 3 times)

class Bird:

    def __init__(self, atype, acall, migrate):
        self.type = atype
        self.call = acall
        self.migrate = migrate

    def talk(self):
        print(self.call)
        print(self.call)
        print(self.call)

    def __str__(self): # this method returns a str of info about this object
        # this method if present tells pythin what to print in the print ...
        # statement for this class
        return "A" + self.type + " that says " + self.call  # return not print!



# outside of the class
bird1 = Bird('owl','hoot', False)
bird2 = Bird('crow','caw', False)
bird3 = Bird('robin','tweet', True)
bird4 = Bird('swallow','chirp', True)

bird2.talk()


# add a new attribute to the Bird class migrates (a boolean) and set that...
# attribute for all your birds













