from tkinter import *
from tkinter import ttk
from ctypes import windll

# set high dpi
windll.shcore.SetProcessDpiAwareness(1)


# window
window = Tk()
window.geometry("800x900")
window.title("Text Editor")


# custom styles
style = ttk.Style()
style.configure('custom.TButton', font=('Helvetica', 26), padding=10)


# widgets
text_label = ttk.Label(master=window, text="this is a label", font=("Helvetica", 20, "bold"))
text_label.pack(pady=20)

text_box = Text(master=window)
text_box.pack()

entry = ttk.Entry(master=window, font=("Open Sans", 15))
entry.pack()

ttk.Label(master=window, text="My Label").pack()
ttk.Button(master=window, text="Print Hello", command=lambda: print("Hello, World!")).pack()

print_button = ttk.Button(master=window, text="Print")
print_button.pack(pady=5)


# start
window.mainloop()
