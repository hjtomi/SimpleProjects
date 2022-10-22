# Create or log into accounts. Each account has a password, information about the given people
# and a diary that they can write

# Register info: username, full name, gender, birth date, email, job, password, password again

# Saves all profiles and their data

import tkinter as tk
from tkinter import messagebox
import os
import time

def dest_wgts(widget_list):
    for widget in widget_list:
        widget.destroy()


def crt_back_btn():
    return tk.Button(text=" << back ", font=theme_font + " 12")


def enter_screen():
    wgts_on_scrn = []
    enter_message = tk.Label(window, text="Create new account of log in?", background=theme_color, foreground=font_color, font=theme_font)
    new_acc_btn = tk.Button(window, text="Create new account", font=theme_font+" 12")
    log_in_btn = tk.Button(window, text="Log in", font=theme_font+" 12")

    wgts_on_scrn = [enter_message, new_acc_btn, log_in_btn]

    enter_message.grid(column=0, row=0, columnspan=2)
    new_acc_btn.grid(column=0, row=1, sticky="e")
    log_in_btn.grid(column=1, row=1, sticky="w")

    new_acc_btn.configure(command=lambda: [dest_wgts(wgts_on_scrn), crt_new_acc_scrn()])
    log_in_btn.configure(command=lambda: [dest_wgts(wgts_on_scrn), log_in_scrn()])


def crt_new_acc_scrn():
    wgts_on_scrn = []
    # account_attributes = ["Username", "Full name", "Gender", "Birth date", "Email", "Job", "Password", "Confirm password"]
    labels = []
    entries = []
    for attribute in account_attributes:
        labels.append(tk.Label(text=attribute, background=theme_color, foreground=font_color, font=theme_font))

    for attribute in account_attributes:
        entries.append(tk.Entry(width=25, font=theme_font+" 13"))

    back_button = crt_back_btn()
    create_button = tk.Button(text=" Create ", font=theme_font+" 12", borderwidth=5)
    buttons = [back_button, create_button]

    wgts_on_scrn.extend(labels + entries + buttons)

    for i in range(len(labels)):
        labels[i].grid(column=0, row=i, sticky="w")

    for i in range(len(entries)):
        entries[i].grid(column=1, row=i)

    back_button.grid(column=0, row=len(account_attributes) + 1, sticky="wn")
    create_button.grid(column=1, row=len(account_attributes)+1, sticky="en")

    back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), enter_screen()])
    create_button.configure(command=lambda: create())

    def create():
        # Check for errors
        error = False
        for i, entry in enumerate(entries):
            if entry.get() == "":
                messagebox.showwarning(title="Warning!", message="Please fill everything!")
                error = True
                break
            for letter in entry.get():
                #if letter not in "abcdefghijklmnopqrstuvwxyzáéúüűóöőABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÚÜŰÓÖŐ1234567890-_. ":
                if letter in "\/:*?"'<>|':
                    messagebox.showwarning(title="Warning!", message="Invalid character in "+entry.get())
                    error = True
                    break
                if letter in "." and i == 0:
                    messagebox.showwarning(title="Warning!", message="Username can not contain a dot")
                    error = True
                    break
        if entries[-1].get() != entries[-2].get():
            messagebox.showwarning(title="Warning!", message="Password and Confirm password are not the same!")
            error = True

        if not error:
            account_data = {
                "Username": entries[0].get(), "Full name": entries[1].get(), "Gender": entries[2].get(),
                "Birth date": entries[3].get(), "Email": entries[4].get(), "Job": entries[5].get(),
                "Password": entries[6].get()}

            # Saving the file
            try:
                f = open(usertxt_path+account_data["Username"]+".txt", "x")
                for values in account_data.values():
                    f.write(values+"\n")
                f.close()

                create_button.destroy()
                back_button.destroy()
                wgts_on_scrn.remove(create_button)
                wgts_on_scrn.remove(back_button)

                info_label = tk.Label(window, text="Account created successfully!", background=theme_color,
                                      foreground=font_color, font=theme_font+" 12")
                info_label.grid(column=1, row=len(account_attributes) + 1)

                back_button_new = crt_back_btn()
                back_button_new.grid(column=0, row=len(account_attributes) + 1, sticky="wn")
                wgts_on_scrn.append(info_label)
                wgts_on_scrn.append(back_button_new)
                back_button_new.configure(command=lambda: [dest_wgts(wgts_on_scrn), enter_screen()])

            except FileExistsError:
                messagebox.showerror(title="Error!", message="Username already exists!")



