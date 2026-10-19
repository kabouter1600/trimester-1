from gpiozero import LED,MCP3008
from time import sleep
 
 
led = LED(3)
while True:
    potwaarde = MCP3008(channel = 0)
    print(potwaarde.value)
    led.on()
    sleep(2*potwaarde.value)
    led.off()
    sleep(2*potwaarde.value)
