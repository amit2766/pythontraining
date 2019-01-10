# Nested decorator patterns 
#	@A
#	@B
#	@C
#	def f(...):
#		...

# Rebinding : f = A(B(C(f)))

# Same with the class decorator 

# 	@A
#	@B
#	class C: 
#		..... definition of class C 
#	Rebinding : C = A(B(C)) 

import sys 

def d1(F): 
	return F
def d2(F): 
	return F
def d3(F): 
	return F

@d1
@d2
@d3
def func():
	print('Hello, Python World!')

def main (): 
	func () 
	sys.exit (0) 

main () 
# func = d1(d2(d3(func)))
# Prints "spam"
