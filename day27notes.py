# Day 27 Notes

alist = [1,3,2,3] #alist is a list of the list ckass

myname = 'Madison' # myname is an instance of the string class

# both alist and myname are objects

# list and string are predefined classes that contain attributes and methods

# list and string are different than primitive data types like int float boolean

print(alist.sort()) # sort is amethod of the list class (but it is also func)
# a method is a function called using the . operator

print(myname.lower()) # lower is a method of the string class

# if you tried to do the lower of a num, only strings have lower method

t1 = turtle.Turtle() # creates a new instance of the turtle class
    # by calling the init function

    
t1.forward() # forward is a method of the turtle class
print(t1.pencolor()) # pencolor is an attribute of the turtle class


# to create your own class you need to write an init function

class Point:    # create a new class

    def __init__(self,xx,yy, zz):
        print("We are creating a new point")
        self.x = xx
        self.y = yy # x and y are attributes of the point class
        self.z = zz

    def is_origin(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    def increment(self):
        self.x += 1
        self.y += 1
        self.z += 1

    def show(self):
        print("a point at position(" + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')')
    
        
    
p1 = Point(50,50)
p2 = Point(0,0)

print(p1.is_origin())
print(p2.is_origin())

# try this... add a method called increment to the Point class that adds...
# one to both the x and y coordinates
# call the increment method on point p2

# you cant use self ouside of your class - it is undefined outside of the class
# try this.. add an attribute to your point class that stores a z coordinate
# change everything to include the z 


print(p2.increment())
p2.show()


















    

    
