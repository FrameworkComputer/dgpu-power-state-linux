# dgpu-power-state-linux
A simple pyudev script to detect if the dGPU is in low power state or not for the Framework Laptop 16; with dGPU attached.

## Considerations

- You need to pip install pyudev.
- Card 1 is assumed to be dGPU, card 2 is assumed to be UMA...change to meet your own needs.
(This can be edited into whatever you like, see below for section you can tweak to meet your needs - but uneeded for Framework Laptop 16 with dGPU.)
```
context = Context()
for device in context.list_devices(subsystem='drm', DEVTYPE='drm_minor'):
    # Attempt to dynamically determine which DRM devices correspond to UMA and dGPU
    if 'card1' in device.sys_path:
        cards['dGPU'] = device.sys_path.split('/')[-1]
    elif 'card2' in device.sys_path:
        cards['UMA'] = device.sys_path.split('/')[-1]
```

- Data pulled from /sys/class/drm/ giving us event specific driven data.

## Features

- Lists power control as On/Off/Auto.
- Vendor/Device data.
- uevent driver.
- Time suspended and active.

## Requirements

### Fedora

```
sudo dnf install git pip -y && pip install pyudev
```

### Ubuntu LTS

```
sudo apt update && sudo apt install git pip -y && pip install pyudev
```

#### Run the script in a terminal as follows

```
git clone https://github.com/FrameworkComputer/dgpu-power-state-linux.git && cd dgpu-power-state-linux && python3 gpu-power-state.py
```

![Power state for dGPU](https://raw.githubusercontent.com/FrameworkComputer/dgpu-power-state-linux/main/dgpu-uma.png "Power state for dGPU")
