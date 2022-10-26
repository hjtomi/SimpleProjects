# random replies to questions
# ask questions back
# words
# basic english grammar
# read input

# store input as data but continue the conversation

import random

words = {
    'greeting': ['hi', 'hello'], 
    'perspron': ['i', 'you', ['he', 'she', 'it'], 'we', 'you', 'they'], 
    '.?!': ['.', '?', '!'], 
    'qwords': ['what', 'why', 'how'], 
    'infowords': ['name', 'age', 'color']
    }

bot_info = {'name': '',}
user_info = {'name': None, 'age': None}

# function to create sentences
# types: greeting, question
def sentence_generator(type):
    sentence = ''
    if type == 'greeting':
        if user_info['name'] == None:
            sentence = "{}".format(words['greeting'][random.randint(0, len(words['greeting'])-1)])
        if user_info['name'] != None:
            sentence = "{} {}".format(words['greeting'][random.randint(0, len(words['greeting']))], user_info['name'])
    if type == 'askname':
        sentence = 'What is your name?'
    
    return sentence

'''
greet = bool(random.getrandbits(1))
ask_name = bool(random.getrandbits(1))
if greet:
    print(sentence_generator('greeting'))

    if ask_name:
        print(sentence_generator('askname'))
'''

    
    
message = ''
greeted = False
while message != 'quit':
    # new message
    newm = False
    # did the user prompt a question
    user_asked = False

    if not greeted:
        print(sentence_generator('greeting'))
        greeted = True
    if user_info['name'] == None:
        print(sentence_generator('askname'))
        message = input()
        user_info['name'] = message
        newm = True
        
        
    if not newm:
        message = input()
        
        
        

