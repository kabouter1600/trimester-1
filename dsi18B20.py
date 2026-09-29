from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor() # aansluiten op pin 4 en d2
while True:
    temperature_celsius = sensor.get_temperature()
    print(temperature_celsius)

