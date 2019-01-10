# Pattern  
def decorator(A, B):
	# Save or use A, B
	def actualDecorator(F):
		# Save or use function F
		# Return a callable: nested def, class with __call__, etc.
		def wrapper (*arg): 
			# Use F + something! 
		return callable
	return actualDecorator

@    (decorator(actual_A, actual_B))			# F = decorator (actual_A, actual_B) (F) 
def F (*arg): 
	# Define F

F (*arg) 
is equivalent to 
decorator (actual_A, actual_B) (F) (*arg)


decorator(arg1, arg2)(F)(*args, **kwargs)