import tkinter as tk
import time

window_size = "380x300"

# General
background_color_theme = "#000000"
font_color_theme = "#ffffff"
main_font = "Roboto"

# Labels
# Time label
time_label_font_size = " 50"

# label
label_font_size = " 25"

# Exit button
exit_button_text = "X"
exit_button_size = (15, 4)
exit_button_font_size = " 30"
exit_button_bg_color = "Red"
exit_button_hl_color = "#a30000"

window = tk.Tk()
window.config(background=background_color_theme)
window.geometry(window_size)
window.resizable(width=False, height=False)


def update_time():
    current_time = time.strftime("%T")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def exit_app():
    window.quit()

time_label = tk.Label(window, text="", font=main_font+time_label_font_size, background=background_color_theme, foreground=font_color_theme)
label = tk.Label(window, text="Current time: ", font=main_font+label_font_size, background=background_color_theme, foreground=font_color_theme)

exit_button = tk.Button(
    window, text=exit_button_text, font=main_font+exit_button_font_size, padx=exit_button_size[0], pady=exit_button_size[1], background=exit_button_bg_color, activebackground=exit_button_hl_color, command=exit_app)

time_label.place(relx=0.5, rely=0.4, anchor="center")
label.place(relx=0.5, rely=0.2, anchor="center")

exit_button.place(relx=0.5, rely=0.7, anchor="center")

update_time()

window.mainloop()