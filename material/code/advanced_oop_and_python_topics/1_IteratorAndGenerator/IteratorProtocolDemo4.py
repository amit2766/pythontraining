#! /usr/local/bin/python3 

import sys 

def main (): 
	line = "-" * 60 
	R = range (10) 
	print ("type (R):", type (R))
	print (line)

	range_iter = R.__iter__() 
	while True: 
		try: 
			x = range_iter.__next__() 
		except StopIteration: 
			break 
		print ("x:", x)
	print (line)

	# Enumerate 
	L = [10, 20, 30, 40] 
	for t in enumerate (L): 
		print ("t:", t)
	print (line) 

	# How does it work? 
	e = enumerate (L) 
	print ("type(e):", type (e)) 

	enum_iter = e.__iter__ () 
	while True: 
		try: 
			t = enum_iter.__next__() 
		except StopIteration: 
			break 
		print ("t:", t)
	print (line)

	sys.exit (0) 

main () 
