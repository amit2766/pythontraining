import sys 

def decorator (arg): 
	print ("type (arg):", type (arg))
	return (10) 


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

	sys.exit (0) 

main () 

