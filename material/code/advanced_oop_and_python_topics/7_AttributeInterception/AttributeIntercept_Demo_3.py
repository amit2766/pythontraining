import sys 

# This program loops infinitely 

cnt = 0 

class TestClass:
	def __init__(self, n1, n2): 
		self._n1 = n1 
		self._n2 = n2 

	def __getattribute__(self, attr): 
            global cnt
            cnt = cnt + 1
            print(cnt) 
            #tmp = self._n1 + 10 
            tmp = object.__getattribute__(self, attr) + 10
            return (tmp)
def main (): 
	inT = TestClass (100, 200)
	print (inT._n1, inT._n2) 
	sys.exit (0) 

main () 
