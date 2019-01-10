import sys 

class BaseClass: 

	def base_static_method ():
		print ("I am in base static method")

	base_d1_attr = 100

	def __init__(self, s1, n1): 
		if type (s1) != str or type (n1) != int: 
			raise TypeError ("Bad argument")
		self.s1 = s1 
		self.n1 = n1 

	def get_str (self): 
		return (self.s1)

	def set_str (self, new_str): 
		if type (new_str) != str: 
			raise TypeError ("Bad arugment")
		self.s1 = new_str 

	def get_int (self): 
		return (self.n1)

	def set_int (self, new_int): 
		if type (new_int) != int: 
			raise TypeError ("Bad argument")
		self.n1 = new_int

# Inheritor 
class DerivedClass (BaseClass): 

	def __init__ (self, s1, n1, f1): 
		if type (s1) != str or type (n1) != int or type (f1) != float: 
			raise TypeError ("Bad argument")

		BaseClass.__init__ (self, s1, n1) 
		self.f1 = f1 

	def get_float (self): 
		return self.f1 

	def set_float (self, new_float): 
		if type (new_float) != float: 
			raise TypeError ("Bad argument")
		self.f1 = new_float

	def derived_static_method (): 
		print ("BaseClass.base_d1_attr:", BaseClass.base_d1_attr) 
		BaseClass.base_static_method () 

def main (): 

	d1 = DerivedClass ("Hello", 10, 3.14)

	print ("str:", d1.get_str ())
	print ("int:", d1.get_int ())
	print ("float:", d1.get_float ())
	DerivedClass.derived_static_method () 

	d1.set_str ("New Str")
	d1.set_int (1000)
	d1.set_float (31.4)

	print ("str:", d1.get_str ())
	print ("int:", d1.get_int ())
	print ("float:", d1.get_float ())

	# Top level scope name
	print ("Top level name:", __name__)
	# Class name 
	class_instance = d1.__class__
	print ("Class instance:", class_instance)
	print ("Type of class_instance:", type (class_instance))

	print ("Basename:", class_instance.__name__)
	print ("Class attributes")
	attr_dict = class_instance.__dict__ 
	for attr in attr_dict: 
		print ("attr:", attr, "Value:", attr_dict[attr])

	print ("Object attributes")
	attr_dict = d1.__dict__
	for attr in attr_dict: 
		print ("attr:", attr, "Value:", attr_dict[attr])

	sys.exit (0)

main () 