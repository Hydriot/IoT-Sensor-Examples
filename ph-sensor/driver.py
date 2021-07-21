import sys
import time
import os

from resources.driver_base import DriverBase
from ADS1115 import PGA, Channel, ConverterMode, ADS1115

## Manufacturer Source
## http://www.cqrobot.wiki/index.php/TDS_Meter_Sensor

class Driver(DriverBase):
    converter_mode = None
    channel = None
    offset = -4.21

    def __init__(self):

        # Set the IIC address (0X48 or 0X49 based on switch on ADC Module)
        self.converter_mode = ConverterMode.x48
        # Set the Programmable Gain Adjustment (Gain and voltage range)
        self.pga = PGA.REG_CONFIG_PGA_6_144V
        # Set the channel
        self.channel = Channel.A1

        DriverBase.__init__(self)        
        pass    

    def convert_raw(self, raw_value):
        # Check manifacturing manual for specific calculation from voltage to PH

        ph_vol = (((raw_value*5.0)/1024)/6)
        ph_value = (3.5 * ph_vol) + self.offset

        return round(ph_value, 2)

    def initialize(self):
        self.ads1115 = ADS1115()

        self.ads1115.setAddr_ADS1115(self.converter_mode)
        self.ads1115.setGain(self.pga)

    def read_voltage(self):
        ph = self.ads1115.readVoltage(self.channel)
        reading = ph['r']
        return reading

    def read_value(self):
        raw_value = self.read_voltage()
        return self.convert_raw(raw_value)

    def is_available(self):
        reading = -1

        try:
            reading = self.read_value()
        except:
            e = sys.exc_info()[0]
            print(f"Failed to read PH. Error Details >> {e}")
            return False
        finally:
            if reading > -1:
                return True        
        
        return False

    def display(self, value):
        print(f"ph Meter - [{value}]")

