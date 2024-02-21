__author__ = "Ib Helmer Nielsen"
__copyright__ = "Copyright 2024, IT-Tek"
__credits__ = ["DonskyTech"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IHN"
__email__ = "ihn@ihn.dk"
__status__ = "Development"
# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin, I2C  # ESP32 hardware
import utime                  # Time lib
import network                # Network lib

SSID = "IHN-AP"
PW = "MaaGodt*7913"

ap = network.WLAN(network.AP_IF)     # Opretter en access point interface
ap.active(True)                      # Aktiverer interface
ap.config(essid=SSID, password=PW)   # Sætter SSID og adgangskode
while ap.active() == False:          # Vent til ap aktiv
    pass
print("Ap aktiv !!")                 # Debugging besked

    