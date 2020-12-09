import esp
import esp32

"""
ESP32 board related functions.
"""


def get_flash():
    """
    get_flash: Reads the on-board Flash memory

    Returns:
        float: On-Board Flash memory in kilobytes
    """

    return esp.flash_size() / 1000


def get_cpu_temperature():
    """
    get_cpu_temperature: Reads the CPU raw temperature

    Returns:
        int: CPU temperature in Fahrenheit
    """

    # Returns internal MCU temperature in Fahrenheit

    return esp32.raw_temperature()


def vendor_debug_off():
    """
    vendor_debug_off: Turns off vendor debugging messages
    """

    esp.osdebug(None)
