import queue
import threading
import time
import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import win32api
import mouse
import keyboard
import json





counter = 1
print(counter)

# GUI Handling

def item_select(_):
    print(tree.selection(), type(tree.selection()))
    for i in tree.selection():
        print(tree.item(i)['values'])

def create_edit_window():

    def select_record():
        global ew_counter
        # select row
        selected = tree.focus()
        values = tree.item(selected, 'values')

        # delete all values before editing them
        ew_x_pos_spinbox.delete(0, tk.END)
        ew_y_pos_spinbox.delete(0, tk.END)
        combo.delete(0, tk.END)
        wait_spinbox.delete(0, tk.END)
        textbox.delete(tk.END, tk.END)
        ew_check_box_right_click.set(False)
        ew_check_box_double_click.set(False)
        ew_check_box_h_mouse_movement.set(False)

        # import all values from selected row
        ew_counter = values[0]
        combo.insert(0, values[1])
        ew_x_pos_spinbox.insert(0, values[2])
        ew_y_pos_spinbox.insert(0, values[3])
        ew_check_box_right_click.set(True if values[4] == "x" else False)
        ew_check_box_double_click.set(True if values[5] == "x" else False)
        ew_check_box_h_mouse_movement.set(True if values[6] == "x" else False)
        textbox.insert(1.0, values[7])
        wait_spinbox.insert(0, values[8])

    def update_record():
        selected = tree.focus()

        ew_record = [ew_counter,
                     combo.get(),
                     int(ew_x_pos_spinbox.get()) if combo.get() == 'C' else "",
                     int(ew_y_pos_spinbox.get()) if combo.get() == 'C' else "",
                     'x' if ew_check_box_right_click.get() is True and combo.get() == 'C' else "",
                     'x' if ew_check_box_double_click.get() is True and combo.get() == 'C' else "",
                     'x' if ew_check_box_h_mouse_movement.get() is True and combo.get() == 'C' else "",
                     textbox.get("1.0", 'end-1c') if combo.get() == 'T' else "",
                     int(wait_spinbox.get())]



        tree.item(selected, text="", values=ew_record)

        if combo.get() == 'C' and textbox.get("1.0", 'end-1c') != '':
            # answer = messagebox.askquestion('Title', 'You chose ' )
            messagebox.showinfo('Info', 'You chose "Click" as action, therefore the text is not added to the record')

    def ew_get_click_position_x_y():
        click_x = 1
        click_y = 0
        while True:
            time.sleep(0.01)
            if keyboard.is_pressed('ctrl') and mouse.is_pressed(button='left'):
                click_x, click_y = mouse.get_position()
                ew_x_pos_spinbox.delete(0, tk.END)
                ew_y_pos_spinbox.delete(0, tk.END)
                ew_x_pos_spinbox.insert(0, click_x)
                ew_y_pos_spinbox.insert(0, click_y)
                break
            else:
                continue

    extra_window = tk.Toplevel()
    extra_window.title('Edit window')

    ew_get_click_position = ttk.Button(extra_window, text="Get Click Position (CTRL+Click)", command=ew_get_click_position_x_y)
    ew_get_click_position.grid(column=2, row=1, rowspan=2, pady=(25, 25), padx=(20, 20))

    save_values_button = ttk.Button(extra_window, text='Save values',
                                    command=lambda: [update_record(), extra_window.destroy()])
    save_values_button.grid(row=10, column=1, pady=(40, 0))

    ttk.Label(extra_window, text="Click/Text ").grid(column=0, row=0, pady=(30, 5))
    # items = ('C', 'T')
    # ew_combobox_value = tk.StringVar(value=items[0])
    combo = ttk.Combobox(extra_window, textvariable=ew_combobox_value)
    combo['values'] = items
    combo.grid(column=1, row=0, pady=(30, 5))

    ttk.Label(extra_window, text="X position: ").grid(column=0, row=1, padx=(10, 10), pady=(0, 5))
    ttk.Label(extra_window, text="Y position: ").grid(column=0, row=2, padx=(10, 10), pady=0)

    ew_x_pos_spinbox = tk.Spinbox(extra_window, from_=0, to=3000)
    ew_x_pos_spinbox.grid(column=1, row=1, padx=(10, 10), pady=(2, 5), ipadx=1)
    ew_y_pos_spinbox = tk.Spinbox(extra_window, from_=0, to=2000)
    ew_y_pos_spinbox.grid(column=1, row=2, padx=(10, 10), pady=(2, 5), ipadx=1)

    ttk.Label(extra_window, text="Right click ").grid(column=0, row=3, pady=(2, 5))
    ttk.Label(extra_window, text="Double click ").grid(column=0, row=4, pady=(2, 5))
    ttk.Label(extra_window, text="Human-like mouse move ").grid(column=0, row=5, pady=(2, 5))

    ew_check_box_right_click_checkbox = ttk.Checkbutton(extra_window, variable=ew_check_box_right_click, onvalue=1,
                                                       offvalue=0)
    ew_check_box_right_click_checkbox.grid(column=1, row=3, padx=(30, 10), pady=(2, 5))

    ew_check_box_double_click_checkbox = ttk.Checkbutton(extra_window, variable=ew_check_box_double_click, onvalue=1,
                                                         offvalue=0)
    ew_check_box_double_click_checkbox.grid(column=1, row=4, padx=(30, 10), pady=(2, 5))

    ew_check_box_h_mouse_movement_checkbox = ttk.Checkbutton(extra_window, variable=ew_check_box_h_mouse_movement,
                                                             onvalue=1, offvalue=0)
    ew_check_box_h_mouse_movement_checkbox.grid(column=1, row=5, padx=(30, 10), pady=(2, 5))

    ttk.Label(extra_window, text="Text: ").grid(column=0, row=6, padx=(10, 10), pady=(20, 5))
    textbox = tk.Text(extra_window, height=2, width=30)
    textbox.grid(column=1, row=6, padx=(10, 10), pady=(20, 5), ipadx=60, ipady=40)

    ttk.Label(extra_window, text="Wait after step [s]: ").grid(column=0, row=9, padx=(30, 10), pady=(2, 5))

    wait_spinbox = tk.Spinbox(extra_window, from_=0, to=600)
    wait_spinbox.grid(column=1, row=9, padx=(10, 10), pady=(2, 5), ipadx=1)
    select_record()


