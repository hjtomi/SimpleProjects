# \t is just a tab
# print("\ta") prints out an "a" with a tab in front of it
print("\ta")

# Immutable objects can be changed, but it creates a new memory stuff thus slowing down the code by a bit

# Dictionaries are also called "hash-maps" is other programming languages

# .join(string_array) concatenates values in string_array
# Example:
string_array = ["s", "a", "m", "p", "l", "e"]
# What to put in between values
#      ||
word = "".join(string_array)
print(word)

# Dry = Don't repeat yourself

#  Something is idempotent if: f(f(x)) = f(x)

# String concatenation: "My name is "+name
# String interpolation: "My name is {}".format(name)

# Tkinter objects can only be destroyed after the have been placed, gridded or packed

# for loop first argument in NOT the index of the second argument, it's the type of the second argument
# Example:
# for widget in widgets:
#       widget.destroy()
# "Widget" is a widget variable like a label or a button

# Enumerate
# for i, var in enumerate(vars):
#       pass
# "i" is the index of the vars

# Partition
# test.partition("str")
# takes out "str" from "test" variable and creates a list of them:
# example:
# print("example".partition("m"))
# returns list of "exa", "m", "ple"

# CREATING BUTTON COMMAND IN FOR LOOP     This is the key to it! Expl: it creates a value that is stored in the button
#   for i in range(3)                       |                    and uses that value instead of the value from the loop
#       my_button.configure(command=lambda i=i: my_func(i))
# All buttons will have different lambda functions
