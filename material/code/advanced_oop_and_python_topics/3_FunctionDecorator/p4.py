#! /usr/bin/python3 

import sys, random 

class Callable: 
    def __init__(self): 
        def test_function (n):
            print ("n:", n, "type (n):", type (n))
        self.to_be_called = test_function 
    def __call__(self, x): 
        self.to_be_called (x) 

def main (): 

    c1 = Callable ()
    for i in range (5):
        c1(random.randint (0, 1000)) 

    sys.exit (0) 

main () 
