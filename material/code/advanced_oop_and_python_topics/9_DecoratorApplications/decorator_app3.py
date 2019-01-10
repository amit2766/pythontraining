import sys 

def tracer(func):										# State via enclosing scope and nonlocal
	calls = 0											# Instead of class attrs or global
	def wrapper(*args, **kwargs):						
		nonlocal calls
		calls += 1 										# calls is per-function, not global
		print('call %s to %s' % (calls,	func.__name__))
		return func(*args, **kwargs)
	return wrapper

@tracer 												# Same as: spam = tracer(spam)
def spam(a, b, c): 
	print(a + b + c) 
	
@tracer 												# Same as: eggs = tracer(eggs)
def eggs(x, y): 
	print(x ** y) 

def main (): 
	spam(1, 2, 3) 											# Really calls wrapper, bound to func
	spam(a=4, b=5, c=6) 									# wrapper calls spam
	eggs(2, 16) 											# Really calls wrapper, bound to eggs
	eggs(4, y=4) 											# Nonlocal calls _is_ per-decoration here
	sys.exit (0) 

main () 