def log_in_scrn():
    wgts_on_scrn = []

    # No account
    if len(os.listdir(accounts_path)) == 0:
        info_label = tk.Label(window, text="No accounts yet...", background=theme_color, foreground=font_color, font=theme_font)
        info_label.grid(column=0, row=0)
        back_button = tk.Button(text=" << back ", font=theme_font+" 12")
        back_button.grid(column=0, row=1, sticky="w")

        wgts_on_scrn = [info_label, back_button]

        back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), enter_screen()])
    else:
        back_button = crt_back_btn()

        row_to_put_btn = 0
        acc_btns = {}
        for file in os.listdir(accounts_path):
            acc_button = tk.Button(window, text=file.partition(".")[0], font=theme_font+" 12")
            acc_button.grid(column=0, row=row_to_put_btn, sticky="w")
            row_to_put_btn += 1
            wgts_on_scrn.append(acc_button)
            acc_btns[file] = acc_button

        back_button.grid(column=0, row=len(os.listdir(accounts_path))+1, sticky="w")

        wgts_on_scrn.append(back_button)
        wgts_on_scrn.extend(acc_btns.values())

        # This could be solved with maybe a class that keeps track of how many accounts have been created
        # Like in the todo app
        for key in acc_btns.keys():
            acc_btns[key].configure(command=lambda key=key: [dest_wgts(wgts_on_scrn), specific_log_in_scrn(key)])


        back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), enter_screen()])


# acc is *username*.txt
# example: hjtomi.txt
def specific_log_in_scrn(acc):
    def check_password(password):
        f = open(usertxt_path+acc, "r")
        for i, line in enumerate(f):
            if i == 6:
                acc_pw = line.partition("\n")[0]
        f.close()
        if password == acc_pw:
            dest_wgts(wgts_on_scrn)
            account_screen(acc)
        else:
            messagebox.showwarning(title="Warning!", message="Incorrect password!")

    wgts_on_scrn = []
    info_label = tk.Label(window, text="Enter password", background=theme_color, foreground=font_color, font=theme_font+" 12")
    inp_fld = tk.Entry(window, font=theme_font+" 12")
    back_button = crt_back_btn()
    log_in_btn = tk.Button(window, text="Log in", font=theme_font+" 12")
    info_label.grid(column=0, row=0, sticky="w")
    inp_fld.grid(column=0, row=1, columnspan=2, sticky="w")
    back_button.grid(column=0, row=2, sticky="w")
    log_in_btn.grid(column=1,row=2, sticky="e")

    wgts_on_scrn = [info_label, inp_fld, back_button, log_in_btn]

    back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), log_in_scrn()])
    log_in_btn.configure(command=lambda: check_password(inp_fld.get()))


def account_screen(acc):
    wgts_on_scrn = []
    f = open(usertxt_path+acc, "r")
    for i, line in enumerate(f):
        if i < 6:
            data_name_label = tk.Label(window, text=data_to_show[i], background=theme_color, foreground=font_color,
                                       font=theme_font+" 12")
            data_label = tk.Label(window, text=line.partition("\n")[0], background=theme_color, foreground=font_color,
                                  font=theme_font+" 12")
            data_name_label.grid(column=0, row=i, sticky="wn")
            data_label.grid(column=1, row=i, sticky="wn")
            wgts_on_scrn.append(data_name_label)
            wgts_on_scrn.append(data_label)

    f.close()
    edit_button = tk.Button(window, text="Edit", font=theme_font+" 12")
    back_button = crt_back_btn()

    wgts_on_scrn.append(edit_button)
    wgts_on_scrn.append(back_button)

    edit_button.grid(column=1, row=len(data_to_show)+1)
    back_button.grid(column=0, row=len(data_to_show)+1)

    back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), log_in_scrn()])
    edit_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), edit_account_scrn(acc)])


