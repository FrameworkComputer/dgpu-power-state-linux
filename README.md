# dgpu-power-state-linux
A simple pyudev script to detect if the dGPU is in low power state or not for the Framework Laptop 16; with dGPU attached.

## Considerations

- You need to pip install pyudev.
- Card 1 is assumed to be dGPU, card2 is assumed to be UMA...change to meet your own needs.
- Data pulled from /sys/class/drm/ giving us event specific driven data.

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
