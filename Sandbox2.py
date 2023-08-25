import mouse
import tkinter as tk
from tkinter import ttk

def run_sequence():
    for row in tree.get_children():
        actual_row = tree.item(row, 'tags')
        if 'C' in actual_row:
            coords = tree.item(row, 'values')[2:4]
            mouse.move(*coords)
            mouse.click('left')
        elif 'T' in actual_row:
            pass

root = tk.Tk()

tree = ttk.Treeview(root, columns=('Type', 'Value', 'X', 'Y'))
tree.pack()

tree.insert("", "end", values=('C', 'Click', 100, 200), tags=('C',))
tree.insert("", "end", values=('T', 'Text', 300, 400), tags=('T',))

run_button = tk.Button(root, text="Run Sequence", command=run_sequence)
run_button.pack()

root.mainloop()