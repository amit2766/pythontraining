# This program will demonstrate use of __getattr__ and __setattr__ 
# for computed attributes! 

import sys 

class AttrSquare:

	def __init__(self, start):
		self.value = start					# Triggers __setattr__!

	def __getattr__(self, attr):			# On undefined attr fetch
		if attr == 'X':
			return self.value ** 2			
		else:
			raise AttributeError (attr)

	def __setattr__(self, attr, value):		# On all assignments. 	
		if attr == 'X':
			attr = 'value'
		self.__dict__[attr] = value

def main (): 

	A = AttrSquare(3) 		# 2 instances of class with overloading
	B = AttrSquare(32) 		# Each has different state information
	print(A.X) 				# 3 ** 2
	A.X = 4 
	print(A.X) 				# 4 ** 2
	print(B.X) 				# 32 ** 2 (1024)

	sys.exit (0) 

main () 
