# Recitation 8 notes

# to create a class point, you initialize it and pass in an x and y
# to create an object you initialize it using init and with the right num of...
# arguments

# to access attributes you do the dot operator, ex. p.x
# to change an attribute you can just say p.x = something



class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancefromorigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    

p = Point(1,1)
print(p.x)
print(p.y)
# type(p) is Point

# if you did p.z it will throw an error

r = Point() # this would be an error if the 2nd and 3rd parameter were just x,y
# but since x=0 and y=0 it will default to (0,0)

s = Point(1) # makes (1,0)
s.y = 5 # makes it (1,5)


print(p.distancefromorigin()) # self is the instance of the Point that the...
# distance from origin method is being called on


class BankAccount:
    def __init__(self, owner, bankId, bankName, balance):
        self.owner = owner
        self.bankId = bankId
        self.bankName = bankName
        self.balance = balance

    # a method is just a function inside a class
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def printAccountInfo(self):
        print(self.owner)
        print(self.bankId)
        print(self.bankName)
        print(self.balance)

    def transfer(self, amount, other):
        if self.balance >= amount:
            other.balance += amount
            self.balance -= amount
        else:
            print("Insufficient funds")


aBank = BankAccount("lucas", 0000, "boA", 50)
aBank.deposit(10)
aBank.withdraw(20)
aBank.withdraw(1000)
bBank = BankAccount("David", 1111, "BoA", 100)
aBank.transfer(bBank, 30)












