# functions with 2 underscores at the beginning and the end are called "Dunder" functions
# Example: __init__ is called "dunder init"

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee({}, {}, {}".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # Changes the default "len()" function to the method below for Employee instances
    # All the changeable functions: https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Corey", "Schafer", 50000)

print(repr(emp1))
print(str(emp1))
print(len(emp1))

