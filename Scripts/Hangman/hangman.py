# _ for each unguessed letter
#

import random


def diw():
    return ''.join(display_word)


# the amount of guesses the user has
guesses = 10
# list of words to chose from randomly
words = ['apple', 'banana', 'pig', "shake", "espresso"]
# randomly choses a word from the list
query = random.choice(words)
# create a list of underscores for each letter in the chosen word
display_word = ["_"] * len(query)
print(diw())


# create list that will store all the letters the user has guessed
guessed_letters = list()
# the program runs until the word is guessed
while ''.join(display_word) != query:
    if guesses <= 0:
        print("no guesses left")
        break
    else:
        print(guesses, "guesses left")
    letter = input()
    # if the letter haven't been guessed already
    if letter not in guessed_letters:
        # adds the letter to the guessed_letters list
        guessed_letters.append(letter)
        # IMPORTANT PART ==> list of indexes of inputted letter in query (query=banana, guess=n, indicies=[2,4])
        indicies = [i for i, x in enumerate(query) if x == letter]
        for index in indicies:
            # replace the indexed underscore to the letter inputted by the user
            display_word[index] = letter
        # decrement the remaining guesses
        guesses -= 1
    else:
        print("letter already guessed")
    # the list of underscored is printed to let the user know which letter they guessed correctly
    print(diw())
