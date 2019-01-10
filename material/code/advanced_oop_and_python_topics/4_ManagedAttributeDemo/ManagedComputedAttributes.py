import sys 

class T: 
	def __init__(self, x): 
		if type(x) != int:
			raise TypeError("Bad type for x") 
		self.x = x 

	def getName(self): 
		return self.__dict__['x'] ** 2 

	def setName(self, new_val): 
		if type(new_val) != int: 
			raise TypeError("Bad type:new_val") 
		self.__dict__['x'] = new_val

	def delName(self): 
		raise TypeError("Not allowed to delete x from object")

	x = property(getName, setName, delName, "Interface to x")

def main(): 
	inT = T(10) 
	print("inT.x:", inT.x) 
	inT.x = 500
	print("inT.x:", inT.x)
	try: 
		del(inT.x)
	except TypeError as e: 
		pass

main() 
