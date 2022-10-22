# Getters, Setters and Deleters

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    # changes fullname so it is a property instead of a method
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # allows the fullname property to be directly altered, example: emp1.fullname = "John Wick"
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # del emp1.fullname
    @fullname.deleter
    def fullname(self):
        print("Name deleted!")
        self.first = None
        self.last = None


emp1 = Employee("Corey", "Schafer")

emp1.fullname = "John Wick"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
