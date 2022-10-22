# Closures

# || In simple terms: A closure is an inner function that remembers and has access to variables in the local scope
# || in which it was created even after the outer function has finished executing

# A closure closes over the free variables from their environment
# In this case "msg" would be that free variable

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func


hi_func = outer_func("hi")
hello_func = outer_func("hello")

hi_func()
hello_func()



# Example

import logging
# Creates a "test.log" file, which is almost like a txt
logging.basicConfig(filename="test.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        # Throws info into the previously created "test.log"
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


# add_logger becomes the "log_func" with "add" as the "func" argument
add_logger = logger(add)
# sub_logger becomes the "log_func" with "sub" as the "func" argument
sub_logger = logger(sub)

# Since "add_logger" is the "log_func" function with "add" as the "func" argument, it calls "log_function" with
# arguments of "3, 3"
# (Does it two times with different numbers)
add_logger(3, 3)
add_logger(4, 5)

# Since "sub_logger" is the "log_func" function with "sub" as the "func" argument, it calls "log_function" with
# arguments of "10, 5"
# (Does it two times with different numbers)
sub_logger(10, 5)
sub_logger(20, 10)