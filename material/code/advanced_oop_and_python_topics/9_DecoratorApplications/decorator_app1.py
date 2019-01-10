import sys 

class tracer:								# State via instance attributes
	def __init__(self, func):				# On @ decorator
		self.calls = 0
		self.func = func				# Save func for later call
	def __call__(self, *args, **kwargs):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))	# On call to original function
		return self.func(*args, **kwargs)

@tracer 										# Same as: spam = tracer(spam)
def spam(a, b, c):							 	# Triggers tracer.__init__
	print(a + b + c) 
@tracer 										# Same as: eggs = tracer(eggs)
def eggs(x, y): 								# Wraps eggs in a tracer object
	print(x ** y) 

def main (): 
	spam(1, 2, 3) 								# Really calls tracer instance: runs tracer.__call__
	spam(a=4, b=5, c=6) 						# spam is an instance attribute
	eggs(2, 16) 								# Really calls tracer instance, self.func is eggs
	eggs(4, y=4) 								# self.calls is per-decoration here
	sys.exit (0) 

main () 
