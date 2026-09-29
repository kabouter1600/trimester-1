from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()
while True:
    temperature_celsius = sensor.get_temperature()
    print(temperature_celsius)

