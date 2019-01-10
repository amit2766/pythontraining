# This program demonstrates computer attributes 

import sys 

class PropSquare:
	def __init__(self, start):
		self.value = start
	def getX(self):					# On attr fetch
		return self.value ** 2
	def setX(self, value):			# On attr assign
		self.value = value
	X = property(getX, setX)		# No delete or docs

# Note implicit association of X and val. X = f (val)

def main (): 

	P = PropSquare(3) 	# Two instances of class with property
	Q = PropSquare(32) 	# Each has different state information
	print(P.X) 			# 3 ** 2 = 9 
	P.X = 4 
	print(P.X) 			# 4 ** 2 = 16 
	print(Q.X) 			# 32 ** 2 = 1024

main () 


