import pyautogui
print("Hover over the button and press Ctrl+C to stop...")
try:
    while True:
        print(pyautogui.position(), end="\r")
except KeyboardInterrupt:
    print("\nStopped!")