#! /usr/local/bin/python3 

import sys

def main (): 

	# What happens when 
	# for key in D:
	#	print ("key:", key, "D[key]:", D[key])
	D = {"a":1, "b":2, "c":3} 
	d_it = dict.__iter__(D)
	while True: 
		try: 
			k = d_it.__next__()
		except StopIteration: 
			break 
		print ("key:", k, "value:", dict.__getitem__(D, k))	 


	sys.exit (0) 

main () 
