import network
import utime
import config


wlan = network.WLAN(network.STA_IF)


def wifi_connect(ssid=config.SSID, passwd=config.WIFI_PASSWD):
    """
        Connects to WiFi.  Will attempt three times to connect.  Uses the LEDs for visual
        indication of network connection status.  RED when disconnected, GREEN when connected.
    """

    count = 3

    print('Attempting to connect to WiFi...')

    while not wlan.isconnected() and count > 0:

        wlan.active(True)
        wlan.config(dhcp_hostname='Wemos_{}'.format(
            config.CLIENT_ID))
        wlan.connect(ssid, passwd)
        count -= 1
        utime.sleep(3)

    if wlan.isconnected():

        print('Connected to Wifi. IP Address: {}'.format(
            wlan.ifconfig()[0]))

    else:

        print('Unable to connect to Wifi')


def wifi_disconnect():
    """
        Function to disconnect from WiFi
    """

    wlan.disconnect()
    wlan.active(False)

    print('Disconnected from WiFi...')

    return wlan.isconnected()


def connection_status():
    """
        Function to get network connection status

    Returns:
        Bool: True for connected, False otherwise
    """

    network_conn = wlan.isconnected()
    return network_conn
