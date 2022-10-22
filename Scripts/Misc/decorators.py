# Decorators
# || A decorator is just a function that takes another function as an argument, adds some kind of functionality
# || and then returns another function - all of this without altering the source code of the original function that you
# || passed in
import time

def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func


hi_func = outer_func("hi")
bye_func = outer_func("bye\n")

hi_func()
bye_func()

# What if instead of printing a message that we passed in, we instead execute a function that we passed in -
# and that's where the decorator goes
# Instead of a message we are going to accept a function as an argument
# Let's alter the code

# THIS is a decorator
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("Display function ran\n")


decorated_display = decorator_function(display)

decorated_display()

# Why would we want to do this?
# Answer: Decorating our functions allows us to easily add functionality to our existing function
# by adding that functionality inside our wrapper
# Example:

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print("Display function ran\n")


decorated_display = decorator_function(display)

decorated_display()

# Where is the "@" ?
# Answer: "@decorator_function" at the top of the function is the same as "display = decorator_function(display)" below
# the function
# So both codes are the same; but the following code is easier to read

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print("Display function ran\n")

display()

# In order to have arguments in your decorated functions, you should include "*args, **kwargs" in your wrapper function
# as shown below
# args stand for arguments, kwargs stands for key word arguments
# * means all, so it accepts all args and kwargs

def decorator_function(original_function):
    #                      !        !
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        #                          !        !
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("Display function ran")

display()

@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})\n".format(name, age))

display_info("John", 25)

# Another option is using classes instead of functions as decorators

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    # *args and **kwargs are still important because "display_info has arguments"
    #                    !        !
    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(self.original_function.__name__))
        #                               !        !
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print("Display function ran")

display()

@decorator_class
def display_info(name, age):
    print("display_info ran with arguments ({}, {})\n".format(name, age))

display_info("John", 25)

# Practical examples of decorators
# Common use case of decorators is logging
# The code below logs what args and kwargs were given in the execution of a function

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name, age):
    print("display_info ran with arguments ({}, {})\n".format(name, age))

display_info("John", 25)
# Now we can easily reuse this decorator any time we want to add that logging functionality to any function

# Another easy practical example that people sometimes use decorators for is for timing how long functions run

import time
def my_timer(orig_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} sec\n".format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
def display_info(name, age):
    # makes it wait for given second so that this function runs for given second
    time.sleep(0)
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info("Hank", 30)

# What if I wanted to apply both of the decorators above to one function?
# You can just stack the decorators on top of each other but be careful! In order to not get an error you have to
# import "wraps" from "functools" and put "@wraps()" above the wrapper function, also your have to
# put the decorator function's name into the "@wraps()" as the argument for it to work properly
# as shown below

#           !
from functools import wraps

def my_logger1(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    #     !
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer2(orig_func):
    import time

    #     !
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} sec\n".format(orig_func.__name__, t2))
        return result

    return wrapper

#    !
@my_logger1
@my_timer2
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info("Benjamin", 68)
