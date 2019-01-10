#! /usr/local/bin/python3 

import sys 

def main (): 
	
	line = "-" * 60 

	print ("List comprehension:")
	L = [x for x in range (10)]
	print (line)

	print ("Generator expression:")
	X = (x for x in range (10))
	for i in X:
		print (i)
	print (line)

	print ("Generator Expression Demistified")
	GE = (x for x in range (10))
	print ("type (GE):", type (GE))
	while True: 
		try: 
			x = GE.__next__() 
		except StopIteration: 
			break 
		print ("x:", x)
	print (line)
	sys.exit (0) 

main () 
