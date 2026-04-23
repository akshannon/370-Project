import usb

# find our device
dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()


import pynput.keyboard