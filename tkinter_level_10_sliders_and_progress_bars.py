import tkinter as tk
from tkinter import ttk
from ctypes import windll

# window
window = tk.Tk()
window.geometry("500x500")
window.title("Sliders")
windll.shcore.SetProcessDpiAwareness(1)

# sliders
slider_int = tk.IntVar(value=44)
slider_horizontal = ttk.Scale(window, from_=18, to=78, length=300, variable=slider_int,
                              command=lambda x: set_progress_val())
slider_horizontal.pack(pady="40")


def set_progress_val():
    progress_val.set(int(((slider_int.get() - 18) / 58) * 100))


progress_val = tk.IntVar(value=0)
set_progress_val()

progress_bar = ttk.Progressbar(window, variable=progress_val)
progress_bar.pack()

# start
window.mainloop()
