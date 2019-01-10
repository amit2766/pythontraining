#! /usr/bin/python3 

def f1 (): 
    X = 100 
    def f2 (): 
        global X
        X = 50000
        print ("f2:X:", X, "hex (id (X)):", hex (id (X)))
    f2 () 
f1 () 
print ("g:X:", X, "hex (id (X)):", hex ( id (X)))
