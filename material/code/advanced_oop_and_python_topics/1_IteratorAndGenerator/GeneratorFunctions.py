#! /usr/local/bin/python3 

import sys 

def gensquares (N): 
	for i in range (N): 
		yield i**2 

def main (): 

	line = "-" * 60 
	G = gensquares (5) 
	print ("type (R):", type (G))

	while True: 
		try: 
			i = G.__next__() 
		except StopIteration: 
			break 
		print ("i:", i)
	print (line)
	# Direct way 
	for i in gensquares (5): 
		print ("i:", i)
	print (line)
	sys.exit (0) 

main () 