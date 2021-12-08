
from machine import I2C, Pin, SoftI2C
import urequests as requests
import ssd1306  # Import oledDisplay driver
import mlx90614  # Melexis MLX90614 IR temperature sensor driver
import time


try:
    i2c = I2C(scl=Pin(5), sda=Pin(4))

    oledDisplay = ssd1306.SSD1306_I2C(
        128, 64, i2c)  # 128 vw x 64 vh display
    tempSensor = mlx90614.MLX90614(i2c)

    while True:
        try:
            oledDisplay.fill(0)
            temperature = tempSensor.read_object_temp()
            temperature = (float(temperature) * 9 / 5) + 32 + 2
            print(temperature)
            oledDisplay.text(str(temperature), 35, 0)
            oledDisplay.show()

            # print(tempSensor.read_ambient_temp(), tempSensor.read_object_temp())
            try:
                if temperature > 98.6:
                    oledDisplay.text("BEEP BEEP", 20, 20)
                    oledDisplay.show()
                    response = requests.get(
                        "http://192.168.0.101:5000/scan?rollno=19IT049&deviceId=3&temp=" + str(temperature))
                    time.sleep_ms(2000)
                else:
                    oledDisplay.text("YOU MAY PASS", 15, 20)
                    oledDisplay.show()
                    time.sleep_ms(1000)
            except:
                print("POST ERROR")
        except:
            print("DISPLAY ERROR")
        time.sleep_ms(1000)
except:
    print("LIB IMPORT ERROR")
