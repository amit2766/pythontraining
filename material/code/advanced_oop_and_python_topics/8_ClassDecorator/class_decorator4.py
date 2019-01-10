# Cannot create multiple instances
class Decorator:
	def __init__(self, C):				# On @ decoration
		self.C = C
		self.n = 0 
	def __call__(self, *args):			# On instance creation
		
		self.wrapped = self.C(*args)
		return self
	def __getattr__(self, attrname):	# On atrribute fetch
		return getattr(self.wrapped, attrname)

@Decorator 			# C = Decorator(C)
class C: 
# Some definition 

x = C() 
y = C() 			# Overwrites x!:q

