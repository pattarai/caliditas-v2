# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import uos
import machine
import network
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('PhantomNode01', 'skywalker')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

# Start Webrepl
webrepl.start()
gc.collect()
