import sys 

def f1 ():
	L = [x for x in range (5)]
	i = 100 

	print (L[i])
	#except IndexError: 
	#	raise IndexError ((len (L), i))

def main (): 
	
	try:
		f1 () 
	
	except IndexError as e: 
		print (e.args)
		(tp, value, traceback) = sys.exc_info () 
		print ("type:", tp, "value:", value, "traceback:", traceback)
	sys.exit (0) 

main () 