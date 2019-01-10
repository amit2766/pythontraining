#! /usr/bin/python3 
X = "Hello" 
def f1 (): 
    def f2 (): 
        def f3 (): 
            nonlocal X 
            print ("f3:X:", X) 
            X = 500           
        print ("f2:X:", X) 
        f3 () 
        print ("f2:X:", X) 
    f2 () 
f1 () 
