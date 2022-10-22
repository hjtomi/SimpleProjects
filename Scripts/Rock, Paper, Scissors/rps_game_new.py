import tkinter as tk
import time
import random

class RPS():

    # Current
    curr_wins = 0
    bot_curr_wins = 0

    # Data
    data_dict = {"games_played": 0,
                 "wins": 0, "losses": 0, "draws": 0,
                 "win_streak": 0, "lose_streak": 0, "draw_streak": 0,
                 "highest_win_streak": 0, "highest_lose_streak": 0, "highest_draw_streak": 0,
                 "rocks_played": 0, "papers_played": 0, "scissors_played": 0,
                 "rock_wins": 0, "rock_losses": 0, "rock_draws": 0,
                 "paper_wins": 0, "paper_losses": 0, "paper_draws": 0,
                 "scissors_wins": 0, "scissors_losses": 0, "scissors_draws": 0,
                 "bot_rocks_played": 0, "bot_papers_played": 0, "bot_scissors_played": 0,
                 "bot_rock_wins": 0, "bot_rock_losses": 0, "bot_rock_draws": 0,
                 "bot_paper_wins": 0, "bot_paper_losses": 0, "bot_paper_draws": 0,
                 "bot_scissors_wins": 0, "bot_scissors_losses": 0, "bot_scissors_draws": 0,
                 "seconds_spent_in_app": 0}

    # 0
    # games_played

    # 1
    # wins = 0
    # losses = 0
    # draws = 0

    # 4
    # win_streak = 0
    # lose_streak = 0
    # draw_streak = 0

    # 7
    # highest_win_streak = 0
    # highest_lose_streak = 0
    # highest_draw_streak = 0

    # 10
    # rocks_played = 0
    # papers_played = 0
    # scissors_played = 0

    # 13
    # rock_wins = 0
    # rock_losses = 0
    # rock_draws = 0

    # 16
    # paper_wins = 0
    # paper_losses = 0
    # paper_draws = 0

    # 19
    # scissors_wins = 0
    # scissors_losses = 0
    # scissors_draws = 0

    # 22
    # bot_rocks_played = 0
    # bot_papers_played = 0
    # bot_scissors_played = 0

    # 25
    # bot_rock_wins = 0
    # bot_rock_losses = 0
    # bot_rock_draws = 0

    # 28
    # bot_paper_wins = 0
    # bot_paper_losses = 0
    # bot_paper_draws = 0

    # 31
    # bot_scissors_wins = 0
    # bot_scissors_losses = 0
    # bot_scissors_draws = 0

    # 34
    # seconds_spent_in_app = 0

    @staticmethod
    def crt_label(win, text, font_size):
        return tk.Label(win, text=text, background=bg_col, foreground=font_col, font=font_size)

    @staticmethod
    def crt_button(win, text, font_size, command):
        return tk.Button(window, text=text, font=font_size, command=command)

    @staticmethod
    def duel(tool):
        bot_tool = random.choice(tools)

        tool_lbl.config(text=tool)
        bot_tool_lbl.config(text=bot_tool)
        if bot_tool == "rock":
            RPS.data_dict["bot_rocks_played"] += 1
            RPS.update_text(data_lbls[22], "bot_rocks_played: " + str(RPS.data_dict["bot_rocks_played"]))
        elif bot_tool == "paper":
            RPS.data_dict["bot_papers_played"] += 1
            RPS.update_text(data_lbls[23], "bot_papers_played: " + str(RPS.data_dict["bot_papers_played"]))
        elif bot_tool == "scissors":
            RPS.data_dict["bot_scissors_played"] += 1
            RPS.update_text(data_lbls[24], "bot_scissors_played: " + str(RPS.data_dict["bot_scissors_played"]))

        if tool == "rock":
            RPS.data_dict["rocks_played"] += 1

            RPS.update_text(data_lbls[10], "rocks_played: "+str(RPS.data_dict["rocks_played"]))
            if bot_tool == "rock":
                RPS.draw()
                RPS.data_dict["rock_draws"] += 1
                RPS.data_dict["bot_rock_draws"] += 1

                RPS.update_text(data_lbls[15], "rock_draws: " + str(RPS.data_dict["rock_draws"]))
                RPS.update_text(data_lbls[27], "bot_rock_draws: " + str(RPS.data_dict["bot_rock_draws"]))
            elif bot_tool == "paper":
                RPS.lose()
                RPS.data_dict["rock_losses"] += 1
                RPS.data_dict["bot_paper_wins"] += 1

                RPS.update_text(data_lbls[14], "rock_losses: " + str(RPS.data_dict["rock_losses"]))
                RPS.update_text(data_lbls[28], "bot_paper_wins: " + str(RPS.data_dict["bot_paper_wins"]))
            elif bot_tool == "scissors":
                RPS.win()
                RPS.data_dict["rock_wins"] += 1
                RPS.data_dict["bot_scissors_losses"] += 1

                RPS.update_text(data_lbls[13], "rock_wins: " + str(RPS.data_dict["rock_wins"]))
                RPS.update_text(data_lbls[32], "bot_scissors_losses: " + str(RPS.data_dict["bot_scissors_losses"]))
        elif tool == "paper":
            RPS.data_dict["papers_played"] += 1

            RPS.update_text(data_lbls[11], "papers_played: " + str(RPS.data_dict["papers_played"]))
            if bot_tool == "rock":
                RPS.win()
                RPS.data_dict["paper_wins"] += 1
                RPS.data_dict["bot_rock_losses"] += 1

                RPS.update_text(data_lbls[16], "paper_wins: " + str(RPS.data_dict["paper_wins"]))
                RPS.update_text(data_lbls[26], "bot_rock_losses: "+str(RPS.data_dict["bot_rock_losses"]))
            elif bot_tool == "paper":
                RPS.draw()
                RPS.data_dict["paper_draws"] += 1
                RPS.data_dict["bot_paper_draws"] += 1

                RPS.update_text(data_lbls[18], "paper_draws: " + str(RPS.data_dict["paper_draws"]))
                RPS.update_text(data_lbls[30], "bot_paper_draws: " + str(RPS.data_dict["bot_paper_draws"]))
            elif bot_tool == "scissors":
                RPS.lose()
                RPS.data_dict["paper_losses"] += 1
                RPS.data_dict["bot_scissors_wins"] += 1

                RPS.update_text(data_lbls[17], "paper_losses: " + str(RPS.data_dict["paper_losses"]))
                RPS.update_text(data_lbls[31], "bot_scissors_wins: " + str(RPS.data_dict["bot_scissors_wins"]))
        elif tool == "scissors":
            RPS.data_dict["scissors_played"] += 1

            RPS.update_text(data_lbls[12], "scissors_played: " + str(RPS.data_dict["scissors_played"]))
            if bot_tool == "rock":
                RPS.lose()
                RPS.data_dict["scissors_losses"] += 1
                RPS.data_dict["bot_rock_wins"] += 1

                RPS.update_text(data_lbls[20], "scissors_losses: " + str(RPS.data_dict["scissors_losses"]))
                RPS.update_text(data_lbls[25], "bot_rock_wins: "+str(RPS.data_dict["bot_rock_wins"]))
            elif bot_tool == "paper":
                RPS.win()
                RPS.data_dict["scissors_wins"] += 1
                RPS.data_dict["bot_paper_losses"] += 1

                RPS.update_text(data_lbls[19], "scissors_wins: " + str(RPS.data_dict["scissors_wins"]))
                RPS.update_text(data_lbls[29], "bot_paper_losses: " + str(RPS.data_dict["bot_paper_losses"]))
            elif bot_tool == "scissors":
                RPS.draw()
                RPS.data_dict["scissors_draws"] += 1
                RPS.data_dict["bot_scissors_draws"] += 1

                RPS.update_text(data_lbls[21], "scissors_draws: " + str(RPS.data_dict["scissors_draws"]))
                RPS.update_text(data_lbls[33], "bot_scissors_draws: " + str(RPS.data_dict["bot_scissors_draws"]))
        RPS.data_dict["games_played"] += 1
        RPS.update_text(data_lbls[0], "games played: "+str(RPS.data_dict["games_played"]))


    @staticmethod
    def win():
        RPS.curr_wins += 1
        RPS.data_dict["wins"] += 1
        RPS.data_dict["win_streak"] += 1
        RPS.data_dict["lose_streak"] = 0
        RPS.data_dict["draw_streak"] = 0
        if RPS.data_dict["win_streak"] > RPS.data_dict["highest_win_streak"]:
            RPS.data_dict["highest_win_streak"] += 1


        RPS.update_text(p_scr_lbl, RPS.curr_wins)
        RPS.update_text(data_lbls[1], "wins: "+str(RPS.data_dict["wins"]))
        RPS.update_text(data_lbls[4], "win_streak: "+str(RPS.data_dict["win_streak"]))
        RPS.update_text(data_lbls[5], "lose_streak: " + str(RPS.data_dict["lose_streak"]))
        RPS.update_text(data_lbls[6], "draw_streak: " + str(RPS.data_dict["draw_streak"]))
        RPS.update_text(data_lbls[7], "highest_win_streak: "+str(RPS.data_dict["highest_win_streak"]))

    @staticmethod
    def lose():
        RPS.bot_curr_wins += 1
        RPS.data_dict["losses"] += 1
        RPS.data_dict["win_streak"] = 0
        RPS.data_dict["lose_streak"] += 1
        RPS.data_dict["draw_streak"] = 0
        if RPS.data_dict["lose_streak"] > RPS.data_dict["highest_lose_streak"]:
            RPS.data_dict["highest_lose_streak"] += 1

        RPS.update_text(b_scr_lbl, RPS.bot_curr_wins)
        RPS.update_text(data_lbls[2], "losses: "+str(RPS.data_dict["losses"]))
        RPS.update_text(data_lbls[4], "win_streak: " + str(RPS.data_dict["win_streak"]))
        RPS.update_text(data_lbls[5], "lose_streak: " + str(RPS.data_dict["lose_streak"]))
        RPS.update_text(data_lbls[6], "draw_streak: " + str(RPS.data_dict["draw_streak"]))
        RPS.update_text(data_lbls[8], "highest_lose_streak: " + str(RPS.data_dict["highest_lose_streak"]))

    @staticmethod
    def draw():
        RPS.data_dict["draws"] += 1
        RPS.data_dict["win_streak"] = 0
        RPS.data_dict["lose_streak"] = 0
        RPS.data_dict["draw_streak"] += 1
        if RPS.data_dict["draw_streak"] > RPS.data_dict["highest_draw_streak"]:
            RPS.data_dict["highest_draw_streak"] += 1

        RPS.update_text(data_lbls[3], "draws: " + str(RPS.data_dict["draws"]))
        RPS.update_text(data_lbls[4], "win_streak: " + str(RPS.data_dict["win_streak"]))
        RPS.update_text(data_lbls[5], "lose_streak: " + str(RPS.data_dict["lose_streak"]))
        RPS.update_text(data_lbls[6], "draw_streak: " + str(RPS.data_dict["draw_streak"]))
        RPS.update_text(data_lbls[9], "highest_draw_streak: " + str(RPS.data_dict["highest_draw_streak"]))

    @staticmethod
    def update_text(lbl, new):
        lbl.config(text=new)

    @staticmethod
    def save_data():
        f = open("data.txt", "w")
        # f.write(f"{RPS.games_played}\n{RPS.wins}\n{RPS.losses}\n{RPS.draws}\n{RPS.win_streak}\n{RPS.lose_streak}\n{RPS.draw_streak}\n{RPS.highest_win_streak}\n{RPS.highest_lose_streak}\n{RPS.highest_draw_streak}\n{RPS.rocks_played}\n{RPS.papers_played}\n{RPS.scissors_played}\n{RPS.rock_wins}\n{RPS.rock_losses}\n{RPS.rock_draws}\n{RPS.paper_wins}\n{RPS.paper_losses}\n{RPS.paper_draws}\n{RPS.scissors_wins}\n{RPS.scissors_losses}\n{RPS.scissors_draws}\n{RPS.bot_rocks_played}\n{RPS.bot_papers_played}\n{RPS.bot_scissors_played}\n{RPS.bot_rock_wins}\n{RPS.bot_rock_losses}\n{RPS.bot_rock_draws}\n{RPS.bot_paper_wins}\n{RPS.bot_paper_losses}\n{RPS.bot_paper_draws}\n{RPS.bot_scissors_wins}\n{RPS.bot_scissors_losses}\n{RPS.bot_scissors_draws}\n{RPS.seconds_spent_in_app}")
        for data in RPS.data_dict.values():
            f.write(str(data)+"\n")
        f.close()

    @staticmethod
    def load_data():
        f = open("data.txt", "r")
        data_list = f.read().split("\n")
        for (data, lbl, dict_key) in zip(data_list, data_lbls, RPS.data_dict.keys()):
            RPS.data_dict[dict_key] = int(data)
            RPS.update_text(lbl, dict_key + ": " + data)
        f.close()


