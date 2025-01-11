import pyautogui
import time
import random
from PIL import ImageGrab

# Define the coordinates (replace with your own values that you find through the find_coordinates script)
layouts_button = (956, 442)  # Coordinates of the "Layouts" button
layout_2_button = (1105, 498)  # Coordinates of the "Layout 2" button or whatever layout you want to use
rebirth_button = (836,594)  # Coordinates of the "Rebirth" button
yes_button = (831, 607) # Coordinates of the "Yes" button after pressing the "Rebirth" button
color_check_region = (795, 595, 800, 600)  # Region of the rebirth GUI to check color (x1, y1, x2, y2)

# Function to detect color change in the rebirth GUI
def is_rebirth_ready(target_color, tolerance=10):
    screenshot = ImageGrab.grab(bbox=color_check_region)
    pixels = screenshot.load()

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            # Handle RGB or RGBA formats
            pixel = pixels[x, y]
            if len(pixel) == 4:  # If RGBA, ignore the alpha channel
                r, g, b, _ = pixel
            else:  # Assume RGB
                r, g, b = pixel

            tr, tg, tb = target_color

            # Check if the color is within the tolerance range
            if (
                abs(r - tr) <= tolerance
                and abs(g - tg) <= tolerance
                and abs(b - tb) <= tolerance
            ):
                return True
    return False

# Main macro loop
print("Starting in 5 seconds.")
time.sleep(5)

try:
    while True:
        # Step 1: Press 'C' to open the menu
        pyautogui.press('c')
        time.sleep(0.3)  # Wait for the menu to load
        # Step 2: Click the "Layouts" button
        pyautogui.click(layouts_button)
        time.sleep(0.4)
        # Step 3: Click the "Load Layout 2" button
        pyautogui.click(layout_2_button)
        time.sleep(1)  # Wait for the layout to load
        # Step 4: Press 'M' to open the rebirth GUI
        pyautogui.press('m')
        time.sleep(10) # Adjust if you have a fast setup
        # Step 5: Wait for the color change in the rebirth GUI
        target_color = (125, 251, 127)  # Replace with the RGB value of the color when rebirth is ready
        while not is_rebirth_ready(target_color,10):
            time.sleep(0.1)  # Change if you want to lessen lag
        if(random.randint(1,20)==15):
            time.sleep(30)
        # Step 6: Click the "Rebirth" button
        pyautogui.click(rebirth_button)
        time.sleep(0.1)
        pyautogui.click(yes_button)
        time.sleep(0.6)  # Wait for the rebirth process to complete
except KeyboardInterrupt:
    print("\nMacro stopped!")
