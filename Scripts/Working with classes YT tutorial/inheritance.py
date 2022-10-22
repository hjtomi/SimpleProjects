from classmethods_and_staticmethods import Employee

# Which class to inherit from
#                  |
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())

dev1 = Developer("Tom", "Cruise", 9, "C#")
mgr1 = Manager("Pam", "Spam", 8765)

mgr1.add_emp(dev1)

print(dev1.prog_lang)
mgr1.print_employees()
