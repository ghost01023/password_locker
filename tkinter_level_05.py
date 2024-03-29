import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

# window
window = tk.Tk()
window.geometry("400x400")
window.title("Buttons and Types")


# function definitions
def button_func():
    print("A basic button function")


# WIDGETS

# button
button_string = tk.StringVar(value="A button with string var")
button = ttk.Button(master=window, text="Button",
                    command=button_func,
                    textvariable=button_string)
button.pack()

# check-box
custom_style = ttk.Style()

frame_check_boxes = ttk.Frame(master=window)
frame_check_boxes.pack()
bool_var = tk.BooleanVar()
check_box = ttk.Checkbutton(master=frame_check_boxes,
                            text="Male", variable=bool_var,
                            command=lambda: bool_var_2.set(False))
bool_var_2 = tk.BooleanVar()
check_box_1 = ttk.Checkbutton(master=frame_check_boxes,
                              text="Female", variable=bool_var_2,
                              command=lambda: bool_var.set(False))
check_box.pack(side="left", padx=10)
check_box_1.pack(side="left", padx=10)
frame_check_boxes.pack(pady=20)

# radio buttons
frame_radio_buttons = ttk.Frame(master=window)
string_var = tk.StringVar()
radio_button_1 = ttk.Radiobutton(master=frame_radio_buttons,
                                 text="Writer", value="OK",
                                 variable=string_var,
                                 command=lambda: print(string_var.get()))
radio_button_2 = ttk.Radiobutton(master=frame_radio_buttons,
                                 text="Plumber", value="Barely OK",
                                 variable=string_var,
                                 command=lambda: print(string_var.get()))
radio_button_3 = ttk.Radiobutton(master=frame_radio_buttons,
                                 text="Electrician", value="Disgraceful",
                                 variable=string_var,
                                 command=lambda: print(string_var.get()))
radio_button_1.pack(side="left", padx=15)
radio_button_2.pack(side="left", padx=15)
radio_button_3.pack(side="left", padx=15)
frame_radio_buttons.pack(pady=20)


# drop-down
# dd = ttk.OptionMenu(master=window, variable="OK")
# dd.pack()

# exercise


def check_click():
    print(radio1_var.get())


def radio_click():
    print(check_var.get())
    # check_var.set(not check_var.get())
    check_var.set(False)


test_frame = ttk.Frame(master=window)
check_var = tk.BooleanVar()
text_check = ttk.Checkbutton(master=test_frame, text="Box", variable=check_var, command=check_click)
text_check.pack()
radio1_var = tk.StringVar()
radio1 = ttk.Radiobutton(master=test_frame, text="A", value="A", variable=radio1_var, command=radio_click)
radio1.pack(side="left", pady=15)
radio2 = ttk.Radiobutton(master=test_frame, text="B", value="B", variable=radio1_var, command=radio_click)
radio2.pack(side="left", pady=15)
test_frame.pack()
# start
window.mainloop()
