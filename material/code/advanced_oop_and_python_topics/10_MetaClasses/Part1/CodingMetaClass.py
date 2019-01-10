class Meta (type): 
	pass

# Class Meta would contain methods 
# Those methdos will have 'Spam', (Eggs, ), {'data':1, 'meth' : <function ..>}

class Eggs:
	pass 

class Spam (Eggs, metaclass=Meta):
	data = 1
	def meth(self, arg):
		return self.data + arg
"""
s = Spam ()
print ("type (s):", type (s))
print ("type (Spam):", type (Spam))
"""


    
