def decorator(F): 		# On @ decoration
	def wrapper(*args): # On wrapped function call
		# Use F and args 
		# F(*args) calls original function 
		# If F (*args) is returning any value other 
		# than None then caputre it and return it 
		return #return value of F(*args))
	return wrapper 

@decorator 				# func = decorator(func)
def func(x, y): 		# func is passed to decorator's F
	# Definition of func (x, y)

func(6, 7) 				# 6, 7 are passed to wrapper's *args
