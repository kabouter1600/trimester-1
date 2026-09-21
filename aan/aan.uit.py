from gpiozero import LED, Button
from time import sleep

led = LED(4)
button = Button(17)

while True:
    button.wait_for_press()
    led.toggle()
    button.wait_for_release()