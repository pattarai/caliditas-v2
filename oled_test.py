import ssd1306  # Import oledDisplay driver
import machine
import time
i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(14))
oledDisplay = ssd1306.SSD1306_I2C(128, 64, i2c)  # 128 vw x 64 vh display

while True:
    oledDisplay.fill(0)
    oledDisplay.text(
        "PATTARAI'S", 23, 20)
    oledDisplay.text(
        "CALIDITAS", 25, 40)
    oledDisplay.show()
    print("Tick")
    time.sleep_ms(500)
