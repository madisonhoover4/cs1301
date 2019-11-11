# Day 31 - classes that interact with each other
# chapters 13, 16, and 21 cover this week's material

class Student:

    def __init__(self, name, gpa, idnum):
        self.name = name
        self.gpa = gpa
        self.idnum = idnum

    def __eq__(self, other):
        return self.idnum == other.idnum    

    def __str__(self):
        return self.idnum + " is named " + self.name + " with gpa of " + str(self.gpa)


class Teacher:

    def __init__(self, aname, alist):
        self.name = aname
        self.students = alist

    def showfirst(self): # print out the first student
        print(self.students[0])

    def gpaAvg(self):
        total = 0
        for stud in self.students:
            total += stud.gpa
        avg = total / len(self.students)
        return avg

    
        

# outside of any class

# create teacher t1 with name "McDaniel"
t1 = Teacher("McDaniel", [])
# create student s1 with name "Cara" 3.9 "3332222"
s1 = Student("Cara", 3.9, "3332222")
# make Cara first in McDaniel's class

t1.students.append(s1)

t1.showfirst()

# add another student to McDaniel's class

s2 = Student("Madison", 3.8, "2996969")

t1.students.append(s2)

# write a method for the teacher class called gpaAverage that computes the...
# average gpa of all this teacher's students

print(t1.gpaAvg())


studentlist = []
studentlist.append(Student('Peter',2.5,'1111111'))
studentlist.append(Student('Kelly',3.0,'2222222'))

mcdaniel = Teacher("Prof McD", studentlist)

studentlist = []
studentlist.append(Student('George',3.4,'2333233'))
studentlist.append(Student('Ringo', 3.2, '3333224'))

smith = Teacher('Prof Smith',studentlist)

# print out all the students in mcdaniel's class

# write an if statement that determines which of these mcdaniel or smith has...
# the highest avg gpa students


if (mcdaniel.gpaAvg() > smith.gpaAvg()):
    print('McDaniel students are smarter')
elif (smith.gpaAvg() > mcdaniel.gpaAvg()):
    print('McDaniel students need to work harder')
else:
    print('Same')

# print out the gpa of the last student in prof smith's class
print(smith.students[len(smith.students)-1].gpa)

# how to tell if 2 students are the same student

s8 = Student('Joe',3.1,'333')
s9 = Student('Joe',3.8,'444')
s10 = Student('Joe',3.8,'444')

print(s8==s9)
print(s9==s10) # use the __eq__ method to determine equality
# this can also be done with these:
# __lt__ aka less than
# __gt__ aka greaterthan
# __ge__ aka >=
# __le__ aka <= 



    





















