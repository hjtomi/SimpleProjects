# SAVE SYSTEM
# LANGUAGE HISTORY
# REWORK THE INPUT SYSTEM (when and how to write out the commands, start?!)

# create a new language (each letter, number and symbol corresponds to a random one, no repeats)
# save languages, make them accessible
# code and decode arguments from chosen language to chosen language
# git is cool


import random
import string


class Language:

    # Class variables
    all_letters = list(string.ascii_letters + string.digits + string.punctuation + " ")

    languages = list()
    language_dict = dict()

    def __init__(self, name):
        self.name = name

        key_list = list(Language.all_letters)
        value_list = list(Language.all_letters)
        random.shuffle(key_list)
        random.shuffle(value_list)

        self.code = {key: value for key, value in zip(key_list, value_list)}

        self.decode = {value: key for key, value in zip(key_list, value_list)}

    # Code a text object's content into the language
    def code_text_object(self, text, textindex):
        # Work
        # Put all the letters in the text.content to a list
        list_text = list(text.content)
        # For every letter in the list
        for i in range(len(list_text)):
            # Change that letter to the corresponding one from the language
            list_text[i] = self.code[list_text[i]]
        # Assignments
        # Change the content of the text
        text.content = ''.join(list_text)
        # Change the text in the dictionary
        Text.text_dict[textindex] = ''.join(list_text)
        # Change the language attribute to the language it has been coded into
        text.language = self.name
        return text.content

    # Decode a text object's content
    def decode_text_object(self, text, textindex):
        list_text = list(text.content)
        for i in range(len(list_text)):
            list_text[i] = self.decode[list_text[i]]
        text.content = ''.join(list_text)
        Text.text_dict[textindex] = ''.join(list_text)
        text.language = "Default"
        return text.content

    def showcase(self):
        print("Name: ", self.name)
        print("Code: ", self.code)
        print("Decode: ", self.decode)

    def code_text(self, text):
        list_text = list(text)
        for i in range(len(list_text)):
            list_text[i] = self.code[list_text[i]]
        return ''.join(list_text)

    def decode_text(self, text):
        list_text = list(text)
        for i in range(len(list_text)):
            list_text[i] = self.decode[list_text[i]]
        return ''.join(list_text)

    def abc(self):
        for l in Language.all_letters:
            print(l, self.code_text(l))

    def hello_world(self):
        hello_world = list("Hello world!")
        for i in range(len(hello_world)):
            hello_world[i] = self.code_text(hello_world[i])
        print(''.join(hello_world))

    @classmethod
    def quick_code(cls, text):
        # create a lang
        key_list = list(cls.all_letters)
        value_list = list(cls.all_letters)
        random.shuffle(key_list)
        random.shuffle(value_list)

        code = {key: value for key, value in zip(key_list, value_list)}

        # logic
        list_text = list(text)
        for i in range(len(list_text)):
            list_text[i] = code[list_text[i]]
        return ''.join(list_text)


class Text:

    # Class variables
    texts = list()
    text_dict = dict()

    def __init__(self, content):
        self.content = content
        self.language = "Default"

    def showcase(self):
        print("Content: ", self.content)
        print("Language: ", self.language)

def main():
    keywords = {
        "nl": "Generate new language (new language)",
        "nt": "Create a given english text (new text)",
        "c": "Code a given text from the text list into chosen language (code)",
        "dc": "Decode a given text from the text list from chosen language (decode)",
        "s": "Showcase a chosen language or text (showcase)",
        "a": "Showcase both languages and texts (all)",
        "f": "Find given letter in a given language (find)",
        "abc": "Showcase the abc",
        "hw": "Print Hello world! in the chosen language (hello world)",
        "cs": "Code a text into a chosen language (code suddenly)",
        "dcs": "Decode a text into a chosen language (decode suddenly)"}

    inp = ""
    while not inp == "exit":
        print("\n", keywords)
        inp = input("Start: ")

        if inp == "nl":
            name = input("Language name: ")
            Language.languages.append(Language(name))
            Language.language_dict[len(Language.languages)-1] = name

        if inp == "nt":
            cont = input("Text: ")
            Text.texts.append(Text(cont))
            Text.text_dict[len(Text.texts)-1] = cont

        if inp == "c":
            print(Language.language_dict)
            print(Text.text_dict)

            try:
                lindex = int(input("Desired language index: "))
                tindex = int(input("Desired text index: "))
                print(Language.code_text_object(Language.languages[lindex], Text.texts[tindex], tindex))

            except IndexError and ValueError:
                print("Invalid!")

        if inp == "dc":
            print(Language.language_dict)
            print(Text.text_dict)

            try:
                lindex = int(input("Desired language index: "))
                tindex = int(input("Desired text index: "))
                print(Language.decode_text_object(Language.languages[lindex], Text.texts[tindex], tindex))

            except IndexError and ValueError:
                print("Invalid!")

        if inp == "s":
            temp = input("Language or Text(L/T)? ")

            if temp == "L":
                print(Language.language_dict)
                index = int(input("Desired language index: "))
                Language.languages[index].showcase()

            elif temp == "T":
                print(Text.text_dict)
                index = int(input("Desired text index: "))
                Text.texts[index].showcase()

        if inp == "a":
            print("Languages: ", Language.language_dict)
            print("Texts", Text.text_dict)

        if inp == "f":
            print(Language.language_dict)
            lindex = int(input("Desired language index: "))
            letter = input("Desired letter: ")

            print(Language.languages[lindex].code[letter])

        if inp == "abc":
            print(Language.language_dict)
            lindex = int(input("Desired language index: "))

            Language.languages[lindex].abc()

        if inp == "hw":
            print(Language.language_dict)
            lindex = int(input("Desired language index: "))

            Language.languages[lindex].hello_world()

        if inp == "cs":
            print(Language.language_dict)
            lindex = int(input("Desired language index: "))
            text = input("Text to code: ")

            print(Language.languages[lindex].code_text(text))

        if inp == "dcs":
            print(Language.language_dict)
            lindex = int(input("Desired language index: "))
            text = input("Text to decode: ")

            print(Language.languages[lindex].decode_text(text))


if __name__ == "__main__":
    main()
