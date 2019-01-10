#! /usr/local/bin/python3 

import sys 

def main (): 

	line = "-" * 60 
	f_handle = open ("test.log", "r") 

	# Read file in line by line fashion 
	while True: 
		try: 
			line = f_handle.__next__() # You can use next (f_handle) as well 
		except StopIteration:
			break 
		print (line, end='')

	f_handle.close () 

	sys.exit (0) 

main () 
