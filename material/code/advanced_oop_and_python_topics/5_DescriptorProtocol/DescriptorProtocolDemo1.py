import sys 

# X.attr -> Descriptor.__get__(Subject.attr, X, Subject)

class Descriptor: 
    def __get__(self, instance, owner): 
        #print (self, instance, owner)
        print("type(self):", type(self))
        print("type(instance):", type(instance))
        print("hex(id(instance):", hex(id(instance)))
        print("type(owner):", type(owner)) 

class Subject: 
    attr = Descriptor () 

def main (): 
    line = "-" * 65
    X = Subject () 
    print("type(X):", type(X)) 
    print("hex(id(X)):", hex(id(X))) 
    print (line)
    p = X.attr 
    q = Subject.attr
    sys.exit (0) 

main () 
