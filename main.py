
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
            temperature = str(temperature)
            print(temperature)
            oledDisplay.text(temperature, 35, 20)
            oledDisplay.show()

            # print(tempSensor.read_ambient_temp(), tempSensor.read_object_temp())
            try:
                response = requests.post("https://caliditas.herokuapp.com/scan", data={
                    "temp": str(temperature),
                    "rollno": "19IT049",
                    "deviceId": "2"
                })
                oledDisplay.text(response.text, 0, 0, 25)
                oledDisplay.show()
            except:
                print("POST ERROR")
        except:
            print("DISPLAY ERROR")
        time.sleep_ms(500)
except:
    print("LIB IMPORT ERROR")