def edit():
    try:
        # Get selected item to Edit
        selected_item = tree.selection()[0]

        print(selected_item)
        create_edit_window()
    except:
        pass


def delete():

    def line_rearrangement():
        global counter

        rearrangement_list_rows = len(tree.get_children())
        rearrangement_list_columns = 9
        rearrangement_list = [[0]*rearrangement_list_columns]*rearrangement_list_rows

        line_counter = 1
        for item in tree.get_children():
            lines = tree.item(item)['values']
            rearrangement_list[line_counter-1] = lines
            if lines[0] != line_counter:
                rearrangement_list[line_counter-1][0] = line_counter

            tree.delete(item)
            tree.insert('', "end", values=rearrangement_list[line_counter-1])
            line_counter += 1
            counter = line_counter


# Get selected item to Delete
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

    line_rearrangement()


def clear_item():

    y_pos_spinbox.delete(0, tk.END)
    y_pos_spinbox.insert(0, "0")
    x_pos_spinbox.delete(0, tk.END)
    x_pos_spinbox.insert(0, "0")
    textbox.delete('1.0', tk.END)
    wait_spinbox_click.delete(0, tk.END)
    wait_spinbox_click.insert(0, "0")
    wait_spinbox_text.delete(0, tk.END)
    wait_spinbox_text.insert(0, "0")
    check_box_right_click.set(0)
    check_box_double_click.set(0)
    check_box_h_mouse_movement.set(0)

