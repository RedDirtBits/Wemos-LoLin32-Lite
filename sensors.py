import utime
import machine
import onewire

from machine import I2C, Pin

# TODO
# Group Sensors into classes, particularly I2C sensors


class I2CSensors:

    """
    A simple class that defines and sets up the I2C bus.
    """

    def __init__(self, scl, sda, freq=100000):

        self.scl = scl
        self.sda = sda
        self.freq = freq
        self.i2cbus = I2C(scl=Pin(self.scl), sda=Pin(self.sda), freq=self.freq)

    def bmp180(self):
        """
        Get data from BMP180 Temperature, Pressure and Altitude sensor

        :param:     None
        :return:    Tuple, Temerature in Fahrenheit, Celcius.  Pressure in hPa and inHg
                    Altitude in meters and feet
        """

        from bmp180 import BMP180

        bus = self.i2cbus
        bmp180 = BMP180(bus)
        bmp180.oversample_sett = 2
        bmp180.baseline = 101325

        temperature_c = round(bmp180.temperature, 2)
        temperature_f = round((temperature_c * 1.8) + 32, 2)
        pressure_hpa = bmp180.pressure
        pressure_inhg = round(pressure_hpa * 0.0002953, 2)
        altitude_meters = bmp180.altitude
        altitude_feet = round(altitude_meters * 3.2808, 2)

        return temperature_c, temperature_f, pressure_hpa, pressure_inhg, altitude_meters, altitude_feet

    def bme280(self):

        from bme280 import BME280

        bus = self.i2cbus
        bme280 = BME280(i2c=bus)

        temperature_c = round(bme280.temperature, 2)
        temperature_f = round((temperature_c * 1.8) + 32, 2)
        pressure = bme280.pressure
        humidity_percent = bme280.humidity

        return temperature_c, temperature_f, pressure, humidity_percent


def get_temperature(pin):
    """
    Get temperature reading from DS18B20 temperature sensor

    :param pin:     An integer value representing the pin the sensor signal wire is connected to
    :return:        Tuple contain the temperature in Fahrenheit and Celcius
    """

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
    """
    Get light level reading from DS18B20 temperature sensor
    :param: None
    :return: light levels in lumens
    """

    try:

        from bh1750 import BH1750

        sensor = BH1750(ic2bus)

        return sensor.luminance(BH1750.ONCE_HIRES_1)

    except ImportError:

        return ImportError('Sensor library not found.')


def read_bmp180():
    """
     Function to read externally connected BMP180 Temperature,
     Barometric Pressure and Altitude sensor

    Returns:
        tuple: Temperature in Celcius, Altitude in Meters and,
        Pressure in Pascals
    """
    from bmp180 import BMP180

    bus = I2C(scl=Pin(23), sda=Pin(19), freq=100000)
    bmp180 = BMP180(bus)
    bmp180.oversample_sett = 2
    bmp180.baseline = 101325

    temperature = bmp180.temperature
    pressure = bmp180.pressure
    altitude = bmp180.altitude

    return temperature, pressure, altitude
