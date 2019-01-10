#! /usr/bin/python3 

import sys

def f1 ():
    X = 10
    def f2 (n, num1=X):
       return (num1 ** n) 
    return (f2) 

def main (): 
    ref_f2 = f1 ()
    print ("ref_f2 (2):", ref_f2 (2))
    print ("ref_f2 (3):", ref_f2 (3))
    sys.exit (0) 

main ()