def add_item(ct, wait_time):
    global counter
    print(counter, x_pos_spinbox.get())
    print(textbox.get("1.0", 'end-1c'))
    print(type(wait_time.get()))

    record = [counter,
              ct,
              int(x_pos_spinbox.get()) if ct == 'C' else "",
              int(y_pos_spinbox.get()) if ct == 'C' else "",
              'x' if check_box_right_click.get() == 1 and ct == 'C' else "",
              'x' if check_box_double_click.get() == 1 and ct == 'C' else "",
              'x' if check_box_h_mouse_movement.get() == 1 and ct == 'C' else "",
              textbox.get("1.0", 'end-1c') if ct == 'T' else "",
              int(wait_time.get())]

    tree.insert('', "end", values=record)

    clear_item()
    counter = counter + 1

# Get click position



def get_click_position_x_y():
    click_x = 1
    click_y = 0
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('ctrl') and mouse.is_pressed(button='left'):
            click_x, click_y = mouse.get_position()
            x_pos_spinbox.delete(0, tk.END)
            y_pos_spinbox.delete(0, tk.END)
            x_pos_spinbox.insert(0, click_x)
            y_pos_spinbox.insert(0, click_y)
            break
        else:
            continue

def save_sequence():
    save_to_json = []

    save_file_path = filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    for item in tree.get_children():
        lines = tree.item(item)['values']
        print(lines)
        save_to_json.append(lines)
    print(save_to_json, save_to_json[0], save_to_json[0][0])

    json_string = json.dumps(save_to_json, indent=2)
    with open(save_file_path.name, 'w') as f:
        f.write(json_string)

def load_sequence():

    load_file_path = filedialog.askopenfilename()

    with open(load_file_path, 'r') as f:
        json_object = json.loads(f.read())

    for row in tree.get_children():
        tree.delete(row)

    for item in json_object:
        tree.insert('', "end", values=item)

def run_sequence():
    global stop_seq
    stop_seq = False

    def stop_listener():
        global stop_seq

        while True:
            time.sleep(0.1)
            if keyboard.is_pressed('s'):
                stop_seq = True

    t1 = threading.Thread(target=stop_listener)
    t1.start()

    for row in tree.get_children():
        if stop_seq is True:
            print("Stopping sequence due to stop_seq")
            break
        else:
            print(tree.item(row)['values'])
            actual_row = tree.item(row)['values']
            if actual_row[1] == 'C':
                mouse.move(actual_row[2], actual_row[3], duration=1)
                if actual_row[4] == 'x':
                    mouse.click('right')
                elif actual_row[5] == 'x':
                    mouse.double_click('left')
                elif actual_row[5] == 'x':
                    # todo: HLMM resolve conflict of pyautogui or solve it somehow
                    # HLMM to be checked
                    pass
                else:
                    mouse.click('left')
                time.sleep(float(actual_row[8]))
                print("executing click")

            elif actual_row[1] == 'T':
                if actual_row[7] == "enter":
                    keyboard.press("enter")
                # if actual_row[7] == "ctrl":
                #     keyboard.press("ctrl")
                # if actual_row[7] == "shift":
                #     keyboard.press("shift")
                #todo: solve hotkey long presses to enable complete functionality
                else:
                    keyboard.write(actual_row[7])
                time.sleep(float(actual_row[8]))


def run_sequence_countinuously():
    global stop_seq
    stop_seq = False
    while stop_seq is False:
        run_sequence()


stop_seq = False

window = tk.Tk()
window.title("Auto Clicker")

frame = tk.Frame(window)
frame.pack(padx=20, pady=10)

# Menu
menu = tk.Menu(window)

# Sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New file'))
file_menu.add_command(label='Open', command=lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label='File', menu=file_menu)

help_menu = tk.Menu(menu, tearoff=False)
help_check_string = tk.StringVar()
help_menu.add_command(label='Help entry', command=lambda: print(help_check_string.get()))
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)

exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='exercise test 1')
menu.add_cascade(label='Exercise', menu=exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label='some more stuff')
exercise_menu.add_cascade(label='more stuff', menu=exercise_sub_menu)
window.configure(menu=menu)

# Tabs
tabControl = ttk.Notebook(frame)
tabControl.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Add Click')
tabControl.add(tab2, text='Tab Text')
tabControl.add(tab3, text='Add Wait (Inactive tab)')

