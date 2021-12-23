try:
    import network
    try:
        from hcsr04 import HCSR04
        # try: 
        #     wlan = network.WLAN(network.STA_IF)
        #     wlan.active(True)
        #     if not wlan.isconnected():
        #         print('connecting to network...')
        #         wlan.connect('PhantomNode01', 'skywalker')
        #         while not wlan.isconnected():
        #             print("not-connected")
        #             pass
        #     if wlan.isconnected():
        #         print('connected')
        # except:
        #     print("WIFI MANAGER ERROR")
        while True:
                try:
                    proximitySensor = HCSR04(trigger_pin=2, echo_pin=13, echo_timeout_us=10000)
                    try:
                        distance = proximitySensor.distance_cm()
                        print(distance)
                    except:
                        print("NO VALUE")
                    
                except:
                    print ("CONNECTION ERROR")
    except:
        print("PROXIMITY LIBRARY ERROR")
except:
    print("NETWORK LIBRARY ERROR")