class_name = "Foo"
class_parents = (object,)
class_body = """
def __init__(self, name):
    self.name = name

def print_name(self):
    print(self.name)
"""
#a new dict is used as local namespace
class_dict = {}

#the body of the class is executed using dict from above as local 
# namespace 
exec(class_body, globals(), class_dict)

# viewing the class dict reveals the name bindings from class body
print (class_dict)
#{'__init__': <function __init__ at 0x10066f8c8>, 'print_name': <function blah at 0x10066fa60>}
# final step of class creation
Foo = type(class_name, class_parents, class_dict)

in_foo = type.__call__(Foo, "xyz")  
in_foo.print_name () 
print("type(in_foo):", type(in_foo)) 

"""
class type: 
    def __call__(self, *args, **kwargs): 
        self : Foo 
        args : ("xyz", ) 
        kwargs : {} 
        --------------------------------
        X = __new__(Foo) 
        #type(X) : Foo 
        #Empty namespace 
        --------------------------------
        Y = type(X).__dict__['__init__'](X, args[0]) 
        return (Y) 
"""
