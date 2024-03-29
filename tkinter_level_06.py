import tkinter as tk
from tkinter import ttk
from ctypes import windll

# window
windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
window.geometry("640x480")
window.title("Argument Based-Function Calls for Widgets")


def launch(hello):
    print(hello)


# text
strVar = tk.StringVar(value="What's on your mind...")
textArea = tk.Label(window, textvariable=strVar, font=("Helvetica", 24))
textArea.pack()


def getSome(event, string):
    ctrlAndShift: bool = event.state & 0x1 and event.state & 0x4
    if len(str(event.keysym)) == 1 and (96 < ord(str(event.keysym).lower()) < 123) and ctrlAndShift:
        print(string)


style = ttk.Style()
style.configure('custom.TButton', font=('Helvetica', 26), padding=10)
entry_string = tk.StringVar(value="")
entry = ttk.Entry(window, font=("Helvetica", 24), textvariable=entry_string)
entry.bind("<Key>", lambda event: getSome(event, "OK"))
entry.pack()

counter: int = 0


def execute_challenge():
    global key_pressed, counter
    text_selected = entry.selection_present()
    if key_pressed and text_selected:
        print("Mousewheel" + str(counter))
        counter += 1


# button
btn = ttk.Button(window, text="Hello", style="custom.TButton")
btn.bind("<Key>", lambda event: getSome(event, entry_string.get()))
btn.pack()

# challenge section
key_pressed = False


def set_key_false():
    global key_pressed
    key_pressed = False


def set_key_true(event):
    global key_pressed
    if event.keysym in ("Shift_R", "Shift_L"):
        key_pressed = True


window.bind("<KeyPress>", set_key_true)
window.bind("<KeyRelease>", lambda event: set_key_false)
window.bind("<MouseWheel>", lambda event: execute_challenge)
entry.bind("<Shift-MouseWheel>", lambda event: print("mousewheel"))

# start
window.mainloop()
