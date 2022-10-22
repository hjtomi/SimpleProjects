import tkinter as tk

class todos:
    amt_of_todos = 0
    def __init__(self, text):
        todos.amt_of_todos += 1
        self.text = text
        self.dict_num = todos.amt_of_todos

    def __repr__(self):
        return "text={}, dict_num={}".format(self.text, self.dict_num)

    def __str__(self):
        return self.text


def create_todo(text):
    todo_dict[todos.amt_of_todos] = todos(text)

    num = todos.amt_of_todos

    label_dict[todos.amt_of_todos] = tk.Label(text=text, font=50)
    label_dict[todos.amt_of_todos].grid(column=0, row=todos.amt_of_todos+2)

    done_dict[todos.amt_of_todos] = tk.Button(text="D", font=50, command=lambda: done_todo(num))
    done_dict[todos.amt_of_todos].grid(column=1, row=todos.amt_of_todos + 2)

    del_dict[todos.amt_of_todos] = tk.Button(text="X", font=50, command=lambda: del_todo(num))
    del_dict[todos.amt_of_todos].grid(column=2, row=todos.amt_of_todos + 2)

    input_field.delete(0, "end")


def done_todo(dict_num):
    label_dict[dict_num].config(foreground="red")


def del_todo(dict_num):
    del todo_dict[dict_num]

    label_dict[dict_num].destroy()
    del label_dict[dict_num]

    done_dict[dict_num].destroy()
    del done_dict[dict_num]

    del_dict[dict_num].destroy()
    del del_dict[dict_num]


todo_dict = {}
label_dict = {}
done_dict = {}
del_dict = {}

window = tk.Tk()

input_field = tk.Entry(window, font=50)
create_button = tk.Button(window, text="Create", font=50, command=lambda: create_todo(input_field.get()))
input_field.grid(column=0, row=0)
create_button.grid(column=1, row=0, columnspan=2, rowspan=2)

window.mainloop()

print(todo_dict)
print(label_dict)
print(done_dict)
print(del_dict)
