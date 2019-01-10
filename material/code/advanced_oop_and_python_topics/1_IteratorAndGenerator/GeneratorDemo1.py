#! /usr/loca/bin/python3 

import sys 

def gen (L): 
	for element in L:
		X = yield (element ** 2) 
		#print ("X:", X)

def main ():

	line = "-" * 60 
	G = gen([x for x in range(1, 6)])
	print("type(G):", type(G)) 
	for y in G:
		print ("y:", y)
	print (line) 
	#sys.exit(0) 

	G = gen ([x for x in range (1, 6)]) 
	print ("type (G):", type (G))
	print (line)
	next (G) # Starting Generator is must 
	i = 0 
	while True: 
		try: 
			val = G.send (i**3)
			print ("val:", val)
		except StopIteration: 
			break 
		i = i + 2 
	print (line)

	sys.exit (0) 

main () 
