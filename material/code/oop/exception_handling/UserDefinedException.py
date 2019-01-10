import sys 

class MyException (Exception): 
	pass 

def action1 ():
	print ("action1:I am in action 1")
	raise MyException ("Hello")

def f1 ():
	try:
		action1 () 
	except MyException as e: 
		print (e.args)
		(tp, value, traceback) = sys.exc_info () 
		print ("type:", tp, "value:", value, "traceback:", traceback)

def main ():
	f1 () 
	sys.exit (0) 

main () 