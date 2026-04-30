import evdev
import subprocess

current_process = None

def on_button_press():
    global current_process

    # If Engine.py is still running from a previous press, stop it before starting a new one
    if current_process is not None and current_process.poll() is None:
        current_process.terminate()
        current_process.wait()  

    print("Button pressed!")

    current_process = subprocess.Popen(["python3", "Engine.py"])

def main():
    # Connect to the USB button which registers as a keyboard on event2
    device = evdev.InputDevice('/dev/input/event2')
    print(f"Listening on: {device.name} ({device.path})")

    # Continuously listen for input events
    for event in device.read_loop():
        # Only trigger on key press 
        if event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_A and event.value == 1:
            on_button_press()

if __name__ == "__main__":
    main()
    