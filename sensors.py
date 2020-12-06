import machine
import onewire
import utime
import ds18x20


from machine import I2C, Pin
from bh1750 import BH1750  # Light Sensor
from bmp180 import BMP180  # Pressure, Humidity, etc. Sensor
from ccs811 import CCS811  # Environmetal sensor

bus = I2C(scl=Pin(23), sda=Pin(19), freq=100000)


def read_ds18b20(self):

    sensor_wire = onewire.OneWire(machine.Pin(5))
    temperature_sensor = ds18x20.DS18X20(sensor_wire)

    sensor_address = temperature_sensor.scan().pop()
    temperature_sensor.convert_temp()

    utime.sleep_ms(500)

    celcius = temperature_sensor.read_temp(sensor_address)
    fahrenheit = (celcius * 1.8) + 32

    return fahrenheit, celcius


def read_bh1750():

    sensor = BH1750(bus)

    return sensor.luminance(BH1750.ONCE_HIRES_1)
