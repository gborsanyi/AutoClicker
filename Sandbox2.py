import pyautogui
import keyboard

from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse button {button} was clicked at ({x}, {y})")

# Create a listener for mouse events
listener = mouse.Listener(on_click=on_click)

# Start listening for mouse events
listener.start()

# Keep the program running
listener.join()
