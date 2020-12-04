import machine
import onewire
import utime
import ds18x20


def read_ds18b20():

    sensor_wire = onewire.OneWire(machine.Pin(5))
    temperature_sensor = ds18x20.DS18X20(sensor_wire)

    sensor_address = temperature_sensor.scan().pop()
    temperature_sensor.convert_temp()

    utime.sleep_ms(500)

    celcius = temperature_sensor.read_temp(sensor_address)
    fahrenheit = (celcius * 1.8) + 32

    return fahrenheit, celcius
