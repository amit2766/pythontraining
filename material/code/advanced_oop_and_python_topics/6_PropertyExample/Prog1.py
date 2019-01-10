import sys 

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

def main (): 

	man = Celsius()
	man.temperature = 37
	print ("man.temperature:", man.temperature)
	print ("man.to_fahrenheit:", man.to_fahrenheit())
	print ("man.__dict__:", man.__dict__)
	sys.exit (0) 

main () 
