import tkinter as tk
from tkinter import ttk
from ctypes import windll
from typing import List

# set-up
window: tk.Tk = tk.Tk()
window.title("TreeView")
window.geometry("1200x900")
windll.shcore.SetProcessDpiAwareness(1)

# lists
first_names: List[str] = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Oliver"]
last_names: List[str] = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                         "Martinez"]

# treeview_style
style: ttk.Style = ttk.Style()
style.configure("Custom.Treeview", font=("Amir", 16))
style.configure("Custom.Treeview.Heading", font=("Century Gothic", 24))

# treeview
table: ttk.Treeview = ttk.Treeview(window, columns=("First Name", "Last Name", "Email"), style="Custom.Treeview",
                                   show="headings")

table.heading("First Name", text="First Name", anchor=tk.CENTER)
table.heading("Last Name", text="Surname", anchor=tk.CENTER)
table.heading("Email", text="email-id", anchor=tk.CENTER)
table.tag_configure("Custom.Treeview", font=("Arial", 28), foreground="black")
table.pack(fill="both", expand=True)

# insert values into table
# table.insert(parent="", index=0, values=("John", "Doe", "John@Doe.com"))
# print("john"[:9])

count: int = 0
for first_name in first_names:
    for last_name in last_names:
        new_person = (first_name, last_name, first_name[0] + last_name[:3] + "@gmail.com")
        table.insert(parent="", index=tk.END, values=new_person)
        count += 1


# events
def item_select():
    # table.selection_add(table.get_children()[len(table.selection())])
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])


def item_delete():
    for i in table.selection():
        all_children = table.get_children()
        next_index = all_children.index(i) + 1
        next_item = all_children[next_index if len(all_children) > next_index else (next_index - 2)]
        table.delete(i)
        if len(all_children) < 2:
            return
        table.selection_add(next_item)


table.bind("<<TreeviewSelect>>", lambda x: item_select())
table.bind("<Shift-Down>", lambda x: print(x))
table.bind("<Delete>", lambda x: item_delete())

# items

# start
window.mainloop()
