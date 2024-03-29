import tkinter as tk
from tkinter import ttk
from ctypes import windll

# window
window = tk.Tk()
window.geometry("500x500")
window.title = "Related Widgets"
windll.shcore.SetProcessDpiAwareness(1)

# tkinter_variable
string_var = tk.StringVar()

# widgets
entry1 = ttk.Entry(master=window, textvariable=string_var, font=("Helvetica", 24))
entry1.pack(pady=10)
entry2 = ttk.Entry(master=window, textvariable=string_var, font=("Helvetica", 24))
entry2.pack(pady=10)

label = ttk.Label(master=window, textvariable=string_var, font=("Helvetica", 24))
label.pack(pady=10)

window.mainloop()
