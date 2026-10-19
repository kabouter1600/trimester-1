File "/home/rpi/programmas/trimester-1/trimester-1/opdracht-bme280.py", line 17, in <module>
    spi = board.SPI()
  File "/usr/local/lib/python3.13/dist-packages/board.py", line 84, in SPI
    return busio.SPI(SCLK, MOSI, MISO)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/busio.py", line 395, in __init__
    self._spi = _SPI(portId)
                ~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/adafruit_blinka/microcontroller/generic_linux/spi.py", line 25, in __init__
    self._spi = spi.SPI(device=(portid, 0))
                ~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/Adafruit_PureIO/spi.py", line 149, in __init__
    raise IOError(f"{device} does not exist")
OSError: /dev/spidev0.0 does not exist

sudo raspi-config nonint do_spi 0
sudo reboot
