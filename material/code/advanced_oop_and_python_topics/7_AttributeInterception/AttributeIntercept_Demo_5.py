import sys 

# This program avoid inifinite loop by 
# explicitly calling __getattribute__ 
# of object class. We can handle case 
# separately for each attribute 

class TestClass:
    def __init__(self, n1, n2): 
        self._n1 = n1 
        self._n2 = n2 
    def __getattribute__(self, attr): 
        if attr == '_n1':
            tmp = object.__getattribute__ (self, '_n1') + 10 
        elif attr == '_n2': 
            tmp = object.__getattribute__ (self, '_n2') + 10 
        return (tmp) 

def main (): 
    inT = TestClass (100, 200)
    print ("inT._n1:", inT._n1) 
    print ("inT._n2:", inT._n2)
    sys.exit (0) 

main () 
