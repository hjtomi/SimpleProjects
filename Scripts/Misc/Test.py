## First-class functions

# Pass function as argument

def test1():
    def square(x):
        return x * x


    def cube(x):
        return x * x * x


    def func_runner(func, arg):
        return func(arg)


    print(func_runner(square, 5))

# Return functions as the result of other function
def test2():
    def logger(msg):
        def log_msg():
            print(msg)
        return log_msg

    lm = logger("sup")
    lm()

## Memoization

# Memoization is used for functions that take a long time to run.
# In simple terms: Remember the answer for an argument and return it immediately
# Example:
def Memoization():
    import time

    dict = {}

    def square(x):
        if x in dict:
            return dict[x]
        time.sleep(1)
        result = x*x
        dict[x] = result
        return result

    print(square(2))
    # second "square(2)" doesn't take for 1 second to run because it remembered the answer for it in "dict"
    print(square(2))

## Combinations and Permutations

def combinations_and_permutations():
    import itertools

    my_letters = [1, 2, 3]

    # Returns all 2 digit combinations of "my_letters" numbers
    combs = itertools.combinations(my_letters, 2)
    for i in combs:
        print(i)

    print("\n")

    # Returns all 2 digit permutations of "my_letters" numbers
    perms = itertools.permutations(my_letters, 2)
    for i in perms:
        print(i)

    print("\n")

    word = "sample"
    my_letters1 = "plmeas"

    combs1 = itertools.combinations(my_letters1, 6)
    perms2 = itertools.permutations(my_letters1, 6)

    for p in perms2:
        if "".join(p) == word:
            print("success")
            break
    else:
        print("bruh")


