class General(Exception):
	 pass
class Specific1(General): 
	pass
class Specific2(General): 
	pass

def raiser0(): # Raise superclass instance
	X = General() 
	raise X 

def raiser1(): # Raise subclass instance
	X = Specific1() 
	raise X 

def raiser2(): # Raise different subclass instance
	X = Specific2() 
	raise X 

for func in (raiser0, raiser1, raiser2):
	try:
		func()
	except General:
	# Match General or any subclass of it
		import sys
		print('caught: %s' % sys.exc_info()[0])
