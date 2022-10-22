class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # alternative employee constructor, splits a string by the "-"-s and assigns all the parts to the variables
    # (first, last, pay)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # Tells if the given date is workday or not (workdays are set to saturday and sunday)
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Michael", "Jackson", 60000)

import datetime
my_date = datetime.date(2022, 8, 28)
print(Employee.is_work_day(my_date))

