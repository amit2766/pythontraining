import sys 

class Celsius:
    def __init__(self, temp = 0):
        self.temperature = temp 

    def to_fahrenheit(self):
        return (self.__dict__['temperature'] * 1.8) + 32
    
    @property
    def temperature(self):
        print("Getting value")
        return (self.__dict__['temperature']) 
    
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__dict__['temperature'] = value 

def main (): 
    c = Celsius()
    print ("c.temperature:", c.temperature)
    c.temperature = 37
    print ("c.temperature:", c.temperature)
    fnht = c.to_fahrenheit()
    print ("fnht:", fnht)
    try:
        c.temperature = -300 
    except ValueError: 
        print("Temperature below -237 is not possible") 
    sys.exit (0) 
main () 
