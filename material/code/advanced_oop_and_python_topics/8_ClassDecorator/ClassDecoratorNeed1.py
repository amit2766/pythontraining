import sys 

class Decorator: 
	def __init__ (self, func): 
		self.func = func 
	def __call__(self, *args): 
		print ("I am in __call__")
		for i in range (len (args)):
			print ("args[", i, "]:", args[i], "type (args[", i, "]):", 
                                type (args[i]))
		self.func (*args)

@Decorator
def f (a, b, c):
	print ("a=", a, "b=", b, "c=", c) 

def main (): 
	f (10, 20, 30) 
	sys.exit (0)

main () 
