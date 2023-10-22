import pyautogui
import random
import time

# Define the screen dimensions
screen_width, screen_height = pyautogui.size()

# Define the number of mouse movements
num_movements = 10

# Define the speed of mouse movement
movement_speed = 0.5  # Adjust this value as needed


# Function to simulate human-like mouse movement
def human_like_mouse_movement():
    for _ in range(num_movements):
        # Generate random coordinates within the screen boundaries
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse cursor to the random position
        pyautogui.moveTo(x, y, duration=movement_speed)

        # Pause for a random short duration to mimic human pauses
        time.sleep(random.uniform(0.1, 0.5))


# Move the mouse in a human-like way
human_like_mouse_movement()
