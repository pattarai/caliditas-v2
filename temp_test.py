import mlx90614  # Melexis MLX90614 IR temperature sensor driver
import machine
import time
i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(14))
tempSensor = mlx90614.MLX90614(i2c)


while True:
    temperature = tempSensor.read_object_temp()
    # Fahrenheit Conversion & Temperature Offset for Distance
    temperature = ((float(temperature) * 9 / 5) + 32) + 12
    print(temperature)
    time.sleep_ms(500)
