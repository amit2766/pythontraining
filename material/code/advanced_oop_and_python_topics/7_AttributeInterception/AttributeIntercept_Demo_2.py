import sys 

class Wrapper:
	def __init__(self, obj):
		self.wrapped = obj
	def __getattr__(self, attrname):
		print('Trace: ' + attrname)
		return getattr(self.wrapped, attrname)

def main (): 
	X = Wrapper([1, 2, 3])
	X.append(4)
	print(X.wrapped)
	sys.exit (0) 

main () 
