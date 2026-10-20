
import time
import board
import spidev 
from adafruit_bme280 import basic as adafruit_bme280
import digitalio

spi = board.SPI()
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)
bme280.sea_level_pressure = 1013.25

f = open("data-bme280.csv","a")
f.write("Time,Temperature (C),Humidity (%),Pressure (hPa),Altitude (m)\n")
f.close()

while True:
    print(f"\nTemperature: {bme280.temperature:0.1f} C")
    print(f"Humidity: {bme280.relative_humidity:0.1f} %")
    print(f"Pressure: {bme280.pressure:0.1f} hPa")
    print(f"Altitude = {bme280.altitude:0.2f} meters")
    huidige_tijd = time.ctime()
    f = open("data-bme280.csv","a")
    f.write(f"{huidige_tijd},{bme280.temperature:0.1f},{bme280.relative_humidity:0.1f},{bme280.pressure:0.1f},{bme280.altitude:0.2f}\n")
    f.close()
    time.sleep(5)
