line = "-" * 65
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print (line, "__new__")
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        print (line, "end __new__")
        supers = supers + (T,) 
        print("supers:", supers) 
        return type.__new__(meta, classname, supers, classdict)

class T: 
    pass 

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
print("Spam.__bases__:", Spam.__bases__) 
print("type(X):", type(X)) 
print("type(Spam):", type(Spam)) 
print (line, "END OF PROGRAM")
