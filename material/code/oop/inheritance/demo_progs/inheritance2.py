# Replace demo 

import sys 

class BaseClass: 
	def method (self): 
		print ("BaseClass:This is a Base-place holder method")

class DerivedClass (BaseClass): 
	def method (self):
		print ("DerivedClass:This is a Derived-place holder method")

def main (): 

	b1 = BaseClass () 
	b1.method () 

	d1 = DerivedClass () 
	d1.method () 

	sys.exit (0) 

main () 