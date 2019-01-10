#! /usr/local/bin/python3 

class Stack: 

	def __init__(self):
		self.lst = [] 

	def push (self, element): 
		self.lst.append (element)

	def pop (self): 
		if len (self.lst) == 0: 
			raise ValueError ("pop:stack empty")
		return self.lst.pop ()

	def examine_stack_top (self): 
		if len (self.lst) == 0: 
			raise ValueError ("est:stack empty")
		return self.lst[len (self.lst) - 1]
		
	def is_stack_empty (self): 
		return len (self.lst) == 0

def main (): 
	st1 = Stack ()
	st1.push (10) 
	st1.push (20) 
	st1.push (30) 
	print ("st1:top:", st1.examine_stack_top ())
	print ("st1.pop1:", st1.pop ())
	print ("st1.pop2:", st1.pop ())
	print ("st1.pop3:", st1.pop ())
	print ("st1.is_stack_empty:", st1.is_stack_empty ())
	print ("st1.pop4:", st1.pop ())

main ()
