import sys 

class T1:
	pass

class T2(T1): 
	pass 

class T3(T2): 
	pass 

class T4(T2): 
	pass 

class T5(T3, T4): 
	pass 

def main ():
	print ("MRO for T5:", T5.__mro__)
	sys.exit (0) 
main () 