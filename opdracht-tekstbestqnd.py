import board
import adafruit_dht
from gpiozero import MCP3008
from time import sleep
teller = 0
 
dhtDevice = adafruit_dht.DHT11(board.D18)
while True:
       
        try:
            temp_dht = dhtDevice.temperature
            temp_f = temp_dht * (9/5) + 32
            humidity = dhtDevice.humidity
               
       
        except RuntimeError as error:
                print( error.args[0])
                sleep(2.0)
                continue
        except Exception as error:
                dhtDevice.exit()
                raise error
       
        sleep(2.0)
       
 
        Digi_waarde = MCP3008(channel = 0)
        spannings_waarde = (Digi_waarde.value / 1) * 3.3
        sleep(1)
 
        temp_TMP = (spannings_waarde - 0.5) /  0.01
       
        print(f"{temp_dht}°C --> DHT")
       
        print(f":{temp_TMP}°C --> TMP36")
 
        verschil = temp_dht-temp_TMP
        gemiddelde = (temp_dht+temp_TMP)/2
 
 
 
 
        f = open("mijndata.csv","a")
        teller = teller + 1
        f.write(f"{teller}:{temp_TMP:.1f},{temp_dht:.1f},{gemiddelde:.1f},{verschil:.1f}")
 
   
        f.close()
        sleep(3)
 
       
   
       
 
