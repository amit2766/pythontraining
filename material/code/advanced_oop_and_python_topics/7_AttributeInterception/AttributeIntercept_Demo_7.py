import sys 

# Using __getattribute__ instead of __getattr__  
# Because we intercept all the attributes, 
# __dict__ entries will be visible in demo_7 
# those were not visible in demo_6. 
# This establishes that only unknown attributes are 
# caught by __getattr__ and all attributes are caught 
# by __getattribute__ 

class Person: 
	def __init__(self, name): 
		self._name = name 

	def __getattribute__(self, attr):				# On [obj.any]
		print('get: ' + attr)						# Intercept all names
		if attr == 'name':			
			attr = '_name'							# Map to internal name
		return object.__getattribute__(self, attr)	# Avoid looping here

	def __setattr__(self, attr, value): 	# obj.attr = value LHS use 
		print ("set:", attr) 
		if attr == 'name': 
			attr = '_name'
		self.__dict__[attr] = value 		# Avoid recursion 

	def __delattr__(self, attr): 
		print ("del:", attr)
		if attr == 'name': 
			attr = '_name'
		del self.__dict__[attr]

def main ():

	p1 = Person ("Rodger") 
	print (p1.name) 

	p1.name = "Rafa" 
	print (p1.name) 
	del (p1.name)

	sys.exit (0)

main () 
