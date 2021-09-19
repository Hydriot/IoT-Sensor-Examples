from abc import ABC, abstractmethod ## abstract module
import sys
import time
import traceback

class DriverBase(ABC):
    def __init__(self):
        self.initialize()
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def read_raw(self): raise NotImplementedError

    def read_value(self):

        try:            
            return self.read_raw()

        except:
            ex = traceback.format_exc()
            print(f"Failed to read Temperature and Humidity. Error Details. Error Details >> {ex}")

            time.sleep(5)
            return None


    def is_available(self):        
        try:
            ouput = self.read_raw()
            if ouput is None:
                return False

            return True

        except:
            ex = traceback.format_exc()
            print(f"Failed to read Temperature and Humidity. Error Details . Error Details >> {ex}")

            time.sleep(5)
            return False

    @abstractmethod
    def display(self, value): raise NotImplementedError
