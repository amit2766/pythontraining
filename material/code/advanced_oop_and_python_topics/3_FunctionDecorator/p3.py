#! /usr/bin/python3 

import sys 

class Callable: 
    def __init__(self): 
        self.to_be_called = lambda : print ("I am in to_be_called") 
    def __call__(self): 
        self.to_be_called () 

def main (): 

    c1 = Callable ()
    for i in range (5):
        c1() 

    sys.exit (0) 

main () 
