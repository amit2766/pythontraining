import sys 
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    def get_temperature(self):
        print("Getting value")
        return self._temperature
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
def main (): 
    temperature = property () 
    print ("type(temperature):", type (temperature))
    print ("temperature:", temperature)
    temperature = temperature.getter (Celsius.get_temperature)
    print ("type(temperature):", type (temperature))
    print ("temperature:", temperature)
    temperature = temperature.setter (Celsius.set_temperature)
    print ("type(temperature):", type (temperature))
    print ("temperature:", temperature)
    Celsius.temperature = temperature
    c = Celsius()
    print ("c.temperature:", c.temperature)
    c.temperature = 30 
    print ("c.temperature:", c.temperature)
    fnht = c.to_fahrenheit()
    print ("fnht:", fnht)
    sys.exit (0) 

main () 
