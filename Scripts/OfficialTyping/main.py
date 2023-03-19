# The official typing is made to help myself become a quick typer.
# The app shows a letter on the screen which the user has to press. If the worong button was pressed you get a warning.
# If the right button is pressed a new letter appears.
# This project was made entirely with the official finger placement.

from tkinter import *
from string import ascii_lowercase
import random


def random_letter():
    return random.choice(ascii_lowercase)


def letter_color():
    letter.config(fg='black')


def key_press(event):
    global current_letter
    global letter
    if event.char == current_letter:
        letter.config(fg='black')
        current_letter = random_letter()
        letter.config(text=current_letter)
    else:
        letter.config(fg='red')


window = Tk()
window.title('Official Typing')
window.resizable(width=False, height=False)
window.bind('<KeyPress>', key_press)
current_letter = random_letter()
letter = Label(text=current_letter, font=('bold', 500))
letter.pack()

window.mainloop()
