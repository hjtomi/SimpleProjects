num = 12
word = 'Hello world!'
isit = False
my_list = [num, word, isit]
d = {'int': num, 'str': word, 'bool': isit, 'list': my_list}

# BASIC

# function
def add(x):
    return x + x/2


print(add(num))

# list comprehension
multiple_of_dividables_of_three = [i*2 for i in range(num) if i % 3 == 0]
print(multiple_of_dividables_of_three)

li = range(1, 11)
new_li = [x**x for x in li]
print(new_li)

# Classes
class Teacher:
    def __init__(self, x):
        temp = x.partition(',')
        self.name = temp[0]
        self.age = temp[2]

    def introduce(self):
        return f"Hello my name is teacher {self.name} and I am {self.age} years old."


t1 = Teacher('Brenda,55')
print(t1.introduce())


# File
f = open('teachers.txt', 'w')
f.write('hello sweetie')
f.close()


# INTERMEDIATE

# Lambda
# lambda functions are small throw away functions
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x: x[1])
print(subject_marks)
for i in subject_marks:
    print(i)


phones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
phones.sort(key=lambda x: x['model'], reverse=True)
print(phones)


# filter takes in 2 arguments first is iterator second is iterable
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
odd_nums = list(filter(lambda x : x % 2 == 1, nums))
print(odd_nums)

squared_nums = [x*x for x in nums]
print(squared_nums)
cubed_nums = [x**3 for x in nums]
print(cubed_nums)


# Map
# map takes 2 args, 1st is function, 2nd is a list
# it runs func with arguments in list
nums = range(51)
def func(x):
    return x+x
print(list(map(func,nums)))

