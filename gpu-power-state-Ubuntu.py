import os
import time
from pyudev import Context

# Define a dictionary to hold our cards' sysfs paths, dynamically discovered
cards = {}

context = Context()
for device in context.list_devices(subsystem='drm', DEVTYPE='drm_minor'):
    # Attempt to dynamically determine which DRM devices correspond to UMA and dGPU
    if 'card0' in device.sys_path:
        cards['dGPU'] = device.sys_path.split('/')[-1]
    elif 'card1' in device.sys_path:
        cards['UMA'] = device.sys_path.split('/')[-1]

# List of attributes to monitor within the device's directory
attributes = [
    "vendor", "device", "uevent", "modalias",
    "power/runtime_status", "power/control", "power/runtime_suspended_time", "power/runtime_active_time",
]

def read_attribute(card_sys_path, attribute):
    try:
        with open(f"/sys/class/drm/{card_sys_path}/device/{attribute}", 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "Not Found"

def print_attribute(attribute, value, red=False):
    RED_START = "\033[91m"
    RED_END = "\033[0m"
    if red:
        print(f"{RED_START}{attribute}: {value}{RED_END}")
    else:
        print(f"{attribute}: {value}")

def clear_screen():
    # Clears the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()  # Clear the screen at the beginning of each iteration
    for name, card_sys_path in cards.items():
        print(f"Checking attributes for {name}:")
        for attribute in attributes:
            value = read_attribute(card_sys_path, attribute)
            if attribute == "power/runtime_status":
                print_attribute(attribute, value, red=True)
            else:
                print_attribute(attribute, value)
        print("-" * 40)
    time.sleep(10)
