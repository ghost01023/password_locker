import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

# window
window = tk.Tk()
window.title("Refresher")
window.geometry("500x500")

# widgets
# button
intVar = tk.IntVar()
intVar.set(45)
helloWorldBtn = ttk.Button(master=window, textvariable=intVar, command=lambda: intVar.set(1000))
helloWorldBtn.pack(pady=10)

# label
userLabel = ttk.Label(master=window, textvariable=intVar)
userLabel.pack(pady=10)


alive = tk.BooleanVar()
# checkbox
alive.set(False)


def aliveStatus():
    # alive.set(not alive.get())
    print("Alive: " + str(alive.get()))


checkBox1 = ttk.Checkbutton(master=window, text="Alive?", variable=alive, command=aliveStatus)
checkBox1.pack(pady=5)

# radio
cuntVar = tk.StringVar()
radio_finland = ttk.Radiobutton(master=window, text="Finland", value="Finland", variable=cuntVar)
radio_kazakhstan = ttk.Radiobutton(master=window, text="Kazakhstan", value="Kazakhstan", variable=cuntVar)
radio_finland.pack()
radio_kazakhstan.pack()

# start
window.mainloop()
