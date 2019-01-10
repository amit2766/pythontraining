class Eggs: 
	pass 

class Spam (Eggs): 
	data = 1 
	def meth (self, arg): 
		return (self.data + arg) 

# Internal Mechanism to be tried out separately 

>>>Spam = type('Spam', (Eggs,), {'data': 1, 'meth': lambda x, y : x.data + y, '__module__': '__main__'})
>>>x = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})
>>>i = x()
>>>x, i 
>>>i.data, i.meth(2)

