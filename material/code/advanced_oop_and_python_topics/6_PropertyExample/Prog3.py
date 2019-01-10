import sys 

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.__dict__['temperature'] * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self.__dict__['temperature']

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__dict__['temperature'] = value

    temperature = property(get_temperature,set_temperature)

def main (): 
    c = Celsius()
    print ("c.temperature:", c.temperature)
    c.temperature = 37
    print ("c.temperature:", c.temperature)
    fnht = c.to_fahrenheit()
    print ("fnht:", fnht)
    c.temperature = -300 
    sys.exit (0) 

main () 
