
def extra(self, arg): ... 				# Extra argument 

# Note 1 : Extras is deriviing itself from type 
# Note 2 : __init__ : Class, classname, superclasses, attributedict! 

class Extras(type):
	def __init__(Class, classname, superclasses, attributedict):
		if required():
			Class.extra = extra

class Client1(metaclass=Extras): ... 	# Metaclass declaration only (3.X form)
class Client2(metaclass=Extras): ... 	# Client class is instance of meta
class Client3(metaclass=Extras): ... 

X = Client1() 
X.extra() 
