# Provider demo 

import sys 

class BaseClass: 
	def delegate (self): 
		self.action () 

class DerivedClass (BaseClass): 
	def action (self): 
		print ("DerivedClass:Action")

def main (): 
	b1 = BaseClass () 
	#b1.delegate () 
	d1 = DerivedClass () 
	d1.delegate () 
	sys.exit (0)

main () 