# This is script that run when device boot up or wake from sleep.

import esp
import esp32

# Redirect debugging messages
# esp.osdebug(0)

# Turn off vendor debugging messages
esp.osdebug(None)

print('Flash Size (KB):', round(esp.flash_size() / 1000))
print('CPU Temp. (F):', esp32.raw_temperature())
