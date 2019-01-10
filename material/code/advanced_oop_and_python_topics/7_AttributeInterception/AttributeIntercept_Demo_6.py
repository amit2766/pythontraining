import sys 
# Try getattr, setattr on idle3. 
class Person: 
    def __init__(self, name): 
        self._name = name 
    def __getattr__(self, attr): 			# object.attr RHS Use
        print ("get:", attr)
        if attr == 'name': 
            return self._name 
        else: 
            raise AttributeError (attr)
    def __setattr__(self, attr, value): 	# obj.attr = value LHS use 
        print ("set:", attr) 
        if attr == 'name': 
            attr = '_name'
        self.__dict__[attr] = value 		# Avoid recursion 
    def __delattr__(self, attr): 
        print ("del:", attr)
        if attr == 'name': 
            attr = '_name'
        if not attr in self.__dict__.keys(): 
            raise AttributeError(attr)
        del self.__dict__[attr]
def main ():
    p1 = Person ("Rodger") 
    print (p1.name) 
    p1.name = "Rafa" 
    print (p1.name) 
    del (p1.name)
    p1.height = 10
    del(p1.height) 
    try:
        del(p1.width)
    except AttributeError:
        print("No attribute 'width' to delete")
    sys.exit (0)
main () 
