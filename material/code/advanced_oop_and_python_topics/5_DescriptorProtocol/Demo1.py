import sys 

class Descriptor: 
    def __get__(self, instance, owner): 
        print("type(self):", type(self)) 
        print("type(instance):", type(instance))
        print("type(owner):", type(owner)) 
        return instance.__dict__['x'] ** 2 

class X: 
    def __init__(self, x): 
        self.x = x 
    
    attr = Descriptor() 

def main(): 
    
    ObjX = X(500) 
    print(ObjX.attr)  

    sys.exit(0) 

main() 
