import time
import board
import adafruit_dht
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
dhtDevice = adafruit_dht.DHT11(board.D18)

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convertVolts(data):
    volts = (100 * 3.3) / float(1023)
    volts = round(volts, 4)
    return volts

def convertTemp(volts):
    temp = (100 * volts) - 50
    temp = round(temp, 4)
    return temp

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}% ")

        data = read_adc(0)
        print("adc   : {:8}".format(data))
        volts = convertVolts(data)
        temp = convertTemp(volts)
        print("volts : {:8.2f}".format(volts))
        print("temp  : {:8.2f}".format(temp))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(5.0)
    