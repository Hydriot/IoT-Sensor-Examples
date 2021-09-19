import time
import Adafruit_DHT as dht
import sys

from resources.driver_base import DriverBase

## Manufacturer Source
## https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
## https://github.com/adafruit/Adafruit_CircuitPython_DHT
## https://pypi.org/project/adafruit-circuitpython-dht/


class Driver(DriverBase):
    pin = None
    last_humidity = None
    last_temperature = None    
    
    def __init__(self, pin): 
        DriverBase.__init__(self)
        self.pin = pin ## GPIO PIN

    def initialize(self):
        pass        

    def read_raw(self):
        self.humidity, self.temperature = dht.read_retry(dht.DHT22, self.pin)

        return self.last_humidity

    def display(self):
        print("Reading Sensor Data...")
        print()
        self.read_value()
        print(f"Temperature [{self.temperature}C] Humidity [{self.last_humidity}]")