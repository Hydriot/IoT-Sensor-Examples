import wiringpi as GPIO
from resources.driver_base import DriverBase

## Manufacturer Source
## http://www.cqrobot.wiki/index.php/Liquid_Level_Sensor

class Driver(DriverBase):
    gpio_pin = None

    def __init__(self, gpio_pin):
        DriverBase.__init__(self)
        self.gpio_pin = gpio_pin
        pass    

    def initialize(self):
        GPIO.wiringPiSetup()

    def read_value(self):
        reading = GPIO.digitalRead(self.gpio_pin)
        return reading

    def is_available(self):
        reading = -1

        try:
            # TODO: If there is nothing it still reads as 0 need better mechanism
            reading = self.read_value()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read Liquid Level Sensor. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True        
        
        return False

    def display(self, value):
        if value == 1:
            print("liquid found!")
        else:
            print("No liquid detected!")