def decorator (ref_fun): 
	def wrapper_function (n1, n2): 
		print ("WP:I am in wrapper_function")
		ref_fun (n1, n2)
		print ("WP:I am done")
	return ref_fun

def my_add (n1, n2): 
	return (n1+n2)

# Using higher order function. 
print ("g:decorator(my_add)(10, 20):", decorator (my_add)(10, 20))
