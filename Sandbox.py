import tkinter as tk
from tkinter import ttk

def insert_value():
    # value = entry.get()  # Get the value from the Entry widget
    combo.insert(tk.END, 'C')  # Insert the value at the end of the list
    check_box_left_click_proba.set(0)

root = tk.Tk()
root.title("Combobox Insert Example")

entry = tk.Entry(root)
entry.pack()

insert_button = tk.Button(root, text="Insert Value", command=insert_value)
insert_button.pack()

ttk.Label(root, text="Click/Text ").pack()
items = ('C', 'T')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(root, textvariable=food_string)
combo['values'] = items
combo.pack()

check_box_left_click_proba = tk.BooleanVar()
check_box_left_click_proba_checkbox = ttk.Checkbutton(root, variable=check_box_left_click_proba, onvalue=1,
                                                      offvalue=0)
check_box_left_click_proba_checkbox.pack()

root.mainloop()
