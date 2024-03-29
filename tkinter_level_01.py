from tkinter import *
import ttkbootstrap as ttk
from ctypes import windll

# set high dpi
windll.shcore.SetProcessDpiAwareness(1)

# window
window = ttk.Window(themename="journal")
window.title("Login")
window.geometry("750x400")
window.tk.call('tk', 'scaling', 1.0)


# functions
def convert():
    try:
        miles: int = entryInt.get()
        kilometres: float = miles * 1.61
        # print(miles)
        style.configure("custom.TButton", font=("Helvetica", 46, "bold"))
        output_string.set(str(round(kilometres, 3)) + " km")
        style.configure("custom.TButton", font=("Helvetica", 46))
    except TclError:
        output_string.set("Enter a valid number")


def key_convert(e):
    print(e)
    convert_button.invoke()
    # convert()


# configure button style
style = ttk.Style()
style.configure('custom.TButton', font=('Helvetica', 46))


# labels
title_label = ttk.Label(master=window, text="Miles to Kilometers", font=("Century Gothic", 66, "bold"))
title_label.pack(pady=35)


# text input
input_frame = ttk.Frame(master=window)
entryInt = IntVar(value=None)
value_input = ttk.Entry(master=input_frame, font=("Open Sans", 40), textvariable=entryInt)
value_input.bind("<Return>", key_convert)
value_input.pack(side="left", padx=20)
convert_button = ttk.Button(master=input_frame, text="Convert", style="custom.TButton", command=convert)
convert_button.pack(side="left")
input_frame.pack(pady=30)


# output
output_string = StringVar()
output_label = ttk.Label(master=window, text="Output", font=("Open Sans", 46, "bold"), textvariable=output_string)
output_label.setvar("text", "Hello and Bye")
output_label.pack()


# run
window.mainloop()
