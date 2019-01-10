line = "-" * 65
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print (line, "__new__")
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        print (line, "end __new__")
        print("type(meta):", type(meta))
        print("type(classname):", type(classname))
        print("type(supers):", type(supers))
        print("type(classdict):", type(classdict)) 
        t = type.__new__(meta, classname, supers, classdict)
        print("type(t):", type(t))
        return (t) 


class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print("type(Spam):", type(Spam)) 
print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
print (line, "END OF PROGRAM")
