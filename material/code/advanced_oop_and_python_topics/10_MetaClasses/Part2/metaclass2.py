class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', classname, supers, classdict, sep='\n...')
        supers = supers + (T, )
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        # Class.foo = 100 
        print ("-" * 65, "__init__")
        print ("Class:", Class, "type (Class):", type (Class))
        print ("classname:", classname, "type (classname):", type (classname))
        print ("Supers:", supers, "type (supers):", type (supers))
        print ("classdict:", classdict, "type (classdict):", type (classdict))
        print('...init class object:', list(Class.__dict__.keys()))
        print("Class.__bases__:", Class.__bases__)
        print ("-" * 65, "END __init__")

class Eggs:
    pass

class T:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaTwo):      # Inherits from Eggs, instance of MetaTwo
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
       return self.data + arg

# Observe that both methods __new__ and __init__ are executed
# after class definition is encountered 

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
