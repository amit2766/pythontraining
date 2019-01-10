import sys 

class Person: 
	def __init__(self, name): 
		if type(name) != str: 
			raise TypeError("Bad type for name")
		self.name = name 

	def getName(self): 
		print("In getName")
		#return self.name
		return (self.__dict__['name'])

	def setName(self, new_name): 
		if type(new_name) != str:
			raise TypeError("Bad type for name")
		print("In setName")
		self.__dict__['name'] = new_name 

	def delName(self): 
		print("In delName")
		del (self.__dict__['name'])

	name = property(getName, setName, delName, "Abstraction Object") 

def main(): 
	p = Person("Yogeshwar")
	try: 
		print("p.name:", p.name) 
	except RecursionError:
		print("OOPS")
	p.name = "Rohit"
	try:
		print("p.name:", p.name)
	except RecursionError: 
		print("OOPS")
	del(p.name) 

main()

