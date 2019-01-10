import sys 

def d1(F): 
	return lambda: 'X' + F()
def d2(F): 
	return lambda: 'Y' + F()
def d3(F): 
	return lambda: 'Z' + F()

@d1
@d2
@d3
def func():
	return 'spam'

def main (): 
	print(func())			#Preduct output! 
	sys.exit (0) 

main () 
