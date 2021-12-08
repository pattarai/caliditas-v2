# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import uos
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl


# Start Webrepl
webrepl.start()
gc.collect()

from machine import I2C, Pin, SoftI2C
import urequests as requests
import ssd1306  # Import OLED driver
import mlx90614  # Melexis MLX90614 IR temperature sensor driver


# Read Temperature
i2cForIR = I2C(scl=Pin(5), sda=Pin(4))
i2cForOled = SoftI2C(scl=Pin(0), sda=Pin(2))
tempSensor = mlx90614.MLX90614(i2cForIR)


# 128 vw x 64 vh display with hardware I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2cForOled)

while True:
    temperature = tempSensor.read_object_temp()
    oled.text(f'Temp:{temperature}')
    oled.show()
    # print(tempSensor.read_ambient_temp(), tempSensor.read_object_temp())
    response = requests.post("https://caliditas.herokuapp.com/scan", data={
        "temp": str(temperature),
        "rollNo": "19IT049",
        "deviceId": "2"
    })
    oled.text(f'Temp:{temperature}\n|res:{response.text}')
    time.sleep_ms(500)
