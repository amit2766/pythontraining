# If you Meta to be a metaclass then make it a subclass of class type 
# class Meta (type): 
#	pass 
# is the simplest way! 

--> class = Meta(classname, superclasses, attributedict)

# Metaclass Meta may override following methods of class type 
--> Meta.__new__(Meta, classname, superclasses, attributedict)
--> Meta.__init__(class, classname, superclasses, attributedict)

# Now if you've class Eggs : pass and want to derive spam for it 
# But if you want to use Metaclass named Meta to be used instead of 
# default type THEN it should be coded as follows 

class Spam(Eggs, metaclass=Meta):			# Inherits from Eggs, instance of Meta
	data = 1								# Class data attribute
	def meth(self, arg):					# Class method attribute
		return self.data + arg

Equivalent to 
Spam = Meta('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})


