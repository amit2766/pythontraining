# Pattern 
def extra(self, arg): ...
def extras(Class):
	if required():
		Class.extra = extra
	return Class
class Client1: ...
	Client1 = extras(Client1)

class Client2: ...
	Client2 = extras(Client2)
class Client3: ...
	Client3 = extras(Client3)
X = Client1()
#-------------------------------------------------------
X.extra()
# Using Calss Decorator for the same 
def extra(self, arg): ...
def extras(Class):
	if required():
		Class.extra = extra
	return Class
@extras 					# Client1 = extras(Client1)
class Client1: ... 
@extras 					# Rebinds class independent of instances
class Client2: ... 
@extras
class Client3: ...

X = Client1()				# Makes instance of augmented class
X.extra()					# X is instance of original Client1

# Decorators technically correspond to metaclass __init__ methods, used to initialize 
# newly created classes. Metaclasses have additional customization hooks beyond class 
# initialization, though, and may perform arbitrary class construction tasks that might 
# be more difficult with decorators. This can make them more complex, but also better suited 
# for augmenting classes as they are being formed.


