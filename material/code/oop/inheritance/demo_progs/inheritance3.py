# Extender demo 

import sys 

class BaseClass:
	def method (self): 
		print ("This is Base-place holder method")

class DerivedClass (BaseClass): 
	def method (self): 
		print ("This is Derived-place holder method")
		print ("Takes help of Base-place holder method")
		BaseClass.method (self) 
		print ("Back to derived class, end...")

def main ():

	b1 = BaseClass ()
	b1.method ()

	d1 = DerivedClass () 
	d1.method () 

	sys.exit (0) 

main () 
