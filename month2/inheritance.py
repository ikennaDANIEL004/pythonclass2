class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printFullname(self):
        print(self.fname + "" + self.lname)




me = person("majesty","chibuike")
me.printFullname()

class Student(person):
    def printLastName(self): 
        print(self.lname)

sanctus = Student("","cisco")
sanctus.printFullname()
sanctus.lname
sanctus.printLastName

        
mytuple = ("apple", "ytuhb",)
mytuple2 = {"apple", "ytuhb",}
print(type(mytuple))
print(type(mytuple2))


h



