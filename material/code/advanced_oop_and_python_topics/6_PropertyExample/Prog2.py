import sys 

class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

def main (): 

    try: 
        c = Celsius(-277)
    except ValueError: 
        print ("-277 is bad value")

    c = Celsius(37)
    print ("c.gettemperature():", c.get_temperature())
    c.set_temperature(10)

    try: 
        c.set_temperature(-300)
    except ValueError: 
        print ("-300 is bad value")

    # Python does not implement data encapuslation 
    c._temperature = -300
    print ("c.gettemperature():", c.get_temperature())

    sys.exit (0) 

main () 
