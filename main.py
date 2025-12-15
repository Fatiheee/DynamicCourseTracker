import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Onboard LED for ESP32

led.off()  # Turn off LED initially
led.on()   # Turn on LED to indicate script is running