def edit_account_scrn(acc):
    def save_data():
        error = False
        for i, entry in enumerate(entries):
            if entry.get() == "":
                messagebox.showwarning(title="Warning!", message="Please fill everything!")
                error = True
                break
            for letter in entry.get():
                # if letter not in "abcdefghijklmnopqrstuvwxyzáéúüűóöőABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÚÜŰÓÖŐ1234567890-_. ":
                if letter in "\/:*?"'<>|':
                    messagebox.showwarning(title="Warning!", message="Invalid character in " + entry.get())
                    error = True
                    break
                if letter in "." and i == 0:
                    messagebox.showwarning(title="Warning!", message="Username can not contain a dot")
                    error = True
                    break
        if entries[-1].get() != entries[-2].get():
            messagebox.showwarning(title="Warning!", message="Password and Confirm password are not the same!")
            error = True

        if not error:
            f = open(usertxt_path+acc, "w")
            new_data = ""
            for i in range(len(entries)):
                new_data = new_data+entries[i].get()+"\n"

            f.write(new_data)
            f.close()

            info_label = tk.Label(window, text="Saved!", background=theme_color, foreground=font_color, font=font_color)
            info_label.grid(column=1, row=len(account_attributes)+1)
            wgts_on_scrn.append(info_label)


    def delete_account():
        answer = messagebox.askyesno(title="Warning!", message="Are you sure you want to permanently delete '{}' account?".format(acc.partition(".")[0]))
        if answer == True:
            os.remove(usertxt_path+acc)
            dest_wgts(wgts_on_scrn)
            enter_screen()

    wgts_on_scrn = []

    data = []
    f = open(usertxt_path + acc, "r")
    for line in f:
        data.append(line.partition("\n")[0])
    f.close()

    labels = []
    for i, attribute in enumerate(account_attributes):
        label = tk.Label(window, text=attribute, background=theme_color, foreground=font_color, font=theme_font+" 12")
        label.grid(column=0, row=i, sticky="w")
        labels.append(label)

    entries = []
    for i in range(len(account_attributes)):
        entry = tk.Entry(width=25, font=theme_font+" 12")
        entry.grid(column=1, row=i, columnspan=2)
        entries.append(entry)
        if i < len(account_attributes)-1:
            entry.insert(0, data[i])

    back_button = crt_back_btn()
    save_button = tk.Button(window, text="Save", font=theme_font+" 12", borderwidth=5)
    delete_account_button = tk.Button(text="Delete account", font=theme_font + " 12", command=delete_account)
    back_button.grid(column=0, row=len(account_attributes) + 1, sticky="w")
    save_button.grid(column=2, row=len(account_attributes) + 1, sticky="e")
    delete_account_button.grid(column=2, row=len(account_attributes) + 2, sticky="e")

    wgts_on_scrn.extend([back_button, save_button, delete_account_button] + labels + entries)

    back_button.configure(command=lambda: [dest_wgts(wgts_on_scrn), account_screen(acc)])
    save_button.configure(command=lambda: save_data())


data_to_show = ["Username:", "Full name:", "Gender:", "Birthday:", "email:", "job:"]
account_attributes = ["Username", "Full name", "Gender", "Birth date", "Email", "Job", "Password", "Confirm password"]

accounts_path = "D:\Scripts\Python\SimpleProjects\Scripts\Profiles\Accounts"
usertxt_path = "D:\Scripts\Python\SimpleProjects\Scripts\Profiles\Accounts\\"

theme_color = "black"
theme_font = "Helvetica"
font_color = "white"

window = tk.Tk()
window.geometry("400x300")
window.resizable(height=False, width=False)
window.config(background=theme_color)

enter_screen()

window.mainloop()
