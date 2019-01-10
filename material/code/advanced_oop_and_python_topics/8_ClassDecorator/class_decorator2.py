import sys 

def decorator (arg): 
	print ("type (arg):", type (arg))
	return (arg)

@decorator 
class C: 
	def __init__(self, n): 
		self.n = n 

	def getn (self):
		return self.n 

	def setn (self, new_n): 
		self.n = new_n 

def main (): 
	print ("type (C):", type (C))
	inC = C (100)
	print (inC.getn ())
	print(inC.n)
	sys.exit (0) 

main () 
