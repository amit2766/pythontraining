#! /usr/local/bin/python3 

import sys 

def main ():

	line = "-" * 60 
	L = [x*10 for x in range (5)]

	# Traversal Way 1 
	for x in range (len (L)): 
		print ("x:", x)
	print (line)
	# Traversal Way 2 
	for i in range (len (L)):
		print ("L[", i, "]:", L[i])
	print (line)
	# Extracting iterator 
	lst_iter = L.__iter__ ()
	print ("lst_iter:", lst_iter)
	print ("type (lst_iter):", type (lst_iter))
	print (line)

	# Accessing the invididual elements of iterator 
	i = lst_iter.__next__() 
	print ("1:i:", i)
	i = lst_iter.__next__()
	print ("2:i:", i)
	i = lst_iter.__next__()
	print ("3:i:", i)
	i = lst_iter.__next__()
	print ("4:i:", i)
	i = lst_iter.__next__()
	print ("5:i:", i)

	# One more lst_iter.__next__ () will generate StopIteration exception 
	try: 
		i = lst_iter.__next__() 
	except StopIteration: 
		print ("Have accessed all objects in an iterator")
	print (line)

	# What happens behind the screen in for x in <iterator> syntax 
	# Extract the iterator again 
	lst_iter = L.__iter__() 
	while True: 
		try:
			x = lst_iter.__next__()
		except StopIteration: 
			break 
		print ("x:", x)
	print (line)

	# Using iter and next method rather than invoking __iter__ and 
	# __next__ explicitly 
	lst_iter = iter (L)
	while  True:
		try: 
			x = next (lst_iter)
		except StopIteration: 
			break
		print ("x:", x)
	print (line)

	sys.exit (0) 

main () 
