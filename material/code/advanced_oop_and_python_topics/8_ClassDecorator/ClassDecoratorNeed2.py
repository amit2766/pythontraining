import sys 

class Decorator: 
	def __init__ (self, func): 
		self.func = func 
	def __call__(self, *args): 
		print ("I am in __call__")
		for i in range (len (args)):
			print ("args[", i, "]:", args[i], "type (args[", i, "]):", type (args[i]))
		self.func (*args)

class C: 
	def __init__(self, n): 
		self._n = n 
	@Decorator
	def getn (self): 
		print ("getn:self._n", self._n)

def main (): 
		
	inC = C (100)
	print ("type (inC):", type (inC))
	inC.getn () 

	sys.exit (0)

main () 
