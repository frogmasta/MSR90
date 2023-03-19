# ==========================================
# Title:  msr90.py
# Author: Eric Roth
# Date:   March 14th, 2023
# ==========================================

import usb.core
import usb.util

from hid_converter import hid_buf_to_keypresses

# -------------------------------------------------------------------------------
# CONSTANTS
# -------------------------------------------------------------------------------

VID = 0xc216
PID = 0x0180

# -------------------------------------------------------------------------------
# FUNCTIONALITY
# -------------------------------------------------------------------------------
class MSR90:
    def __init__(self) -> None:
        self.device = None
        self.cfg = None
        self.interface = None
        self.endpoint = None

    def __str__(self) -> str:
        return self.device.__str__()

    def __repr__(self) -> str:
        return self.device.__repr__()
    
    def find_device(self) -> bool:
        self.device = usb.core.find(idVendor=VID, idProduct=PID)

        if self.device is None:
            print("Failed to find MSR90...")
            return False
        
        self.device.set_configuration()
        self.cfg = self.device.get_active_configuration()
        self.interface = self.cfg[(0, 0)]
        self.endpoint = self.interface[0]

        print("Found MSR90!")

        return True
    
    def read_card(self, timeout=10000) -> str:
        buf = []
        output = ""
        try:
            buf += self.device.read(self.endpoint, 8, timeout)
            output += hid_buf_to_keypresses(buf)
            buf = []
        except usb.core.USBTimeoutError:
            raise TimeoutError # Abstract away the pyUSB

        while True:
            try:
                buf += self.device.read(self.endpoint, 8, 1000)
                output += hid_buf_to_keypresses(buf)
                buf = []
            except usb.core.USBTimeoutError:
                break
        
        return output
