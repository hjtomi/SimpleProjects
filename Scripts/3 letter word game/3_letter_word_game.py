import random

words = [
    'cat', 'bat', 'via', 'new', 'app', 'mow', 'map', 'cap', 'bra', 'ass', 'sex'
    ]
query = random.choice(words)
print('___')

word = str()
while word != "exit":
    word = input()
    if word == query:
        print("You correctly guesses the word\n", word.upper())
        break
    num = 0
    for i in range(len(query)):
        if word[i] in query:
            num += 1

    print(word, num)
