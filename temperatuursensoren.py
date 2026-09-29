import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor, Unit
from gpiozero import LED
from time import sleep

dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
led_groen = LED(17)
led_oranje = LED(27)
led_rood = LED(22)
volgnummer = 1

while True:
    sleep(2.0)
    print(volgnummer)
    volgnummer += 1
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error
    
    time.sleep(2.0)

    temperature_celsius = sensor.get_temperature()
    print(temperature_celsius)
    
    print(f"Temp: {temperature_c:.1f} C / {temperature_celsius} C")
    if temperature_c < temperature_celsius:
        groter_getal = temperature_celsius
        kleiner_getal = temperature_c

    else:
        groter_getal = temperature_c
        kleiner_getal = temperature_celsius

    verschil = groter_getal - kleiner_getal

    print(f"Verschil: {verschil:.1f} C")
    
    if verschil < 1:
        led_groen.on()
        led_oranje.off()
        led_rood.off()
        print("groen aan")

    elif 1 < verschil < 5:
        led_groen.off()
        led_oranje.on()
        led_rood.off()
        print("oranje aan")

    elif verschil > 5:
        led_groen.off()
        led_oranje.off()
        led_rood.on()
        print("rood aan")
    