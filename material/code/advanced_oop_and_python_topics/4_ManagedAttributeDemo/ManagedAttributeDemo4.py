class Person:
	def __init__(self, name):
		self._name = name
		
	@property 					# name = property(name)
	def name(self):
		"name property docs"
		print('fetch...')
		print ("Getter:")
		#print ("Addr (name):", hex (id (name)))
		#print ("type (name):", type (name))

		return self._name


	@name.setter				# name = name.setter(name)
	def name(self, value):
		print('change...')
		print ("Setter:")
		#print ("Addr (name):", hex (id (name)))
		#print ("type (name):", type (name))
		self._name = value

	@name.deleter 				# name = name.deleter(name)
	def name(self):
		print('remove...')
		print ("Deleter:")
		#print ("Addr (name):", hex (id (name)))
		#print ("type (name):", type (name))
		del self._name

def main ():
	bob = Person('Bob Smith')	# bob has a managed attribute
	print("type(bob.name):", type(bob.name))
	print(bob.name)				# Runs name getter (name 1)
	bob.name = 'Robert Smith'	# Runs name setter (name 2)
	print(bob.name)
	del bob.name 				# Runs name deleter (name 3)
	print('-'*20)
	sue = Person('Sue Jones')	# sue inherits property too
	print(sue.name)
	print(Person.name.__doc__)	# Or help(Person.name)

main () 
