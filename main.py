import utime
import wifi
import sensors

wifi.wifi_connect()

print("Hello, world!")
print('The current temperature is:', sensors.read_ds18b20()[0])

utime.sleep(5)

wifi.wifi_disconnect()
