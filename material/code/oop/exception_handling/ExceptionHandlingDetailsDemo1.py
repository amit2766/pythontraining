import sys 

line = "-" * 60

def action1 (): 
	print ("action1:in action")
	raise IndexError 

def action2 ():
	print ("action1:in action")
	raise IndexError ("Sending some data", 10, 20)


def f1 (): 
	try: 
		action1 () 
	except IndexError: 
		print ("Index Error")

def f2 (): 
	try: 
		action1 () 
	except IndexError as e: 
		print ("Index Error")
		print ("type (e):", type (e))
		print (e)

def f3 (): 
	try: 
		action2 () 
	except IndexError as e: 
		print ("Index Error")
		print ("type (e):", type (e))
		print ("type(e.args):", type (e.args))
		for arg in e.args: 
			print ("arg:", arg)

def main (): 
	f1 () 
	print (line)
	f2 () 
	print (line)
	f3 () 
	print (line)

	sys.exit (0) 

main () 