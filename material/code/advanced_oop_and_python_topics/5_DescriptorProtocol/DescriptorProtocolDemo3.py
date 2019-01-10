import sys 

class Name:
	"name descriptor docs"
	def __get__(self, instance, owner):		# self=Name, instance=PersonObject
		print('fetch...')					# owner=Person
		print("type(self):", type(self))
		print("type(instance):", type(instance))
		print("type(owner):", type(owner))
		return instance._name
	def __set__(self, instance, value):
		print('change...')
		instance._name = value
	def __delete__(self, instance):
		print('remove...')
		del instance._name

class Person: 
	def __init__(self, name): 
		self._name = name 
	name = Name() 						# Assign descriptor to attr

def main ():
	bob = Person('Bob Smith') 			# bob has a managed attribute
	print(bob.name) 					# Runs Name.__get__
	bob.name = 'Robert Smith' 			# Runs Name.__set__
	print(bob.name) 
	del bob.name 						# Runs Name.__delete__
	print('-'*20)
	sue = Person('Sue Jones')			# sue inherits descriptor too
	print(sue.name)
	print(Name.__doc__)					# Or help(Name)
	sys.exit (0)

main () 





