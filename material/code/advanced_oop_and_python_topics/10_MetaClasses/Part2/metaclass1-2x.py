line = "-" * 65
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
    	print (line, "__new__")
    	print ("meta:", meta, "type (meta):", type (meta))
    	print ("classname:", classname, "type (classname):", type (classname)) 
    	print ("supers:", supers, "type (supers):", type (supers))
    	print ("classdict:", classdict, "type(classdict):", type (classdict))
    	print (line, "end __new__")
    	return type.__new__(meta, classname, supers, classdict)

class Eggs(object, metaclass=MetaOne):
    pass

print('making class')
class Spam(Eggs, object):                 # Inherits from Eggs, instance of MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print ("type (Eggs):", type (Eggs))
print ("type (Spam):", type (Spam))

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
print (line, "END OF PROGRAM")
