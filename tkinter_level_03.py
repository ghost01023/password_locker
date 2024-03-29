import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("400x400")
window.title("Get/Set Widgets")

style = ttk.Style()


def rem_bold():
    style.configure("Bold.TButton", font=("Helvetica", 12))
    button.config(style="Bold.TButton")


def set_style():
    style.configure('Bold.TButton', font=('Helvetica', 12, 'bold'))
    button.config(style="Bold.TButton")
    label["text"] = entry.get()
    entry["state"] = "disabled"
    button.after(20, rem_bold)


def callSet(e):
    print(e)
    set_style()


def reset():
    global entry_string
    label["text"] = "This is a label"
    entry_string = ""
    entry["state"] = "enabled"


def callReset(e):
    print(e)
    if window["focus"] is not entry:
        reset()


window.bind("<Return>", callReset)

# widgets
label = ttk.Label(master=window, text="This is a label")
label.pack()

entry_string = tk.StringVar()
entry = ttk.Entry(master=window, textvariable=entry_string)
entry.bind("<Return>", callSet)
entry.pack()

button = ttk.Button(master=window, text="Click Me!", command=set_style)
style.configure("Bold.TButton", font=("Helvetica", 12))
button.config(style="Bold.TButton")
button.pack()

reset_button = ttk.Button(master=window, text="Reset", command=reset)
reset_button.config(style="Bold.TButton")
reset_button.pack()

# start
window.mainloop()
