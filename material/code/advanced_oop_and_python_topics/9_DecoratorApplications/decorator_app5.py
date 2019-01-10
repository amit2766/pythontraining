import sys 

# A call tracer decorator for both functions and methods
def tracer(func):
	calls = 0
	def onCall(*args, **kwargs):
		nonlocal calls
		calls += 1
		print('call %s to %s' % (calls, func.__name__))
		return func(*args, **kwargs)
	return onCall

@tracer
def spam(a, b, c):				# spam = tracer(spam)
	print(a + b + c)			# onCall remembers spam

@tracer						
def eggs(N):
	return 2 ** N

class Person:
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	@tracer
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)
	
	@tracer
	def lastName(self):
		return self.name.split()[-1]

def main (): 
	spam(1, 2, 3)				# Runs onCall(1, 2, 3)
	spam(a=4, b=5, c=6)
	print(eggs(10))
	print(eggs(5))

	print('methods...')
	bob = Person('Bob Smith', 50000)
	sue = Person('Sue Jones', 100000)
	print(bob.name, sue.name)
	sue.giveRaise(.10)
	print(int(sue.pay))
	print(bob.lastName(), sue.lastName())


main () 
