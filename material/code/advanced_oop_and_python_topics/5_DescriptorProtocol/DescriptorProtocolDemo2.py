import sys 

class Descriptor: 
	def __get__ (*arg): 
		print ("Descriptor:get") 
		print ("arg:", arg)

class Test1: 
	attr = Descriptor () 

def main (): 
	line = "-" * 65
	inT1 = Test1 () 
	print (line)
	print ("inT1.attr:", inT1.attr)
	print (line)
	print ("Test1.attr:", Test1.attr)
	print (line)
	inT1.attr = 100
	print ("inT1.attr:", inT1.attr)
	print (line)
	print ("Test1.attr:", Test1.attr)
	print (line)
	inT2 = Test1 () 
	print (line)
	print ("inT2.attr:", inT2.attr)
	print (line)
	print ("Test2.attr:", Test2.attr)
	print (line)
	sys.exit (0) 

main () 
