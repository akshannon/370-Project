'''
HOW TO INSTALL ON PI

Install Python headers and evdev
> sudo apt install python3-dev
> pip install evdev

Add yourself to the input group
> sudo usermod -aG input $USER

Log out and back in, then verify
> groups  # should show "input"

'''

# find button with cat /proc/bus/input/devices


import evdev
import subprocess

def find_button_device(name_hint=None):
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(f"  {device.path}: {device.name}")
        if name_hint and name_hint.lower() in device.name.lower():
            return device
    return None

def on_button_press():
    global current_process

    # Kill the old process if it's still running
    if current_process is not None and current_process.poll() is None:
        current_process.terminate()
        current_process.wait()  # ensure it's fully stopped before starting new one

    print("Button pressed!")
    current_process = subprocess.Popen(["python3", "Engine.py"])

def main():
    print("Available input devices:")
    device = find_button_device()  # pass a name hint if needed

    if device is None:
        print("Device not found.")
        return

    print(f"\nListening on: {device.name} ({device.path})")

    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            on_button_press()

if __name__ == "__main__":
    main()