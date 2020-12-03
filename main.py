import utime
import wifi

wifi.wifi_connect()

print("Hello, world!")

utime.sleep(10)

wifi.wifi_disconnect()
