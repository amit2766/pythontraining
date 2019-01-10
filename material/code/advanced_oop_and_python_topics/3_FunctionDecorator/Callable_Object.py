import sys 

class TestClass: 
	def __init__(self, ref_fun): 
		self.function = ref_fun 

	def __call__ (self):
		self.function () 

def test_function (): 
	print ("test_function:In test_function")

def main ():
	t1 = TestClass (test_function)
	t1 () # Invoke __call__ passing t1 as self
	sys.exit ()

main ()
