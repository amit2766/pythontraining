import sys 

# This program avoid inifinite loop by 
# explicitly calling __getattribute__ 
# of object class. 

class TestClass:
	def __init__(self, n1, n2): 
		self._n1 = n1 
		self._n2 = n2 

	def __getattribute__(self, attr): 
		tmp = None
		if attr == "_n1": 
			tmp = object.__getattribute__ (self, '_n1') + 10 
		elif attr == "_n2": 
			tmp = object.__getattribute__ (self, '_n2') + 20 
		else:
			raise AttributeError("Non existent attribute", attr)
		
		return (tmp) 

def main (): 
	inT = TestClass (100, 200)
	print ("inT._n1:", inT._n1) 
	print ("inT._n2:", inT._n2)
	try:
		print ("inT.x", inT.x) 
	except AttributeError:
		print("WOKE")
	sys.exit(0) 

main () 