# TAB 1
ttk.Label(tab1, text="X position: ").grid(column=0, row=0, padx=(10, 10), pady=(20, 5))
ttk.Label(tab1, text="Y position: ").grid(column=0, row=1, padx=(10, 10), pady=0)

x_pos_spinbox = tk.Spinbox(tab1, from_=0, to=3000)
x_pos_spinbox.grid(column=1, row=0, padx=(10, 10), pady=(30, 5), ipadx=5)
y_pos_spinbox = tk.Spinbox(tab1, from_=0, to=2000)
y_pos_spinbox.grid(column=1, row=1, padx=(10, 10), pady=(2, 5), ipadx=5)

get_click_position = ttk.Button(tab1, text="Get Click Position (CTRL+Click)", command=get_click_position_x_y)
get_click_position.grid(column=3, row=0, rowspan=2, columnspan=3, pady=(25, 0), padx=(8, 8), ipadx=80, ipady=10)

ttk.Label(tab1, text="Right click ").grid(column=0, row=2, pady=(2, 5))
ttk.Label(tab1, text="Double click ").grid(column=0, row=3, pady=(2, 5))
ttk.Label(tab1, text="Human-like mouse move ").grid(column=0, row=4, pady=(2, 5))

# check_box_right_click_value = tk.IntVar()
# check_box_right_click=ttk.Checkbutton(tab1, onvalue=1, offvalue=0,variable=check_box_right_click_value).grid(column=1, row=2,padx=(30,10), pady=(2, 5))
#
check_box_right_click = tkinter.IntVar()
check_box_right_click_checkbox = ttk.Checkbutton(tab1, variable=check_box_right_click, onvalue=1, offvalue=0)
check_box_right_click_checkbox.grid(column=1, row=2, padx=(30, 10), pady=(2, 5))

check_box_double_click = tkinter.IntVar()
check_box_double_click_checkbox = ttk.Checkbutton(tab1, variable=check_box_double_click, onvalue=1, offvalue=0)
check_box_double_click_checkbox.grid(column=1, row=3, padx=(30, 10), pady=(2, 5))

check_box_h_mouse_movement = tkinter.IntVar()
check_box_h_mouse_movement_checkbox = ttk.Checkbutton(tab1, variable=check_box_h_mouse_movement, onvalue=1, offvalue=0)
check_box_h_mouse_movement_checkbox.grid(column=1, row=4, padx=(30, 10), pady=(2, 5))

ttk.Label(tab1, text="Wait after step [s]: ").grid(column=0, row=5, padx=(30, 10), pady=(2, 5))
wait_spinbox_click = tk.Spinbox(tab1, from_=0, to=600)
wait_spinbox_click.grid(column=1, row=5, padx=(10, 10), pady=(2, 5), ipadx=5)

add_click = ttk.Button(tab1, text="ADD", command=lambda: add_item("C", wait_spinbox_click))
add_click.grid(column=3, row=2, rowspan=4, columnspan=3, padx=(10, 10), pady=(5, 15), ipadx=130, ipady=68)
# TAB 2
ttk.Label(tab2, text="Text: ").grid(column=0, row=0, padx=(10, 10), pady=(20, 5))
textbox = tk.Text(tab2, height=2, width=30)
textbox.grid(column=1, row=0, padx=(10, 10), pady=(20, 5), ipadx=100, ipady=45)

ttk.Label(tab2, text="Wait after step [s]: ").grid(column=0, row=2, padx=(30, 10), pady=(2, 5))
wait_spinbox_text = tk.Spinbox(tab2, from_=0, to=600)
wait_spinbox_text.grid(column=1, row=2, padx=(10, 10), pady=(2, 5), ipadx=5)

add_text = ttk.Button(tab2, text="ADD", command=lambda: add_item("T", wait_spinbox_text)).grid(column=0, row=3,
                                                                                               columnspan=4,
                                                                                               padx=(40, 40),
                                                                                               pady=(5, 15), ipadx=260,
                                                                                               ipady=10)

