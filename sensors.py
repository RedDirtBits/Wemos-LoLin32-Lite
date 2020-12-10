import utime
import machine
import onewire

from machine import I2C, Pin


class I2CSensors:

    """
    A simple class that defines and sets up the I2C bus.
    """

    def __init__(self, scl, sda, freq=100000):

        self.scl = scl
        self.sda = sda
        self.freq = freq
        self.i2cbus = I2C(scl=Pin(self.scl), sda=Pin(self.sda), freq=self.freq)

    def scan_i2c(self):
        """
        scan_i2c: Scans the I2C bus for any connected devices

        Returns:
            dictionary: Device number, Decimal Address, Hexidecimal Address
        """

        bus = self.i2cbus
        devices = bus.scan()

        device_list = {}

        if len(devices) == 0:

            return 'No I2C devices found.'

        else:

            for number, device in enumerate(devices):

                # device_info = {'Device No.': number + 1, 'Dec. Address': device, 'Hex Address': hex(device)}

                device_info = {
                    number: {'Dec. Address': device, 'Hex Address': hex(device)}}

                device_list.update(device_info)

        return device_list

    def bmp180(self):
        """
        Get data from BMP180 Temperature, Pressure and Altitude sensor

        :param:     None
        :return:    Tuple, Temerature in Fahrenheit, Celcius.  Pressure in hPa and inHg
                    Altitude in meters and feet
        """

        try:

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

        except ImportError:

            return ' BMP180 sensor library not found'

    def bme280(self):

        try:

            from bme280 import BME280

            bus = self.i2cbus
            bme280 = BME280(i2c=bus)

            temperature_c = round(bme280.temperature, 2)
            temperature_f = round((temperature_c * 1.8) + 32, 2)
            pressure = bme280.pressure
            humidity_percent = bme280.humidity

            return temperature_c, temperature_f, pressure, humidity_percent

        except ImportError:

            return 'BME280 sensor library not found'

        except OSError:

            return 'BME280 does not exist'

    def bh1750(self):

        try:

            from bh1750 import BH1750

            bus = self.i2cbus
            bh1750 = BH1750(bus)

            return bh1750.luminance(BH1750.ONCE_HIRES_1)

        except ImportError:

            return 'BH1750 sensor library not found'


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
