def decorator (d_arg1, d_arg2): 
	print ("d_arg1:", d_arg1)
	print ("d_arg2:", d_arg2)
	def actual_decorator (F): 
		print ("I am in actual_decorator")
		def wrapper (arg): 
			print ("arg to F:", arg)
			print ("type arg to F:", type (arg))
			F(arg) 
		return wrapper 
	return actual_decorator 

@decorator (100, 200)
def F (arg):
	print ("F:arg:", arg)

F (100)


@decorator("F1.LOG")
def F1(x1, x2): 
	pass 

@decorator("F2.LOG")
def F2(y1, y2, y3): 
	pass

line = '-' * 65

def decorator(f_name): 
	def actual_decorator(F): 
		f_handle = open(f_name, "w") 
		print(line, file=f_handle)
		f_handle.close() 
		def wrapper(*args, **kwargs): 
			f_handle = open(f_name, "a")
			print(*args, **kwargs, file=f_handle)
			f_handle.close() 
			return F(*args, **kwargs)
		return wrapper 
	return actual_decorator
