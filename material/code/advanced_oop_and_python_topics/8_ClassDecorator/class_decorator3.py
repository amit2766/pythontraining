import sys 

def decorator(cls):								# On @ decoration
	class Wrapper:
		def __init__(self, *args):				# On instance creation
			self.wrapped = cls(*args)
		def __getattr__(self, name):			# On attribute fetch
			return getattr(self.wrapped, name)
	return Wrapper

@decorator 										# C = decorator(C)
class C:										# Run by Wrapper.__init__
	def __init__(self, x, y): 
		self.attr = 'spam' 
		self.x = x 
		self.y = y 
	def display (self): 
		print ("attr:", self.attr)
		print ("self.x:", self.x)
		print ("self.y:", self.y)

def main (): 
	x = C(6, 7) 									# Really calls Wrapper(6, 7)
	print("type(x):", type(x)) 
	print(x.attr) 									# Runs Wrapper.__getattr__, prints "spam"
	x.display () 
	print("type(C):", type(C))
	print("C.__dict__:", C.__dict__)

main () 
