# Same, but with generic __getattr__ undefined attribute interception

class Powers:
	def __init__(self, square, cube):
		self._square = square
		self._cube = cube
	def __getattr__(self, name):
		if name == 'square':
			return self._square ** 2
		elif name == 'cube':
			return self._cube ** 3
		else:
			raise TypeError('unknown attr:' + name)
	def __setattr__(self, name, value):
		if name == 'square':
			self.__dict__['_square'] = value
		else:
			self.__dict__[name] = value

def main (): 
	# square and cube are not attributes of class! 
	X = Powers(3, 4)
	print(X.square)
	print(X.cube)
	X.square = 5
	print(X.square)

main () 

