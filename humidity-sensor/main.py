import time
import os
from driver import Driver

toggle = True
pin = 22 ## GPIO 25

driver = Driver(pin)

try:
    while True:
        os.system('clear') 
        driver.display()

        toggle = not toggle
        print()
        print("Press Cntr+C in terminal to exit. " + ("[|]" if toggle else "[-]"))        
        time.sleep(5)

## Continue with loop until Cntr+C is pressed in terminal
except KeyboardInterrupt:
    print("Exit Monitoring")