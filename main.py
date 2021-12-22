try:
    import mlx90614  # Melexis MLX90614 IR temperature sensor driver
    from hcsr04 import HCSR04  # HC-SR04 Ultrasonic Sensor Driver
    try:
        import ssd1306  # Import oledDisplay driver
        try:
            import network
            import wifimgr
            try:
                import webrepl
            except:
                print("Webrepl Module Import Error")
            try:
                import urequests as requests
                try:
                    import ujson as json
                    try:
                        import time
                        import machine
                        import framebuf
                        try:
                            try:
                                i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(
                                    14),freq=50000)
                                try:
                                    tempSensor = mlx90614.MLX90614(i2c)
                                    
                                    try:
                                        oledDisplay = ssd1306.SSD1306_I2C(
                                            128, 64, i2c)  # 128 vw x 64 vh display
                                        try:
                                            try:
                                                # Logo in Byte Array Format
                                                buffer = bytearray(b'xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x01\x80\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x01\x80\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x01\x80\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x01\x80\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x80\x00\x01\x80\x00\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x01\x80\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x00\x40\x01\x80\x02\x00\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x00\x60\x00\x00\x06\x00\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x30\x00\x00\x0c\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x18\x03\xc0\x18\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x0c\x1f\xf8\x30\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x00\x7c\x3e\x00\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x00\xe0\x07\x00\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x01\xc0\x01\x80\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x03\x00\x00\xc0\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x07\x00\x00\x60\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x06\x18\x0c\x60\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x0c\x38\x0c\x30\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x0c\x78\x0e\x30\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x0c\x78\x0e\x10\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x0c\x78\x0f\x18\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x1f\x8c\x78\x1f\x19\xf8\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x1f\x8c\x7f\xff\x19\xf8\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x0c\x7f\xfe\x30\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x0c\x7f\xfe\x30\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x06\x3f\xfc\x30\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x06\x1f\xfc\x60\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x03\x0f\xf8\x60\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x03\x0f\xf0\xc0\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x01\x8f\xf0\x80\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x01\x8f\xf1\x80\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x00\xcf\xf1\x00\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x0c\xcf\xf3\x30\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x18\x6f\xf3\x18\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x30\x6f\xf6\x0c\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x60\x6f\xf6\x06\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x40\x3f\xf6\x02\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x00\x3f\xfc\x00\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x3f\xfc\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x1f\xf8\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x00\x00\x00\x00\x00\x00\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x00\x00\x0f\xf0\x00\x00\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x80\x00\x0f\xf0\x00\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x07\xe0\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x00\x00\x00\x00\x07\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x07\xe0\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x01\x80\x00\x1f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x80\x00\x00\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0\x00\x00\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00\x00\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

                                                fb = framebuf.FrameBuffer(
                                                    buffer, 128, 64, framebuf.MONO_HLSB)
                                                print(dir(framebuf))
                                                oledDisplay.fill(0)
                                                oledDisplay.framebuf.blit(fb, 0, 0)
                                                oledDisplay.invert(1)
                                                oledDisplay.show()
                                                time.sleep_ms(2000)

                                                oledDisplay.fill(0)
                                                oledDisplay.text(
                                                    "PATTARAI'S", 10, 20)
                                                oledDisplay.text(
                                                    "CALIDITAS", 20, 40)
                                                oledDisplay.show()
                                                time.sleep_ms(2000)

                                            except:
                                                print("Logo Loading Error")
                                                
                                            try:
                                                oledDisplay.fill(0)
                                                oledDisplay.text(
                                                    "CONNECT WIFI AT", 0, 20)
                                                oledDisplay.text(
                                                    "192.168.4.1", 20, 40)
                                                oledDisplay.show()
                                                wlan = network.WLAN(network.STA_IF)
                                                wlan.active(True)
                                                if not wlan.isconnected():
                                                    print('connecting to network...')
                                                    wlan.connect('PhantomNode01', 'skywalker')
                                                    while not wlan.isconnected():
                                                        print("not-connected")
                                                        pass
                                                #connectToNetwork()
                                                #wlan = wifimgr.get_connection()
                                                #if wlan is None:
                                                #    print(
                                                #        "Could not initialize the network connection.")
                                                    # connectToNetwork()
                                                #    while True:
                                                #       pass  # Wait for network to connect
                                            except:
                                                print("WIFI MANAGER ERROR")
                                            

                                            try:
                                                buzzer = machine.Pin(
                                                    12, machine.Pin.OUT)
                                                buzzer.value(0)
                                            except:
                                                print(
                                                    "Buzzer Pin Initialize Error")
                                            while True:
                                                try:
                                                    proximitySensor = HCSR04(trigger_pin=2, echo_pin=13, echo_timeout_us=10000)
                                                    distance = proximitySensor.distance_cm()
                                                    print(
                                                        "Distance: " + distance)
                                                    if distance < 40 and distance > 0:
                                                        try:
                                                            temperature = tempSensor.read_object_temp()
                                                            # Fahrenheit Conversion & Temperature Offset for Distance
                                                            temperature = (
                                                                (float(temperature) * 9 / 5) + 32) + 12
                                                            print(
                                                                "Temperature: " + temperature)

                                                            oledDisplay.fill(0)
                                                            oledDisplay.text(
                                                                str(temperature), 35, 0)
                                                            oledDisplay.show()

                                                            if temperature > 99 and temperature < 120:
                                                                buzzer.value(1)
                                                                oledDisplay.text(
                                                                    "ALERT!!", 20, 20)
                                                                oledDisplay.text(
                                                                    "GO BACK FOR PIC", 0, 40)
                                                                oledDisplay.show()

                                                                try:  # Insert Temperature to DB
                                                                    oledDisplay.fill(
                                                                        0)
                                                                    oledDisplay.text(
                                                                        "INSERTING", 20, 20)
                                                                    oledDisplay.text(
                                                                        "TO DB", 0, 40)
                                                                    oledDisplay.show()
                                                                    time.sleep_ms(
                                                                        1000)
                                                                    url = 'http://caliditas.herokuapp.com/scan'
                                                                    data = {"rollno": "20IT055", "deviceId": "1", "temp": str(temperature)}
                                                                    file = {'image': open('buffer.png', 'rb')}
                                                                    response = requests.post(url, data=data, files=file)
                                                                    oledDisplay.fill(
                                                                        0)
                                                                    oledDisplay.text(
                                                                        "ALERTING", 20, 20)
                                                                    oledDisplay.text(
                                                                        "OFFICIALS", 0, 40)
                                                                    oledDisplay.show()
                                                                    time.sleep_ms(
                                                                        500)

                                                                except:
                                                                    print(
                                                                        "DB ERROR")
                                                            else:
                                                                buzzer.value(0)
                                                                oledDisplay.text(
                                                                    "YOU MAY PASS", 15, 20)
                                                                oledDisplay.show()
                                                                time.sleep_ms(
                                                                    1000)
                                                        except:
                                                            print(
                                                                "Error in Reading Temperature")

                                                    else:
                                                        oledDisplay.fill(0)
                                                        oledDisplay.text(
                                                            "NO ONE HERE", 15, 20)
                                                        oledDisplay.show()
                                                        time.sleep_ms(500)
                                                except:
                                                    print(
                                                        "Error in Reading Proximity")

                                        except:
                                            print("Network Connection Error")
                                            oledDisplay.fill(0)
                                            oledDisplay.text(
                                                "NETWORK ERROR", 20, 20)
                                            time.sleep_ms(1000)
                                    except:
                                        print(
                                            "OLED Display Initialization Error")
                                except:
                                    print("Sensors Initialization Error")
                            except:
                                print("I2C Configuration Error")
                        except:
                            print("Error Starting the Device")
                    except:
                        print("Built-In Modules Import Error")
                except:
                    print("UJSON Module Import Error")
            except:
                print("Requests Module Import Error")
        except:
            print("Network Module Import Error")
    except:
        print("OLED Display Driver Import Error")
except:
    print("IR Thermistor Driver Import Error")



def connectToNetwork():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        try:
            wlan.connect('PhantomNode01', 'skywalker')
            while not wlan.isconnected():
                pass
        except:
            print("Could not connect to PhantomNode01")
            try:
                wlan.connect('Phantom', '8754462663')
                while not wlan.isconnected():
                    pass
            except:
                print("Could not connect to Phantom")
                try:
                    wlan.connect('LICET WIFI', 'Licet@#786')
                    while not wlan.isconnected():
                        pass
                except:
                    print("Could not connect to LICET WIFI")
                        

