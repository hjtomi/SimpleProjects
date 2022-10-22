

# first class functions
# Higher order function: If a function accepts other functions as arguments or returns functions as their result
# treat functions as any other variable/object



# Python program to demonstrate working of map
# Return double of n
def square(x):
    return x * x
# We double all numbers using map()
numbers = (1, 2, 3, 4, 5)
result = map(square, numbers)
print(list(result))




# pass functions as arguments

def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# what is called the "argument"?
# argument is the "square" function here
#                    |
#                   /
#                  |
squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

def cube(x):
    return x * x * x




# return a function from another function
# return functions as the result of other function
# (the point is the same...)

def logger(msg):
    def log_message():
        print("Log:",msg)

    return log_message

log_hi = logger("Hi")
log_hi()

# Practical use-case

def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text

print_h1 = html_tag("h1")
print_h1("Test headline!")
print_h1("Another Headline!")

print_p = html_tag("p")
print_p("Test paragraph!")


# Just a test by me, works the same as above

def test(tag, msg):
    return("<{0}>{1}</{0}>".format(tag, msg))

print(test("h1", "Test headline!"))
