# Attribute can be added to a class after it has been 
# defined. So we create an attribute e.g. extra in this 
# case. And client can make choice late in the process 
# and has the ability to add the attribute conditionally. 

# required is a placeholder function here, depicting the 
# fact that attribute is being added to a client class 
# if required returns favourably and that depends upon 
# end user choices. 

def extra(self, arg): ... 			# Extra attribute coded separately 

class Client1: ..self 				# Client augments: too distributed
	if required():
		Client1.extra = extra

class Client2: ...
	if required():
		Client2.extra = extra

class Client3: ...
	if required():
		Client3.extra = extra

X = Client1()
X.extra()							# Put your manual check here
