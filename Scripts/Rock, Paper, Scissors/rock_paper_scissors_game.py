# Counts score and probability if the player has a win, lose or draw streak
# Remember the biggest win, lose and draw streak

# UI is set up, time for making the duel and data!

import tkinter as tk
import random


def spawn_image():
    cnvs.create_image(18, 18)


def crt_label(win, text, font_size):
    return tk.Label(win, text=text, background=bg_col, foreground=font_col, font=font_size)


def crt_button(win, text, font_size, command):
    return tk.Button(window, text=text, font=font_size, command=command)


def duel(tool):
    tool_lbl.config(text=tool)
    bot_tool = random.choice(tools)
    bot_tool_lbl.config(text=bot_tool)
    if tool == bot_tool:
        curr_wins += 1
    elif tool == tools[0] and bot_tool == tools[1]:
        result("Lose")
    elif tool == tools[0] and bot_tool == tools[2]:
        result("Win")
    elif tool == tools[1] and bot_tool == tools[2]:
        result("Lose")
    elif tool == tools[1] and bot_tool == tools[0]:
        result("Win")
    elif tool == tools[2] and bot_tool == tools[0]:
        result("Lose")
    elif tool == tools[2] and bot_tool == tools[1]:
        result("Win")


def rock():
    curr_tool = tools[0]
    duel(curr_tool)


def paper():
    curr_tool = tools[1]
    duel(curr_tool)


def scissors():
    curr_tool = tools[2]
    duel(curr_tool)


def load_data():
    # Load data into variables
    pass

def main_scrn():
    pvb = crt_label(window, "Player vs Bot", 50)
    pvb.grid(column=0, row=0, columnspan=3)

    p_scr_lbl.grid(column=0, row=1)

    b_scr_lbl.grid(column=2, row=1)

    bot_lbl = crt_label(window, "BOT", 50)
    bot_lbl.grid(column=0, row=2, columnspan=3)

    bot_tool_lbl.grid(column=0, row=3, columnspan=3)

    tool_lbl.grid(column=0, row=4, columnspan=3)

    player_lbl = crt_label(window, "PLAYER", 50)
    player_lbl.grid(column=0, row=5, columnspan=3)

    rock_button = crt_button(window, "ROCK", 50, command=rock)
    rock_button.grid(column=0, row=6, columnspan=1)

    paper_button = crt_button(window, "PAPER", 50, command=paper)
    paper_button.grid(column=1, row=6, columnspan=1)

    scissors_button = crt_button(window, "SCISSORS", 50, command=scissors)
    scissors_button.grid(column=2, row=6, columnspan=1)


data_file_path = "D:\Scripts\Python\SimpleProjects\Scripts\Rock, Paper, Scissors\data.txt"
images_path = "D:\Scripts\Python\SimpleProjects\Scripts\Rock, Paper, Scissors\Images\\"



# Current
curr_wins = 0
bot_curr_wins = 0


# Data
games_played = 0

wins = 0
losses = 0
draws = 0

win_streak = 0
lose_streak = 0
draw_streak = 0

highest_win_streak = 0
highest_lose_streak = 0
highest_draw_streak = 0

rocks_played = 0
papers_played = 0
scissors_played = 0

rock_wins = 0
rock_losses = 0
rock_draws = 0

paper_wins = 0
paper_losses = 0
paper_draws = 0

scissors_wins = 0
scissors_losses = 0
scissors_draws = 0

bot_rocks_played = 0
bot_papers_played = 0
bot_scissors_played = 0

bot_rock_wins = 0
bot_rock_losses = 0
bot_rock_draws = 0

bot_paper_wins = 0
bot_paper_losses = 0
bot_paper_draws = 0

bot_scissors_wins = 0
bot_scissors_losses = 0
bot_scissors_draws = 0

seconds_spent_in_app = 0


curr_wgts = []
tools = ["Rock", "Paper", "Scissors"]


bg_col = "black"
font_col = "white"

window = tk.Tk()
window.config(background=bg_col)
window.geometry("800x600")
window.resizable(width=False, height=False)

cnvs = tk.Canvas(window, background=bg_col, width=32, height=32, highlightthickness=0)
cnvs.place(anchor="center", relx=.5, rely=.5)

rock_image = tk.PhotoImage(file=images_path+"rock.png")
paper_image = tk.PhotoImage(file=images_path+"paper.png")
scissors_image = tk.PhotoImage(file=images_path+"scissors.png")

load_data()

p_scr_lbl = crt_label(window, curr_wins, 50)
b_scr_lbl = crt_label(window, bot_curr_wins, 50)

bot_tool_lbl = crt_label(window, "", 50)
tool_lbl = crt_label(window, "", 50)

main_scrn()

window.mainloop()
