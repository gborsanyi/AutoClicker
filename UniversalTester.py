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

from src.widgets_init import AutoClickerApp

counter = 1
print(counter)

stop_seq = False


def main():
    counter = 1
    print(counter)
    stop_seq = False

    window = tk.Tk()
    window.title("Auto Clicker")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=10)

    app = AutoClickerApp(window, frame, stop_seq, counter)
    app.create_gui()

    window.mainloop()

if __name__ == "__main__":
    main()