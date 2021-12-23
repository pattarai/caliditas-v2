try:
    import network
    try:
        from hcsr04 import HCSR04
        import time
        try: 
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            if not wlan.isconnected():
                print('connecting to network...')
                wlan.connect('jesinthan', 'jesinthan')
                while not wlan.isconnected():
                    pass
            if wlan.isconnected():
                print('connected')
        except:
            print("WIFI MANAGER ERROR")
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
            time.sleep_ms(1000)
    except:
        print("PROXIMITY LIBRARY ERROR")
except:
    print("NETWORK LIBRARY ERROR")