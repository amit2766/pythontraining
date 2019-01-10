class GetAttr:
	attr1 = 1
	def __init__(self):
		self.attr2 = 2
	def __getattr__(self, attr):			# On undefined attrs only
		print('get: ' + attr)
		if attr == 'attr3':			# Not on attr1: inherited from class
			return 3			# Not on attr2: stored on instance
		else:
			raise AttributeError(attr)

def test_get_attr ():
	X = GetAttr()
	print(X.attr1)
	print(X.attr2)
	print(X.attr3)
	print('-'*20)

test_get_attr () 

class GetAttribute:
	attr1 = 1
	def __init__(self):
		self.attr2 = 2
	def __getattribute__(self, attr):	    # On all attr fetches	
		print('get: ' + attr)							
		if attr == 'attr3':
			return 3
		else:
			return object.__getattribute__(self, attr)	# Use superclass to avoid looping here

def test_get_attribute (): 
	X = GetAttribute()
	print(X.attr1)
	print(X.attr2)
	print(X.attr3)

test_get_attribute () 
