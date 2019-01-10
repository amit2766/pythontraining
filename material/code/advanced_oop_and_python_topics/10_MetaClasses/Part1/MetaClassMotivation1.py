# Adding methods to class via inheritance. 
# This is too static. 

class Extras:
	def extra(self, args):			# Normal inheritance: too static
		...

class Client1(Extras): ... 			# Clients inherit extra methods
class Client2(Extras): ... 
class Client3(Extras): ... 

X = Client1() 						# Make an instance
X.extra() 							# Run the extra methods
