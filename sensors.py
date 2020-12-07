import utime
import machine
import onewire

from machine import I2C, Pin

# TODO
# Group Sensors into classes, particularly I2C sensors

ic2bus = I2C(scl=Pin(23), sda=Pin(19), freq=100000)


def get_temperature(pin):

    try:

        import ds18x20

    except ImportError:

        return 'Unable to import DS18x20 library.'

    else:

        sensor_wire = onewire.OneWire(machine.Pin(pin))
        temperature_sensor = ds18x20.DS18X20(sensor_wire)

        try:

            sensor_address = temperature_sensor.scan().pop()

        except IndexError:

            return 'Check sensor. Unable to get sensor address.'

        else:

            temperature_sensor.convert_temp()

            utime.sleep_ms(500)

            celcius = temperature_sensor.read_temp(sensor_address)
            fahrenheit = (celcius * 1.8) + 32

            return fahrenheit, celcius


def bh1750():

    try:

        from bh1750 import BH1750

        sensor = BH1750(ic2bus)

        return sensor.luminance(BH1750.ONCE_HIRES_1)

    except ImportError:

        return ImportError('Sensor library not found.')
