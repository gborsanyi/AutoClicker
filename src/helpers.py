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


class AutoClickerHelpers:

    def __init__(self, app):
        self.app = app


    def item_select(self):
        print(self.app.tree.selection(), type(self.app.tree.selection()))
        for i in self.app.tree.selection():
            print(self.app.tree.item(i)['values'])

    def create_edit_window(self):

        def select_record():
            global ew_counter
            # select row
            selected = self.app.tree.focus()
            values = self.app.tree.item(selected, 'values')

            # delete all values before editing them
            ew_x_pos_spinbox.delete(0, tk.END)
            ew_y_pos_spinbox.delete(0, tk.END)
            combo.delete(0, tk.END)
            wait_spinbox.delete(0, tk.END)
            textbox.delete(tk.END, tk.END)
            self.app.ew_check_box_right_click.set(False)
            self.app.ew_check_box_double_click.set(False)
            self.app.ew_check_box_h_mouse_movement.set(False)

            # import all values from selected row
            ew_counter = values[0]
            combo.insert(0, values[1])
            ew_x_pos_spinbox.insert(0, values[2])
            ew_y_pos_spinbox.insert(0, values[3])
            self.app.ew_check_box_right_click.set(True if values[4] == "x" else False)
            self.app.ew_check_box_double_click.set(True if values[5] == "x" else False)
            self.app.ew_check_box_h_mouse_movement.set(True if values[6] == "x" else False)
            textbox.insert(1.0, values[7])
            wait_spinbox.insert(0, values[8])

        def update_record():
            selected = self.app.tree.focus()

            ew_record = [ew_counter,
                         combo.get(),
                         int(ew_x_pos_spinbox.get()) if combo.get() == 'C' else "",
                         int(ew_y_pos_spinbox.get()) if combo.get() == 'C' else "",
                         'x' if self.app.ew_check_box_right_click.get() is True and combo.get() == 'C' else "",
                         'x' if self.app.ew_check_box_double_click.get() is True and combo.get() == 'C' else "",
                         'x' if self.app.ew_check_box_h_mouse_movement.get() is True and combo.get() == 'C' else "",
                         textbox.get("1.0", 'end-1c') if combo.get() == 'T' else "",
                         int(wait_spinbox.get())]



            self.app.tree.item(selected, text="", values=ew_record)

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
        combo = ttk.Combobox(extra_window, textvariable=self.app.ew_combobox_value)
        combo['values'] = self.app.items
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

        ew_check_box_right_click_checkbox = ttk.Checkbutton(extra_window, variable=self.app.ew_check_box_right_click, onvalue=1,
                                                           offvalue=0)
        ew_check_box_right_click_checkbox.grid(column=1, row=3, padx=(30, 10), pady=(2, 5))

        ew_check_box_double_click_checkbox = ttk.Checkbutton(extra_window, variable=self.app.ew_check_box_double_click, onvalue=1,
                                                             offvalue=0)
        ew_check_box_double_click_checkbox.grid(column=1, row=4, padx=(30, 10), pady=(2, 5))

        ew_check_box_h_mouse_movement_checkbox = ttk.Checkbutton(extra_window, variable=self.app.ew_check_box_h_mouse_movement,
                                                                 onvalue=1, offvalue=0)
        ew_check_box_h_mouse_movement_checkbox.grid(column=1, row=5, padx=(30, 10), pady=(2, 5))

        ttk.Label(extra_window, text="Text: ").grid(column=0, row=6, padx=(10, 10), pady=(20, 5))
        textbox = tk.Text(extra_window, height=2, width=30)
        textbox.grid(column=1, row=6, padx=(10, 10), pady=(20, 5), ipadx=60, ipady=40)

        ttk.Label(extra_window, text="Wait after step [s]: ").grid(column=0, row=9, padx=(30, 10), pady=(2, 5))

        wait_spinbox = tk.Spinbox(extra_window, from_=0, to=600)
        wait_spinbox.grid(column=1, row=9, padx=(10, 10), pady=(2, 5), ipadx=1)
        select_record()


    def edit(self):
        try:
            # Get selected item to Edit
            selected_item = self.app.tree.selection()[0]

            print(selected_item)
            self.create_edit_window()
        except:
            pass


    def delete(self):

        def line_rearrangement():
            global counter

            rearrangement_list_rows = len(self.app.tree.get_children())
            rearrangement_list_columns = 9
            rearrangement_list = [[0]*rearrangement_list_columns]*rearrangement_list_rows

            line_counter = 1
            for item in self.app.tree.get_children():
                lines = self.app.tree.item(item)['values']
                rearrangement_list[line_counter-1] = lines
                if lines[0] != line_counter:
                    rearrangement_list[line_counter-1][0] = line_counter

                self.app.tree.delete(item)
                self.app.tree.insert('', "end", values=rearrangement_list[line_counter-1])
                line_counter += 1
                counter = line_counter


    # Get selected item to Delete
        selected_item = self.app.tree.selection()[0]
        self.app.tree.delete(selected_item)

        line_rearrangement()


    def clear_item(self):

        self.app.y_pos_spinbox.delete(0, tk.END)
        self.app.y_pos_spinbox.insert(0, "0")
        self.app.x_pos_spinbox.delete(0, tk.END)
        self.app.x_pos_spinbox.insert(0, "0")
        self.app.textbox.delete('1.0', tk.END)
        self.app.wait_spinbox_click.delete(0, tk.END)
        self.app.wait_spinbox_click.insert(0, "0")
        self.app.wait_spinbox_text.delete(0, tk.END)
        self.app.wait_spinbox_text.insert(0, "0")
        self.app.check_box_right_click.set(0)
        self.app.check_box_double_click.set(0)
        self.app.check_box_h_mouse_movement.set(0)

    def add_item(self, ct, wait_time):

        print(self.app.counter, self.app.x_pos_spinbox.get())
        print(self.app.textbox.get("1.0", 'end-1c'))
        print(type(wait_time.get()))

        record = [self.app.counter,
                  ct,
                  int(self.app.x_pos_spinbox.get()) if ct == 'C' else "",
                  int(self.app.y_pos_spinbox.get()) if ct == 'C' else "",
                  'x' if self.app.check_box_right_click.get() == 1 and ct == 'C' else "",
                  'x' if self.app.check_box_double_click.get() == 1 and ct == 'C' else "",
                  'x' if self.app.check_box_h_mouse_movement.get() == 1 and ct == 'C' else "",
                  self.app.textbox.get("1.0", 'end-1c') if ct == 'T' else "",
                  int(wait_time.get())]

        self.app.tree.insert('', "end", values=record)

        self.clear_item()
        self.app.counter = self.app.counter + 1

    # Get click position
    def get_click_position_x_y(self):
        click_x = 1
        click_y = 0
        while True:
            time.sleep(0.01)
            if keyboard.is_pressed('ctrl') and mouse.is_pressed(button='left'):
                click_x, click_y = mouse.get_position()
                self.app.x_pos_spinbox.delete(0, tk.END)
                self.app.y_pos_spinbox.delete(0, tk.END)
                self.app.x_pos_spinbox.insert(0, click_x)
                self.app.y_pos_spinbox.insert(0, click_y)
                break
            else:
                continue

    def save_sequence(self):
        save_to_json = []

        save_file_path = filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON files", "*.json")])

        for item in self.app.tree.get_children():
            lines = self.app.tree.item(item)['values']
            print(lines)
            save_to_json.append(lines)
        print(save_to_json, save_to_json[0], save_to_json[0][0])

        json_string = json.dumps(save_to_json, indent=2)
        with open(save_file_path.name, 'w') as f:
            f.write(json_string)

    def load_sequence(self):

        load_file_path = filedialog.askopenfilename()

        with open(load_file_path, 'r') as f:
            json_object = json.loads(f.read())

        for row in self.app.tree.get_children():
            self.app.tree.delete(row)

        for item in json_object:
            self.app.tree.insert('', "end", values=item)

    def run_sequence(self):
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

        for row in self.app.tree.get_children():
            if stop_seq is True:
                print("Stopping sequence due to stop_seq")
                break
            else:
                print(self.app.tree.item(row)['values'])
                actual_row = self.app.tree.item(row)['values']
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


    def run_sequence_countinuously(self):
        global stop_seq
        stop_seq = False
        while stop_seq is False:
            self.run_sequence()
