line = "-" * 65
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print (line, "__new__")
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        print (line, "end __new__")
        if not 'meth' in classdict.keys(): 
            raise AttributeError("meth MUST be defined in SPAM") 
        return type.__new__(meta, classname, supers, classdict)


class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of MetaOne
    data = 1                              # Class data attribute
    print("I AM HERE")
    def meth1(self, arg):                  # Class method attribute
        return self.data + arg

print("type(Spam):", type(Spam)) 
print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
print (line, "END OF PROGRAM")

Spam = MetaOne(classname, supers, classdict,)