try:
    data_file = open("data.txt", "x")
    data_file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n")
    data_file.close()
except FileExistsError:
    pass

tools = ["rock", "paper", "scissors"]

bg_col = "black"
font_col = "white"

window = tk.Tk()
window.config(background=bg_col)
window.geometry("800x600")
window.resizable(width=False, height=False)

pvb = RPS.crt_label(window, "Player vs Bot", 50)
p_scr_lbl = RPS.crt_label(window, RPS.curr_wins, 50)
b_scr_lbl = RPS.crt_label(window, RPS.bot_curr_wins, 50)
bot_lbl = RPS.crt_label(window, "BOT", 50)
bot_tool_lbl = RPS.crt_label(window, "", 50)
tool_lbl = RPS.crt_label(window, "", 50)
player_lbl = RPS.crt_label(window, "PLAYER", 50)
rock_button = RPS.crt_button(window, "ROCK", 50, command=lambda: RPS.duel(tools[0]))
paper_button = RPS.crt_button(window, "PAPER", 50, command=lambda: RPS.duel(tools[1]))
scissors_button = RPS.crt_button(window, "SCISSORS", 50, command=lambda: RPS.duel(tools[2]))
save_button = RPS.crt_button(window, "Save data", 50, command=RPS.save_data)


pvb.grid(column=0, row=0, columnspan=3)
p_scr_lbl.grid(column=0, row=1)
b_scr_lbl.grid(column=2, row=1)
bot_lbl.grid(column=0, row=2, columnspan=3)
bot_tool_lbl.grid(column=0, row=3, columnspan=3)
tool_lbl.grid(column=0, row=4, columnspan=3)
player_lbl.grid(column=0, row=5, columnspan=3)
rock_button.grid(column=0, row=6, columnspan=1)
paper_button.grid(column=1, row=6, columnspan=1)
scissors_button.grid(column=2, row=6, columnspan=1)
save_button.grid(column=0, row=7, columnspan=2, sticky="w")

# Stats
colnum = 0
rownum = 7
data_lbls = []
first_col_check = False
for i, item in enumerate(RPS.data_dict.items()):
    rownum += 1
    if i % 10 == 0 and i / 1 != 0 and not(first_col_check):
        colnum += 3
        rownum = 0
        first_col_check = True
    elif i % 22 == 0 and i / 1 != 0 and first_col_check:
        colnum += 3
        rownum = 0

    data_lbls.append(RPS.crt_label(window, item[0]+": 00000", 50))
    data_lbls[i].grid(column=colnum, row=rownum, columnspan=3, sticky="w")

RPS.load_data()

def update_time():
    RPS.data_dict["seconds_spent_in_app"] += 1
    data_lbls[34].config(text="seconds_spent_in_app: "+str(RPS.data_dict["seconds_spent_in_app"]))
    data_lbls[34].after(1000, update_time)
update_time()

window.mainloop()
