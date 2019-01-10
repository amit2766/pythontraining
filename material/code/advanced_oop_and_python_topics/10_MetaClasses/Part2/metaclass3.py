# A simple function can serve as a metaclass too

def MetaFunc(classname, supers, classdict):
	print ("-" * 65, "MetaFunc")
	print ("Classname:", classname, "type (classname):", type (classname))
	print ("Supers:", supers, "type (supers):", type (supers))
	print ("classdict:", classdict, "type (classdict):", type (classdict))
	print ("-" * 65, "END MetaFunc")
	return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):            # Run simple function at end
    data = 1                                     # Function returns class
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print ("type (Spam):", type (Spam))
print('data:', X.data, X.meth(2))
