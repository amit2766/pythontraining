class T1: 
	def __init__(self, n):
		self.n = n 
	def prnt (self): 
		print ("T1:n", self.n)

class T2: 
	def __init__(self, n): 
		self.n = n 
	def prnt (self): 
		print ("T2:self.n", self.n)

class T3 (T2, T1): 
	def __init__(self, n1, n2, n3):
		T1.__init__(self, n1)
		T2.__init__(self, n2)
		self.n = n3 

def main ():

	t = T3 (10, 3.14, "Hello") 
	t.prnt () 
	print (T3.__mro__)

main () 