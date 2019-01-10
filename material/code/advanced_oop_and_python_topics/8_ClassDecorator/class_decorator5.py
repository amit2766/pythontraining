# Multiple instances pattern 
import sys 

class Wrapper:
	def __init__(self, arg):
		self.wrapped = arg
	def __getattr__(self, name):			
		return getattr(self.wrapped, name)

def decorator(C):
	def onCall(*args):
		return Wrapper(C(*args))
	return onCall

@decorator 										
class C:										
	def __init__(self, x, y): 
		self.attr = 'spam' 
		self.x = x 
		self.y = y 
	def display (self): 
		print ("attr:", self.attr)
		print ("self.x:", self.x)
		print ("self.y:", self.y)

def main (): 
	inC = C (100, 200) 
	print ("type (inC):", type (inC))
	print(inC.attr) 
	inC.display () 
	inC1 = C (300, 400)
	inC1.display () 
	inC.display () 
	sys.exit (0) 

main () 

