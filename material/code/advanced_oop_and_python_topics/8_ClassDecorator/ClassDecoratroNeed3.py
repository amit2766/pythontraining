def decorator(F):			# F is func or method without instance
	def wrapper(*args):		# class instance in args[0] for method
							# F(*args) runs func or method

	
	return wrapper


@decorator
def func(x, y):				# func = decorator(func)
...

# End of func definition 

func(6, 7)					# Really calls wrapper(6, 7)



class C: 					# method = decorator(method)
@decorator 					# Rebound to simple function
def method(self, x, y): 
... 
X = C() 				
X.method(6, 7) 				# Really calls wrapper(X, 6, 7)

#-------------------------------------------------------------------------- 