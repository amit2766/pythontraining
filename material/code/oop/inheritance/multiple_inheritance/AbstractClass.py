from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
	def delegate(self):
		self.action()
	@abstractmethod
	def action(self):
		pass

#X = Super () 
class Sub(Super): 
	pass

#X = Sub () 

class Sub2 (Super):
	def action(self):
		print('Test Message')

X = Sub2 ()
X.delegate () 



