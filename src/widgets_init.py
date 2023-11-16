import queue
import threading
import time
import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
# import win32api
import mouse
import keyboard
import json

from src.helpers import AutoClickerHelpers

class AutoClickerApp:

    def __init__(self, window, frame, stop_sec, counter):
        self.window = window
        self.frame = frame
        self.stop_seq = stop_sec
        self.counter = counter
        self.helpers = AutoClickerHelpers(self)

    def create_gui(self):
        # Menu
        self.menu = tk.Menu(self.window)

        # Sub menu
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label='New', command=lambda: print('New file'))
        self.file_menu.add_command(label='Open', command=lambda: print('Open file'))
        self.file_menu.add_separator()
        self.menu.add_cascade(label='File', menu=self.file_menu)

        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.help_check_string = tk.StringVar()
        self.help_menu.add_command(label='Help entry', command=lambda: print(self.help_check_string.get()))
        self.help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=self.help_check_string)

        self.menu.add_cascade(label='Help', menu=self.help_menu)

        self.exercise_menu = tk.Menu(self.menu, tearoff=False)
        self.exercise_menu.add_command(label='exercise test 1')
        self.menu.add_cascade(label='Exercise', menu=self.exercise_menu)

        self.exercise_sub_menu = tk.Menu(self.menu, tearoff=False)
        self.exercise_sub_menu.add_command(label='some more stuff')
        self.exercise_menu.add_cascade(label='more stuff', menu=self.exercise_sub_menu)
        self.window.configure(menu=self.menu)

        # Tabs
        self.tabControl = ttk.Notebook(self.frame)
        self.tabControl.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text='Add Click')
        self.tabControl.add(self.tab2, text='Tab Text')
        self.tabControl.add(self.tab3, text='Add Wait (Inactive tab)')

        # TAB 1
        ttk.Label(self.tab1, text="X position: ").grid(column=0, row=0, padx=(10, 10), pady=(20, 5))
        ttk.Label(self.tab1, text="Y position: ").grid(column=0, row=1, padx=(10, 10), pady=0)

        self.x_pos_spinbox = tk.Spinbox(self.tab1, from_=0, to=3000)
        self.x_pos_spinbox.grid(column=1, row=0, padx=(10, 10), pady=(30, 5), ipadx=5)
        self.y_pos_spinbox = tk.Spinbox(self.tab1, from_=0, to=2000)
        self.y_pos_spinbox.grid(column=1, row=1, padx=(10, 10), pady=(2, 5), ipadx=5)

        self.get_click_position = ttk.Button(self.tab1, text="Get Click Position (CTRL+Click)", command=self.helpers.get_click_position_x_y)
        self.get_click_position.grid(column=3, row=0, rowspan=2, columnspan=3, pady=(25, 0), padx=(8, 8), ipadx=80, ipady=10)

        ttk.Label(self.tab1, text="Right click ").grid(column=0, row=2, pady=(2, 5))
        ttk.Label(self.tab1, text="Double click ").grid(column=0, row=3, pady=(2, 5))
        ttk.Label(self.tab1, text="Human-like mouse move ").grid(column=0, row=4, pady=(2, 5))

        # check_box_right_click_value = tk.IntVar()
        # check_box_right_click=ttk.Checkbutton(tab1, onvalue=1, offvalue=0,variable=check_box_right_click_value).grid(column=1, row=2,padx=(30,10), pady=(2, 5))
        #
        self.check_box_right_click = tkinter.IntVar()
        self.check_box_right_click_checkbox = ttk.Checkbutton(self.tab1, variable=self.check_box_right_click, onvalue=1, offvalue=0)
        self.check_box_right_click_checkbox.grid(column=1, row=2, padx=(30, 10), pady=(2, 5))

        self.check_box_double_click = tkinter.IntVar()
        self.check_box_double_click_checkbox = ttk.Checkbutton(self.tab1, variable=self.check_box_double_click, onvalue=1, offvalue=0)
        self.check_box_double_click_checkbox.grid(column=1, row=3, padx=(30, 10), pady=(2, 5))

        self.check_box_h_mouse_movement = tkinter.IntVar()
        self.check_box_h_mouse_movement_checkbox = ttk.Checkbutton(self.tab1, variable=self.check_box_h_mouse_movement, onvalue=1, offvalue=0)
        self.check_box_h_mouse_movement_checkbox.grid(column=1, row=4, padx=(30, 10), pady=(2, 5))

        ttk.Label(self.tab1, text="Wait after step [s]: ").grid(column=0, row=5, padx=(30, 10), pady=(2, 5))
        self.wait_spinbox_click = tk.Spinbox(self.tab1, from_=0, to=600)
        self.wait_spinbox_click.grid(column=1, row=5, padx=(10, 10), pady=(2, 5), ipadx=5)

        self.add_click = ttk.Button(self.tab1, text="ADD", command=lambda: self.helpers.add_item("C", self.wait_spinbox_click))
        self.add_click.grid(column=3, row=2, rowspan=4, columnspan=3, padx=(10, 10), pady=(5, 15), ipadx=130, ipady=68)
        # TAB 2
        ttk.Label(self.tab2, text="Text: ").grid(column=0, row=0, padx=(10, 10), pady=(20, 5))
        self.textbox = tk.Text(self.tab2, height=2, width=30)
        self.textbox.grid(column=1, row=0, padx=(10, 10), pady=(20, 5), ipadx=100, ipady=45)

        ttk.Label(self.tab2, text="Wait after step [s]: ").grid(column=0, row=2, padx=(30, 10), pady=(2, 5))
        self.wait_spinbox_text = tk.Spinbox(self.tab2, from_=0, to=600)
        self.wait_spinbox_text.grid(column=1, row=2, padx=(10, 10), pady=(2, 5), ipadx=5)

        self.add_text = ttk.Button(self.tab2, text="ADD", command=lambda: self.helpers.add_item("T", self.wait_spinbox_text)).grid(column=0, row=3,
                                                                                                       columnspan=4,
                                                                                                       padx=(40, 40),
                                                                                                       pady=(5, 15), ipadx=260,
                                                                                                       ipady=10)

        # TAB 3
        ttk.Label(self.tab3, text="Wait after step [s]: ").grid(column=0, row=0, padx=(30, 10), pady=(100, 30))
        self.wait_spinbox_wait = tk.Spinbox(self.tab3, from_=0, to=600).grid(column=1, row=0, padx=(10, 10), pady=(100, 30), ipadx=5)
        self.add_wait = ttk.Button(self.tab3, text="ADD").grid(column=0, row=1, columnspan=4, padx=(40, 40), pady=(5, 15), ipadx=260,
                                                     ipady=10)

        #todo: add result processing tab and lines

        # Table / Treeview

        self.columns = ('line', 'C/T', 'X pos', 'Y pos', "Right Click", "Double click", "Hl mouse movement", "Text", "Wait")
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings")

        self.tree.tag_configure('ttk', background='yellow')
        self.tree.heading('line', text='Line')
        self.tree.column('line', minwidth=0, width=40, anchor=tk.CENTER)
        self.tree.heading('C/T', text='Click/Text')
        self.tree.column('C/T', minwidth=0, width=90, anchor=tk.CENTER)
        self.tree.heading('X pos', text='X pos')
        self.tree.column('X pos', minwidth=0, width=55, anchor=tk.CENTER)
        self.tree.heading('Y pos', text="Y pos")
        self.tree.column('Y pos', minwidth=0, width=55, anchor=tk.CENTER)
        self.tree.heading('Right Click', text="Right Click")
        self.tree.column('Right Click', minwidth=0, width=85, anchor=tk.CENTER)
        self.tree.heading('Double click', text="Double click")
        self.tree.column('Double click', minwidth=0, width=110, anchor=tk.CENTER)
        self.tree.heading('Hl mouse movement', text="HLMM")
        self.tree.column('Hl mouse movement', minwidth=0, width=80, anchor=tk.CENTER)
        self.tree.heading('Text', text="Text")
        self.tree.column('Text', minwidth=0, width=280, anchor=tk.CENTER)
        self.tree.heading('Wait', text="Wait [s]")
        self.tree.column('Wait', minwidth=0, width=50, anchor=tk.CENTER)
        self.tree.grid(row=1, column=0, columnspan=3, padx=30, pady=10)



        # Buttons
        self.save_sequence_button = tk.Button(self.frame, text="Save sequence", command=self.helpers.save_sequence)
        self.save_sequence_button.grid(row=3, column=0, columnspan=3, sticky="news", padx=20, pady=7)
        self.load_sequence_button = tk.Button(self.frame, text="Load sequence", command=self.helpers.load_sequence)
        self.load_sequence_button.grid(row=4, column=0, columnspan=3, sticky="news", padx=20, pady=7)
        self.run_sequence_button = tk.Button(self.frame, text="RUN SEQUENCE", bg="#5cc41e", command=self.helpers.run_sequence)
        self.run_sequence_button.grid(row=5, column=0, columnspan=3, sticky="news", padx=20, pady=5, ipady=10)
        self.run_sequence_continuously_button = tk.Button(self.frame, text="RUN SEQUENCE CONTINUOUSLY", bg="#03AC13", command=self.helpers.run_sequence_countinuously)
        self.run_sequence_continuously_button.grid(row=6, column=0,columnspan=2, sticky="news", padx=20, pady=5, ipadx=5, ipady=5)
        self.stop_sequence_button = tk.Button(self.frame, text="STOP SEQUENCE  (Press S)", bg="#FF0000")
        self.stop_sequence_button.grid(row=6, column=2, columnspan=2, sticky="news", padx=20, pady=5, ipadx=130, ipady=5)

        self.edit_btn = ttk.Button(self.frame, text="Edit", command=self.helpers.edit)
        self.edit_btn.grid(row=2, column=0, columnspan=1, padx=5, pady=10)
        self.del_btn = ttk.Button(self.frame, text="Delete", command=self.helpers.delete)
        self.del_btn.grid(row=2, column=2, columnspan=1, padx=5, pady=10)

        # extra window
        self.ew_counter = 0
        self.items = ('C', 'T')
        self.ew_combobox_value = tk.StringVar(value=self.items[0])

        self.ew_check_box_right_click = tk.BooleanVar(value=False)
        self.ew_check_box_double_click = tk.BooleanVar(value=False)
        self.ew_check_box_h_mouse_movement = tk.BooleanVar(value=False)

        self.tree.bind('<<TreeviewSelect>>', self.helpers.item_select())
