# Miners Haven Rebirth Macro

A Python script to automate repetitive rebirth tasks in the Roblox game **Miners Haven**. This script uses image recognition and keyboard/mouse automation to interact with the game. It can automatically load layouts, detect rebirth readiness, and perform rebirths. The macro runs in a loop until you terminate the process.

---

## Features
- Opens menus and clicks buttons to load specific layouts.
- Detects color changes in the rebirth GUI to determine when rebirth is ready.
- Performs rebirths automatically in a loop.

---

## Requirements

### System Requirements
- **Operating System**: macOS or Windows
- **Python Version**: Python 3.8 or later

### Python Libraries
- `pyautogui` (Mouse and keyboard automation)
- `pillow` (Image processing)

---

## Setup

### 1. Clone the Repository
```bash
# Clone the GitHub repository
git clone https://github.com/wittenpan/miners-haven-rebirth.git
cd miners-haven-rebirth
```

### 2. Create a Virtual Environment
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Script
Edit the `main.py` file to update the following:
- **Coordinates**: Replace the button coordinates with the values that match your screen resolution. To do this, you may run the find_coordinates.py script and press enter to log coordinates. 
  ```python
  layouts_button = (500, 400)  # Replace with your "Layouts" button coordinates
  layout_2_button = (550, 450)  # Replace with your "Load Layout 2" button coordinates
  rebirth_button = (600, 500)  # Replace with your "Rebirth" button coordinates
  color_check_region = (795, 595, 800, 600)  # Replace with the region of the rebirth GUI to check
  ```
- **Target Color**: Update the `target_color` with the RGB values of the "rebirth ready" indicator in the GUI.
  ```python
  target_color = (125, 251, 127)  # Replace with the RGB color for rebirth readiness, although it should be the same theoretically. Check to make sure.
  ```

---

## Usage

### 1. Run the Macro
Run the script:
```bash
python main.py
```

---

## Troubleshooting

1. **Image Recognition Not Working**:
   - Ensure the `color_check_region` is correct for your screen resolution.
   - Increase the `tolerance` value in the `is_rebirth_ready` function.

2. **Dependencies Not Installed**:
   - Verify your virtual environment is active.
   - Run `pip install -r requirements.txt` again.

3. **Script Stops Unexpectedly**:
   - Adjust `time.sleep` durations if the game menus are loading slowly.
   - Make sure your computer does not sleep.

---

## Contributing
Feel free to submit issues or contribute to the project by opening a pull request. There are some issues currently, like the human error component. To make it more realistic, you can add random times where the player places a couple of things e.g. champion infuser and infusers. However, all contributions are welcome!

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Disclaimer
This script is provided for educational purposes only. Use it responsibly and ensure compliance with the game’s terms of service.

