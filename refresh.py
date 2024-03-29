import tkinter as tk
from ctypes import windll

# high resolution
windll.shcore.SetProcessDpiAwareness(1)

# window
window = tk.Tk()
window.title("Refresh")
window.geometry("500x400")

# title
app_desc_label = tk.Label(master=window, text="Unit Converter", font=("Calibri", 18, "italic"))
app_desc_label.pack()


def set_from(k):
    global choice_to
    if choice_from == "Mile":
        choice_to.set(unit_choices[0])
    else:
        choice_to.set(unit_choices[1])


def set_to(l):
    global choice_from
    if choice_to == "Mile":
        choice_from.set(unit_choices[0])
    else:
        choice_from.set(unit_choices[1])


# choice
choice_frame = tk.Frame(master=window)
label_from = tk.Label(master=choice_frame, text="From: ")
label_from.pack(side="left", padx=5)
unit_choices = ["Mile", "Kilometer"]
choice_from = tk.StringVar()
choice_from.set("Select Unit")
# select_from = tk.OptionMenu(master=choice_frame, variable=default_choice_from)
select_from = tk.OptionMenu(choice_frame, choice_from, *unit_choices, command=set_from)
select_from.pack(side="left", padx=5)
label_to = tk.Label(master=choice_frame, text="To: ")
label_to.pack(side="left", padx=5)
choice_to = tk.StringVar(value="Select Unit")
select_to = tk.OptionMenu(choice_frame, choice_to, *unit_choices, command=set_to)
select_to.pack(side="left", padx=5)
choice_frame.pack(pady=10)


def convert(str_from):
    if str_from.get() == "Mile":
        res = input_val.get() * 1.68
    else:
        res = input_val.get() / 1.68
    res_var.set(res)


# input field
label_area = tk.Frame(master=window)
input_val = tk.DoubleVar(value=None)
inp_text = tk.Entry(master=label_area, textvariable=input_val)
inp_text.pack(side="left", padx=10)
inp_text.bind("<Return>", lambda x: convert(choice_from))
inp_btn = tk.Button(master=label_area, text="Convert", command=lambda: convert(choice_from))
inp_btn.pack(side="left", padx=10)
label_area.pack(pady=15)

# result field
res_var = tk.DoubleVar(value=None)
result = tk.Label(window, font=("Anonymous Pro", 16), textvariable=res_var)
result.pack()

# start
window.mainloop()
