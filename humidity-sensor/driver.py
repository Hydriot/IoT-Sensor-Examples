import time
import RPi.GPIO
## import adafruit_dht
import Adafruit_DHT as dht
import sys

from resources.driver_base import DriverBase

## Manufacturer Source
## https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
## https://github.com/adafruit/Adafruit_CircuitPython_DHT
## https://pypi.org/project/adafruit-circuitpython-dht/

## Manuall install
## git clone https://github.com/adafruit/Adafruit_Python_DHT.git
## cd Adafruit_Python_DHT
## sudo apt-get upgrade
## sudo apt-get install build-essential python-dev python-openssl
## sudo python3 setup.py install

## python -m pip install adafruit-circuitpython-dht
## python -m pip install adafruit-circuitpython-lis3dh
## sudo python3 -m pip install libgpiod2
## sudo python -m pip install board --upgrade


class Driver(DriverBase):
    pin = None
    ## sensor = None
    last_humidity = None
    last_temperature = None
    
    ## GPIO PIN
    def __init__(self, pin): 
        DriverBase.__init__(self)
        self.pin = pin

    def initialize(self):
        ## self.sensor = dht.DHT22
        ## self.sensor = adafruit_dht.DHT22(self.pin)
        pass

    def read_value(self):
        self.last_humidity, self.last_temperature = dht.read_retry(dht.DHT22, self.pin)        
        # self.last_humidity = self.sensor.humidity
        # self.last_temperature = self.sensor.temperature

        return self.last_temperature

    def is_available(self):
        reading = -1

        try:
            # TODO: If there is nothing it still reads as 0 need better mechanism
            reading = self.read_value()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read Temperature and Humidity. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True
        
        return False

    def display(self):
        temp = self.read_value()

        print(f"Temperature [{temp}C] Humidity [{self.last_humidity}]")