# TAB 3
ttk.Label(tab3, text="Wait after step [s]: ").grid(column=0, row=0, padx=(30, 10), pady=(100, 30))
wait_spinbox_wait = tk.Spinbox(tab3, from_=0, to=600).grid(column=1, row=0, padx=(10, 10), pady=(100, 30), ipadx=5)
add_wait = ttk.Button(tab3, text="ADD").grid(column=0, row=1, columnspan=4, padx=(40, 40), pady=(5, 15), ipadx=260,
                                             ipady=10)

#todo: add result processing tab and lines

# Table / Treeview

columns = ('line', 'C/T', 'X pos', 'Y pos', "Right Click", "Double click", "Hl mouse movement", "Text", "Wait")
tree = ttk.Treeview(frame, columns=columns, show="headings")

tree.tag_configure('ttk', background='yellow')
tree.heading('line', text='Line')
tree.column('line', minwidth=0, width=40, anchor=tk.CENTER)
tree.heading('C/T', text='Click/Text')
tree.column('C/T', minwidth=0, width=90, anchor=tk.CENTER)
tree.heading('X pos', text='X pos')
tree.column('X pos', minwidth=0, width=55, anchor=tk.CENTER)
tree.heading('Y pos', text="Y pos")
tree.column('Y pos', minwidth=0, width=55, anchor=tk.CENTER)
tree.heading('Right Click', text="Right Click")
tree.column('Right Click', minwidth=0, width=85, anchor=tk.CENTER)
tree.heading('Double click', text="Double click")
tree.column('Double click', minwidth=0, width=110, anchor=tk.CENTER)
tree.heading('Hl mouse movement', text="HLMM")
tree.column('Hl mouse movement', minwidth=0, width=80, anchor=tk.CENTER)
tree.heading('Text', text="Text")
tree.column('Text', minwidth=0, width=280, anchor=tk.CENTER)
tree.heading('Wait', text="Wait [s]")
tree.column('Wait', minwidth=0, width=50, anchor=tk.CENTER)
tree.grid(row=1, column=0, columnspan=3, padx=30, pady=10)



# Buttons
save_sequence_button = tk.Button(frame, text="Save sequence", command=save_sequence)
save_sequence_button.grid(row=3, column=0, columnspan=3, sticky="news", padx=20, pady=7)
load_sequence_button = tk.Button(frame, text="Load sequence", command=load_sequence)
load_sequence_button.grid(row=4, column=0, columnspan=3, sticky="news", padx=20, pady=7)
run_sequence_button = tk.Button(frame, text="RUN SEQUENCE", bg="#5cc41e", command=run_sequence)
run_sequence_button.grid(row=5, column=0, columnspan=3, sticky="news", padx=20, pady=5, ipady=10)
run_sequence_continuously_button = tk.Button(frame, text="RUN SEQUENCE CONTINUOUSLY", bg="#03AC13", command=run_sequence_countinuously)
run_sequence_continuously_button.grid(row=6, column=0,columnspan=2, sticky="news", padx=20, pady=5, ipadx=5, ipady=5)
stop_sequence_button = tk.Button(frame, text="STOP SEQUENCE  (Press S)", bg="#FF0000")
stop_sequence_button.grid(row=6, column=2, columnspan=2, sticky="news", padx=20, pady=5, ipadx=130, ipady=5)

edit_btn = ttk.Button(frame, text="Edit", command=edit)
edit_btn.grid(row=2, column=0, columnspan=1, padx=5, pady=10)
del_btn = ttk.Button(frame, text="Delete", command=delete)
del_btn.grid(row=2, column=2, columnspan=1, padx=5, pady=10)

# extra window
ew_counter = 0
items = ('C', 'T')
ew_combobox_value = tk.StringVar(value=items[0])

ew_check_box_right_click = tk.BooleanVar(value=False)
ew_check_box_double_click = tk.BooleanVar(value=False)
ew_check_box_h_mouse_movement = tk.BooleanVar(value=False)

tree.bind('<<TreeviewSelect>>', item_select)

window.mainloop()
