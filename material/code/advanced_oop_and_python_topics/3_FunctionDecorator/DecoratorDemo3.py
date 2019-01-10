def decorator (ref_fun): 
	def wrapper_function (n1, n2): 
		print ("WP:I am in wrapper function")
		rs = ref_fun (n1, n2)
		print ("WP:I am done")
		# Wrapper function will get return value returned by the my_add
		# therefore, it is it's responsibility to return the same. 
		return (rs) 
	return wrapper_function 

@decorator 
def my_add (n1, n2): 
	return (n1+n2)

summation = my_add (10, 20)
print ("g:summation:", summation)
