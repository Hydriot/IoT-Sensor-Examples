import time
import os
from driver import Driver

toggle = True
pin = 1 ## GPIO 18

driver = Driver(pin)

try:
    while True:
        os.system('clear') 
        val = driver.read_value()        
        driver.display(val)

        toggle = not toggle
        print()
        print("Press Cntr+C in terminal to exit. " + ("[|]" if toggle else "[-]"))        
        time.sleep(1)

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")