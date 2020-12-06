import esp
import esp32

"""
ESP32 board related functions.
"""


def get_flash():

    # Returns the on-board flash size in KB

    return esp.flash_size() / 1000


def get_cpu_temperature():

    # Returns internal MCU temperature in Fahrenheit

    return esp32.raw_temperature()
