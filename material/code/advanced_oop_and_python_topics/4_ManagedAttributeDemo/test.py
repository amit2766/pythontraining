class Person:
	def __init__(self, name):
		self._name = name
		
	@property 					# name = property(name)
	def name(self):
		"name property docs"
		print('fetch...')
		return self._name


	@name.setter				# name = name.setter(name)
	def name(self, value):
		print('change...')
		self._name = value

	@name.deleter 				# name = name.deleter(name)
	def name(self):
		print('remove...')
		del self._name

def main ():
	bob = Person('Bob Smith')	# bob has a managed attribute
	print(bob.name)				# Runs name getter (name 1)
	print ("addr(Person.name.getter):", hex(id((Person.name.getter))))
	bob.name = 'Robert Smith'	# Runs name setter (name 2)
	print ("addr(Person.name.setter):", hex(id((Person.name.setter))))
	print(bob.name)
	del bob.name 				# Runs name deleter (name 3)
	print('-'*20)
	sue = Person('Sue Jones')	# sue inherits property too
	print(sue.name)
	print(Person.name.__doc__)	# Or help(Person.name)

	print ("type (Person.name):", type (Person.name))
	print ("hex(id(Person.name)):", hex(id(Person.name)))
	print ("type (Person.name.getter):", type (Person.name.getter))
	print ("type (Person.name.setter):", type (Person.name.setter))
	print ("type (Person.name.deleter):", type (Person.name.deleter))

	print ("addr(Person.name.getter):", hex(id((Person.name.getter))))
	print ("addr (Person.name.setter):", hex(id((Person.name.setter))))
	print ("addr (Person.name.deleter):", hex(id(Person.name.deleter)))



main () 