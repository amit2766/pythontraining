import sys 

calls = 0					# State via enclosing scope and global
def tracer(func):
	def wrapper(*args, **kwargs):	# Instead of class attributes
		global calls				# calls is global, not per-function
		calls += 1
		print('call %s to %s' % (calls, func.__name__))
		return func(*args, **kwargs)
	return wrapper

@tracer 							# Same as: spam = tracer(spam)
def spam(a, b, c): 
	print(a + b + c) 

@tracer 							# Same as: eggs = tracer(eggs)
def eggs(x, y): 
	print(x ** y) 

def main ():
	spam(1, 2, 3) 						# Really calls wrapper, assigned to spam
	spam(a=4, b=5, c=6) 				# wrapper calls spam
	eggs(2, 16) 						# Really calls wrapper, assigned to eggs
	eggs(4, y=4) 						# Global calls is not per-decoration here!
	sys.exit (0) 

main () 
