def decorator (ref_fun): 
	# Wrapper function *should* (not must) all the arguments required by 
	# original function F as it's formal parameter  
	def wrapper_function (arg): 
		print ("WP:I am in wrapper function, calling ref_fun, with my arg")
		ref_fun (arg) 
		print ("WP:I am done ")
	return wrapper_function 

def F (arg):
	print ("F:arg:", arg)

F = decorator (F)
F ("Hello")
