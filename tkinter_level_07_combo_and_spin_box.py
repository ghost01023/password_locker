import tkinter as tk
from tkinter import ttk
from ctypes import windll

# set high dpi
windll.shcore.SetProcessDpiAwareness(1)

# window
window = tk.Tk()
window.title("Combobox and Spinbox")
window.geometry("500x450")

# widgets
combo_choices = ("Vanilla", "Chocolate", "Strawberry", "Grape", "Mint")
combo_string = tk.StringVar(value="Select Flavor")
combo_box = ttk.Combobox(master=window, textvariable=combo_string)
combo_box["values"] = combo_choices
combo_box.bind("<<ComboboxSelected>>", lambda x: print("Testing..."))
combo_box.pack()


def spin_crement(event):
    spin_int.set(((spin_int.get()) % 44))


spin_int = tk.IntVar(value=3)
spin = ttk.Spinbox(window, from_=3, to=44, textvariable=spin_int)
spin.bind("<<Increment>>", spin_crement)
spin.bind("<<Decrement>>", spin_crement)
# spin["value"] = [x for x in range(0, 100)]
spin.pack()


# challenge spin-box
sp_value = tk.StringVar(value="A")
sp_box = ttk.Spinbox(window, textvariable=sp_value)
sp_box_values = ("A", "B", "C", "D", "E")
sp_box["value"] = sp_box_values
sp_box.bind("<<Increment>>", lambda x: print(sp_value.get()))
sp_box.pack()

# start
window.mainloop()
