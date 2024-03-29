import math
import tkinter as tk
from ctypes import windll

# setup
window = tk.Tk()
window.title("Canvas_#01")

width = 800
height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
windll.shcore.SetProcessDpiAwareness(1)
dpi_scale = windll.user32.GetDpiForSystem() / 96  # DPI scaling factor
scaled_width = int(width * dpi_scale)
scaled_height = int(height * dpi_scale)

x = (screen_width - scaled_width) * 7
y = (screen_height - scaled_height) * 2
geometry_string = f"{width}x{height}+{x}+{int(math.fabs(y))}"
window.geometry(geometry_string)


# canvas draw functions
# def set_color(color):
#     canvas.itemconfigure(rectangle, fill=color)


def set_border(item_id, val):
    width_val = 3 if canvas.type(item_id) == "oval" else 1
    canvas.itemconfigure(item_id, width=(width_val if val else 0), dash=(1, 2))


def make_selectable(item_id):
    canvas.tag_bind(item_id, "<Enter>", lambda p: set_border(item_id, True))
    canvas.tag_bind(item_id, "<Leave>", lambda p: set_border(item_id, False))


drag_event_array = []

new_figure = True


def canvas_r_btn_click_drag(event):
    global new_figure
    if new_figure:
        new_figure = False
        if figure_choice_val.get() == "rectangle":
            created_figure = canvas.create_rectangle((event.x, event.y, event.x, event.y), width=0)
            make_selectable(created_figure)
        elif figure_choice_val.get() == "oval":
            created_figure = canvas.create_oval((event.x, event.y, event.x, event.y), width=0)
            make_selectable(created_figure)
        else:
            created_figure = canvas.create_line((event.x, event.y, event.x, event.y), width=1)
        canvas.itemconfigure(canvas.find_all()[-1], fill=figure_color_val.get())
        canvas.tag_bind(created_figure, "<Button-1>", select_element)
    else:
        item_id = canvas.find_all()[-1]
        drag_event(event, item_id)


in_selection = False


def select_element(event):
    global in_selection
    in_selection = True
    item_id = canvas.find_closest(event.x, event.y)[0]
    select_label_val.set(item_id)


def deselect_element():
    global in_selection
    if not in_selection:
        select_label_val.set(0)
    else:
        in_selection = False


def canvas_r_btn_reset():
    global new_figure
    del drag_event_array[:]
    new_figure = True


def update_figure(item_id, coords):
    new_coords = [coords[0][0], coords[0][1], coords[1][0], coords[1][1]]
    canvas.coords(item_id, *new_coords)


def drag_event(event, item_id):
    if len(drag_event_array) == 2:
        drag_event_array[1] = (event.x, event.y)
        update_figure(item_id, drag_event_array)
    else:
        drag_event_array.append((event.x, event.y))
    print(drag_event_array)


# canvas
canvas = tk.Canvas(window, bg="white", width=700, height=500)
canvas.pack()


# rectangle = canvas.create_rectangle((10, 10, 200, 100), fill="pink", width=0)
# make_selectable(rectangle)
# circle = canvas.create_oval((150, 150, 250, 250), fill="green", width=0)
# make_selectable(circle)


def empty_drag_array():
    del drag_event_array[:]


def delete_element(key):
    if key == "Delete" and select_label_val.get() > 0:
        canvas.delete(select_label_val.get())
        select_label_val.set(0)


canvas.bind("<Button-1>", lambda p: deselect_element())
canvas.bind("<B1-Motion>", lambda p: canvas_r_btn_click_drag(p))
canvas.bind("<ButtonRelease-1>", lambda p: canvas_r_btn_reset())
window.bind("<KeyPress>", lambda p: delete_element(p.keysym))

# figure choices
figure_choices = ("rectangle", "oval", "line")
figure_choice_val = tk.StringVar(value=figure_choices[0])
figure_menu = tk.OptionMenu(window, figure_choice_val, *figure_choices)
figure_menu.pack(side="left")

# figure_color
figure_color_choices = ("red", "green", "blue", "black", "teal", "pink")
figure_color_val = tk.StringVar(value=figure_color_choices[0])
figure_color_menu = tk.OptionMenu(window, figure_color_val, *figure_color_choices)
figure_color_menu.pack(side="left")

# selected_label
select_label_val = tk.IntVar(value=0)
select_label = tk.Label(window, textvariable=select_label_val)
select_label.pack()

# start
window.mainloop()
